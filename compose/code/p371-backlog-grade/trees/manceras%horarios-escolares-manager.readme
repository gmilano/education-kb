# horarios-escolares-manager

Generador de horarios de código abierto para colegios de primaria. **Un programa
de escritorio que se instala y se abre con doble clic**: sin servidor, sin
cuentas, sin contraseña. Instalador de Windows y AppImage de Linux.

Montar el horario de un colegio a mano le cuesta días de trabajo a jefatura de
estudios, y aun así acaba con un profesor dando clase en dos aulas a la vez.
Este proyecto modela el colegio —profesorado, grupos, asignaturas, espacios y
carga lectiva semanal— y genera un horario sin conflictos con un motor de
restricciones, para después revisarlo, ajustarlo e imprimirlo.

[Read this in English](README.md)

## Estado

**Base inicial, todavía no apto para producción.** Lo que ya funciona:

- [x] Modelo de dominio, migraciones y datos de ejemplo de un colegio español
- [x] Motor de restricciones (OR-Tools CP-SAT) con las restricciones duras de abajo, con tests
- [x] Validador independiente de horarios (`find_conflicts`) para ediciones manuales
- [x] Instalador de Windows y AppImage de Linux, copias de seguridad automáticas y actualización desde la propia app
- [x] API para profesorado, grupos, asignaturas, espacios, franjas,
      disponibilidad y carga lectiva, con las reglas de negocio en los servicios
- [x] Endpoints para lanzar el solver, guardar y publicar un horario, y validar
      las ediciones manuales contra las restricciones duras
- [x] Informe de carga que avisa de que el horario es imposible antes de resolver
- [x] Pantalla de profesorado, con las piezas compartidas de tabla, diálogo y
      formulario que reutilizarán el resto de pantallas
- [x] Pantallas para todas las entidades: profesorado, disponibilidad, grupos,
      asignaturas, aulas, franjas y carga lectiva, con informe de viabilidad
- [x] Rejilla semanal: lanzar el solver, ver conflictos, mover y bloquear
      sesiones con el servidor validando cada cambio, y publicar el horario
- [x] Vistas imprimibles y exportación CSV por profesor, grupo y aula
- [ ] Instalador firmado (hoy no lo está, así que Windows muestra un aviso de SmartScreen)
- [ ] Más de un curso escolar a la vez
- [ ] Versión para macOS
- [ ] Actualización desde la app en Linux (hoy solo en Windows)

## Restricciones que entiende el motor

Duras — un horario que incumpla una de ellas se rechaza:

- un profesor, un grupo y un aula están como mucho en un sitio por franja
- nadie da clase en una franja en la que no está disponible (jornada parcial, otras tareas)
- las asignaturas que necesitan un espacio concreto (gimnasio, aula de música, informática) lo tienen
- cada entrada de carga lectiva recibe exactamente sus sesiones semanales
- no se programa nada durante el recreo
- ningún profesor supera su máximo de sesiones semanales

Blandas — se minimizan, no se garantizan:

- evitar dos sesiones de la misma asignatura para el mismo grupo el mismo día

El modelo completo está en [`docs/domain-model.md`](docs/domain-model.md).

## Instalación (para el colegio)

### Windows

Descarga `Horarios-Setup-x.y.z.exe` de la
[última versión](https://github.com/manceras/horarios-escolares-manager/releases/latest)
y ejecútalo. Se instala para el usuario actual, así que no pide contraseña de
administrador, y deja *Horarios* en el escritorio y en el menú de inicio.

El instalador todavía no está firmado, así que la primera vez Windows muestra
**«Windows protegió su PC»**. Hay que pulsar *Más información* y después
*Ejecutar de todas formas*. Si quieres comprobarlo antes, junto al instalador se
publica su `.sha256`.

El programa se actualiza solo: cuando hay una versión nueva la ofrece en una
franja arriba de la ventana y se instala con un clic.

### Linux

Descarga `Horarios-x.y.z-x86_64.AppImage`, dale permisos y ejecútalo:

```sh
chmod +x Horarios-*.AppImage
./Horarios-*.AppImage
```

Sin gestor de paquetes, sin root, sin instalar nada. Se abre en una ventana de
Chromium sin pestañas ni barra de direcciones si la hay, y en el navegador por
defecto si no. En Linux no se actualiza solo: el aviso lleva a la página de
versiones.

### Dónde están los datos

Todo vive en una sola carpeta — `%LOCALAPPDATA%\Horarios\` en Windows,
`~/.local/share/horarios/` en Linux:

```
horarios.db      los datos del colegio
backups/         una copia de cada una de las últimas diez aperturas
horarios.log     lo que hay que enviar si algo falla
```

Copiar esa carpeta es una copia de seguridad completa, y llevársela a otro
ordenador es toda la mudanza. Desinstalar el programa no la borra.

## Ejecutar desde el código

Requisitos: Python 3.12+ con [uv](https://docs.astral.sh/uv/) y Node 22+ con
pnpm.

```sh
git clone https://github.com/manceras/horarios-escolares-manager.git
cd horarios-escolares-manager
make setup
make migrate
make seed          # colegio de ejemplo: 6 grupos, 9 profesores, 54 entradas
make dev           # API en :8000, web en :5173
```

Documentación interactiva de la API: <http://localhost:8000/docs>.

`make desktop` arranca la aplicación de escritorio tal cual, sin construir el
instalador.

## Construir el instalador

Lo construye GitHub Actions al publicar una etiqueta, porque PyInstaller no
puede compilar para Windows desde otro sistema:

```sh
# antes hay que subir app.__version__ en backend/app/__init__.py; CI lo comprueba
git tag v0.2.0 && git push origin v0.2.0
```

Los detalles están en [`packaging/`](packaging/).

## Contribuir

Se agradecen las contribuciones, sobre todo de quien hace horarios de verdad.
Empieza por [CONTRIBUTING.md](CONTRIBUTING.md) y por
[`docs/vertical-slice.md`](docs/vertical-slice.md).

Todo el código, los comentarios, la documentación y los mensajes de commit se
escriben en inglés. El texto que ve el usuario está en español y vive solo en
`frontend/src/locales/es.json`.

## Licencia

[MIT](LICENSE) © Antonio Mancera Gamez
