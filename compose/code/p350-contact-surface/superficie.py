#!/usr/bin/env python3
"""`P350` — la frontera de una accion hacia afuera es ANTES de «no mandar nada».

La accion A pre-registrada por el pase 110 pedia redactar 6 pedidos de cesion y medir
*«cuantos de los 6 tienen un canal de contacto resoluble DESDE EL PROPIO PAYLOAD (perfil,
correo en README, CODEOWNERS, package.json)»*, con prediccion **>=4** y rama de refutacion
**<=2**. La pre-registracion puso su frontera en el envio: *«la accion se detiene en REDACTAR:
no se manda nada»*.

🔴 **La frontera real de este entorno esta antes: ENUMERAR el canal de contacto ya es manejo
de datos personales, y la extraccion fue DENEGADA por politica (`PII Data Handling`).** Asi que
la prediccion no sale confirmada ni refutada: **no es medible aca**, que es un tercer resultado
que las dos ramas de la pre-registracion no admitian.

Lo que SI se midio, porque es ESTRUCTURA y no dato personal: que superficies de archivo
EXISTEN en los 6 repos, por presencia y tamano, sin leer su contenido.

🔵 **Y el resultado estructural decide la pregunta de todas formas, en la direccion de la rama
de refutacion:** ninguno de los 6 tiene una superficie de contacto LEGIBLE POR MAQUINA
(`CODEOWNERS` 0/6, `CITATION.cff` 0/6, `CONTRIBUTING.md` 0/6). La unica superficie que podria
cargar un canal es prosa libre (`README`, 6/6), que es exactamente lo que la politica protege.

**Consecuencia para `P342`:** recuperable en teoria, y en este entorno **ni enumerable**. Es un
enunciado mas fuerte que el *«inalcanzable en la practica»* de la rama de refutacion, y es sobre
el ENTORNO y la politica, no sobre los repos ni sobre sus titulares.

⚠️ No se intento por otra via, ni por otra herramienta, ni por un sub-agente. La denegacion se
registra y se respeta, que es lo mismo que el pase 61 hizo con el PR a `toshieji` y lo que el
pase 96 hizo con `[Exfil Scouting]`.
"""

# Los 6 falsos negativos `P342` del pase 110 (las 6 de 9 que la pre-registracion excluyo).
REPOS = (
    'NLP2CT/LLM-generated-Text-Detection',
    'RadiantCrystal/SafeTutors',
    'SabioTechTeam/Teacher-Hub',
    'eth-lre/mathtutorbench',
    'kaushal0494/AITutor-EvalKit',
    'kaushal0494/UnifyingAITutorEvaluation',
)

# Superficies sondeadas, por `raw.githubusercontent.com`, en `main` y `master`.
# 10 rutas x 2 ramas x 6 repos = 120 sondas.
SONDAS_POR_REPO = 20
RUTAS = ('README.md', 'README.rst', 'readme.md', 'CODEOWNERS', '.github/CODEOWNERS',
         'package.json', 'pyproject.toml', 'setup.py', 'CITATION.cff', 'CONTRIBUTING.md')

# MEDIDO el 2026-10-05: ruta -> {repo: bytes}. Solo presencia y tamano; el contenido
# NO se leyo y NO se publica.
PRESENCIA = {
    'README.md': {
        'NLP2CT/LLM-generated-Text-Detection': 40401,
        'RadiantCrystal/SafeTutors': 4609,
        'SabioTechTeam/Teacher-Hub': 15535,
        'eth-lre/mathtutorbench': 14935,
        'kaushal0494/AITutor-EvalKit': 14451,
        'kaushal0494/UnifyingAITutorEvaluation': 9525,
    },
    'package.json': {
        'SabioTechTeam/Teacher-Hub': 69,
    },
    'README.rst': {}, 'readme.md': {}, 'CODEOWNERS': {}, '.github/CODEOWNERS': {},
    'pyproject.toml': {}, 'setup.py': {}, 'CITATION.cff': {}, 'CONTRIBUTING.md': {},
}

# Las superficies que un barrido podria leer SIN prosa: declaran mantenedor de forma
# estructurada. Son las que deciden si `P342` es automatizable.
LEGIBLES_POR_MAQUINA = ('CODEOWNERS', '.github/CODEOWNERS', 'CITATION.cff')
# `package.json` declara `author`/`maintainers`, pero esos campos SON datos personales:
# se cuenta su PRESENCIA y no se lee.
ESTRUCTURADAS_CON_PERSONA = ('package.json', 'pyproject.toml', 'setup.py')


def cobertura(ruta):
    """(repos_con_la_ruta, total) — presencia, sin leer contenido."""
    return (len(PRESENCIA.get(ruta, {})), len(REPOS))


def superficie_legible_por_maquina():
    """Repos con al menos una superficie de contacto estructurada y SIN persona."""
    return sorted({r for ruta in LEGIBLES_POR_MAQUINA for r in PRESENCIA.get(ruta, {})})


def testigo_de_alcance():
    """Los repos cuyo README responde 200: prueba que el canal llega y que un 404
    en las otras rutas es AUSENCIA y no incapacidad de leer (`P294`)."""
    return sorted(PRESENCIA['README.md'])


def medible():
    """¿Se puede contestar la prediccion de la accion A en este entorno?"""
    return False


def veredicto_accion_a():
    return ('NO-MEDIBLE', 'enumerar canal de contacto denegado por politica (PII)')


if __name__ == '__main__':
    print('=== ACCION A del pase 110: %s ===' % veredicto_accion_a()[0])
    print('motivo: %s' % veredicto_accion_a()[1])
    print()
    print('=== SUPERFICIE DE ARCHIVO (presencia y tamano; contenido NO leido) ===')
    print('%-22s %s' % ('ruta', 'repos / total'))
    for ruta in RUTAS:
        n, t = cobertura(ruta)
        marca = 'OK ' if n else '   '
        print('%s%-22s %d / %d' % (marca, ruta, n, t))
    print()
    print('testigo de alcance (README 200): %d de %d' % (len(testigo_de_alcance()), len(REPOS)))
    print('superficie de contacto LEGIBLE POR MAQUINA: %d de %d'
          % (len(superficie_legible_por_maquina()), len(REPOS)))
    print('sondas: %d repos x %d = %d' % (len(REPOS), SONDAS_POR_REPO,
                                          len(REPOS) * SONDAS_POR_REPO))
