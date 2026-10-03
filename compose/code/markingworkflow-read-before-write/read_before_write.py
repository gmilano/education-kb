"""read-before-write de `markingworkflow` (patron P152, KB education pase 60).

Medido en moodle/moodle @ main, public/mod/assign/externallib.php (5.3rc2):
  - l. 464  el campo se asigna sin condicional
  - l. 584  esta en el contrato de salida y NO es VALUE_OPTIONAL
  - l. 401  leer exige mod/assign:view
  - l. 1033 escribir nota exige mod/assign:grade
Como view es estrictamente mas debil que grade, toda puerta que pueda calificar
puede leer la precondicion con el token que ya tiene.

Sin dependencias y sin red: el cliente de web service se inyecta.
"""


class RefuseToWrite(Exception):
    """Se rehusa escribir porque la plataforma no sostiene la garantia de borrador."""

    def __init__(self, reason, markingworkflow=None):
        super().__init__(reason)
        self.reason = reason
        self.markingworkflow = markingworkflow


DRAFT_STATE = "readyforreview"


def read_markingworkflow(ws_call, courseid, assignmentid):
    """Devuelve 0/1, o None si el dato no se pudo determinar.

    `ws_call(fn, **params)` es el mismo canal que la pieza ya usa para
    mod_assign_save_grade; no requiere capacidad adicional.
    """
    resp = ws_call("mod_assign_get_assignments", courseids=[courseid])
    if not isinstance(resp, dict):
        return None
    for course in resp.get("courses", []) or []:
        for a in course.get("assignments", []) or []:
            if a.get("id") == assignmentid:
                v = a.get("markingworkflow")
                if v is None:
                    return None
                try:
                    return int(v)
                except (TypeError, ValueError):
                    return None
    return None


def guarded_save_grade(ws_call, courseid, assignmentid, userid, grade, **extra):
    """Escribe la nota SOLO si la plataforma sostiene el estado de borrador.

    Falla cerrado: si markingworkflow no es 1, no escribe.
    """
    mw = read_markingworkflow(ws_call, courseid, assignmentid)

    if mw is None:
        raise RefuseToWrite(
            "no se pudo determinar markingworkflow para la assignment "
            "{}: se rehusa escribir (fallar cerrado)".format(assignmentid),
            markingworkflow=None,
        )
    if mw != 1:
        raise RefuseToWrite(
            "markingworkflow=0: esta assignment no tiene estado de borrador, "
            "cualquier escritura PUBLICA la nota. Se rehusa escribir. "
            "Activar 'Usar flujo de trabajo de calificacion' en la assignment "
            "y reintentar.",
            markingworkflow=mw,
        )

    params = dict(
        assignmentid=assignmentid,
        userid=userid,
        grade=grade,
        workflowstate=DRAFT_STATE,
    )
    params.update(extra)
    return ws_call("mod_assign_save_grade", **params)
