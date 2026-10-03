"""20 asertos, sin red. ESCRITOS Y NO CORRIDOS en el pase 60 (ver README)."""

from read_before_write import (
    DRAFT_STATE,
    RefuseToWrite,
    guarded_save_grade,
    read_markingworkflow,
)

ASSERTS = 0


def check(cond, label):
    global ASSERTS
    ASSERTS += 1
    if not cond:
        raise AssertionError(label)


def fake(assignments, record=None):
    """ws_call de mentira; `record` acumula las llamadas de escritura."""

    def ws_call(fn, **params):
        if fn == "mod_assign_get_assignments":
            return {"courses": [{"assignments": assignments}]}
        if fn == "mod_assign_save_grade":
            if record is not None:
                record.append(params)
            return {"ok": True}
        raise AssertionError("fn inesperada: " + fn)

    return ws_call


def test_lectura():
    ws = fake([{"id": 7, "markingworkflow": 1}])
    check(read_markingworkflow(ws, 1, 7) == 1, "lee 1")
    ws = fake([{"id": 7, "markingworkflow": 0}])
    check(read_markingworkflow(ws, 1, 7) == 0, "lee 0")
    ws = fake([{"id": 7, "markingworkflow": "1"}])
    check(read_markingworkflow(ws, 1, 7) == 1, "coacciona string")
    ws = fake([{"id": 9, "markingworkflow": 1}])
    check(read_markingworkflow(ws, 1, 7) is None, "assignment ausente -> None")
    ws = fake([{"id": 7}])
    check(read_markingworkflow(ws, 1, 7) is None, "campo ausente -> None")
    ws = fake([{"id": 7, "markingworkflow": "x"}])
    check(read_markingworkflow(ws, 1, 7) is None, "ilegible -> None")
    ws = fake([])
    check(read_markingworkflow(ws, 1, 7) is None, "sin assignments -> None")


def test_rama_buena():
    rec = []
    ws = fake([{"id": 7, "markingworkflow": 1}], rec)
    guarded_save_grade(ws, 1, 7, 42, "8.0")
    check(len(rec) == 1, "escribio exactamente una vez")
    check(rec[0]["workflowstate"] == DRAFT_STATE, "workflowstate es borrador")
    check(rec[0]["workflowstate"] == "readyforreview", "el literal es readyforreview")
    check(rec[0]["userid"] == 42, "userid pasa")
    check(rec[0]["grade"] == "8.0", "grade pasa")
    check("released" not in rec[0], "no manda released")


def test_rama_mala_no_escribe():
    # el control que importa: markingworkflow=0 NO debe escribir NADA
    rec = []
    ws = fake([{"id": 7, "markingworkflow": 0}], rec)
    try:
        guarded_save_grade(ws, 1, 7, 42, "8.0")
        check(False, "debio rehusar con markingworkflow=0")
    except RefuseToWrite as e:
        check(e.markingworkflow == 0, "reporta la casilla")
        check("PUBLICA" in e.reason, "explica el motivo real")
    check(rec == [], "CONTROL: no escribio nada con markingworkflow=0")


def test_falla_cerrado():
    for assignments, label in (
        ([{"id": 7}], "campo ausente"),
        ([], "assignment ausente"),
        ([{"id": 7, "markingworkflow": None}], "campo nulo"),
    ):
        rec = []
        ws = fake(assignments, rec)
        try:
            guarded_save_grade(ws, 1, 7, 42, "8.0")
            check(False, "debio rehusar: " + label)
        except RefuseToWrite:
            check(rec == [], "no escribio: " + label)


def test_control_negativo():
    # si el guard estuviera roto y escribiera siempre, test_rama_mala fallaria.
    # este control verifica que el fake DETECTA una escritura.
    rec = []
    ws = fake([{"id": 7, "markingworkflow": 1}], rec)
    ws("mod_assign_save_grade", assignmentid=7)
    check(len(rec) == 1, "CONTROL NEGATIVO: el fake registra escrituras")


if __name__ == "__main__":
    test_lectura()
    test_rama_buena()
    test_rama_mala_no_escribe()
    test_falla_cerrado()
    test_control_negativo()
    print("{}/{} OK".format(ASSERTS, ASSERTS))
