<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="img/openredlab-blanco.png">
    <img src="img/openredlab.png" alt="OpenRedLab" width="320">
  </picture>
</p>

# OpenRedLab

**Simulador de redes para aprender direccionamiento IP, subredes y diagnóstico.** Armás una red en el navegador, configurás direcciones, máscaras, puertas de enlace y rutas, y al hacer ping ves el recorrido del paquete paso a paso. Si falla, el simulador te dice en qué paso se cortó y por qué.

**Usalo online:** https://fhleonardi.github.io/openredlab/

No hace falta instalar nada: es un único archivo HTML, sin dependencias y sin conexión a internet. También podés descargar [`index.html`](index.html) y abrirlo con doble clic. Tu trabajo se guarda solo en el navegador: la próxima vez que lo abras, te ofrece recuperarlo.

**Guías:** [para el alumno](docs/guia-rapida-alumno.md) · [para docentes](docs/guia-docente.md), que explica cómo usarlo en clase y cómo armar laboratorios y desafíos.

## Qué podés hacer

- **Armar la red** con PC, servidores, routers, firewalls, switches, cámaras, dispositivos IoT, puntos de acceso y una nube Internet, unidos por cables de cobre, fibra o enlaces inalámbricos.
- **Elegir el equipo como en la realidad:** un router estándar (g0/0, fib0…) o tipo MikroTik (ether1, sfp1…), un firewall (wan, lan, dmz), switches de 8, 24 o 48 puertos, o un hub. En routers y firewalls podés agregar o quitar puertos y elegir el medio de cada uno.
- **Hacer ping** entre equipos o a un nombre (google.com) y seguir el recorrido: la decisión con IP «AND» máscara, la puerta de enlace, ARP, las tablas de rutas de cada router y la vuelta de la respuesta.
- **Ver las capas y el encapsulamiento:** cada paso del recorrido dice en qué capa ocurre (modelos OSI y TCP/IP), y *Cómo viaja el paquete* muestra las tramas de cada tramo: cambian las MAC en cada router, el paquete IP conserva su origen y su destino y el TTL baja uno por router.
- **Ver el paquete viajar:** después de un ping, una consulta DNS o una conexión, un paquete se mueve por el lienzo trama por trama: azul el pedido, verde la respuesta y, en TCP, violeta la apertura y naranja el cierre. Hay botones para pausar, repetir y cambiar la velocidad (×0.5 a ×4), y un clic en una trama salta a ese tramo. Si algo se corta o se rechaza, el paquete queda en rojo y marca el equipo con una ✗. El DORA de DHCP se anima igual, mensaje por mensaje.
- **Conectarse a servicios con TCP y UDP:** un servidor atiende HTTP, HTTPS, SSH, FTP, SMTP o un puerto propio; *Conectar* muestra el socket (IP:puerto ↔ IP:puerto), el handshake de tres pasos, el pedido y la respuesta, y el cierre, o los datagramas de UDP. Si nadie escucha en el puerto, el diagnóstico lo dice (D31): la red llega, el servicio no.
- **Capturar el tráfico como Wireshark:** la pestaña *Captura* registra lo que pasa por un cable (o por todos) mientras hacés pings, consultas DNS y conexiones: número, origen, destino, protocolo e info, el detalle por capas de cada paquete y un filtro (`icmp`, `dns`, `tcp.port==80`, `ip.addr==…`).
- **Medir la calidad del enlace (QoS):** cada cable tiene latencia, jitter y pérdida; el ping manda 1, 4, 10 o 50 paquetes y, como el ping real, informa los perdidos y el tiempo mínimo, medio y máximo. Si no vuelve ninguno, el diagnóstico lo explica (D32).
- **Ver los dominios de colisión y de broadcast:** el selector *Dominios* del lienzo pinta cada dominio con un color y los cuenta. El hub repite cada trama por todos sus puertos; el switch separa un dominio de colisión por puerto; el router corta el broadcast.
- **Resolver nombres reales de internet (a pedido):** con el interruptor «Resolver nombres reales» prendido, los nombres que la simulación no conoce (example.com, por ejemplo) se consultan a Cloudflare por DNS sobre HTTPS. Es lo único que la página manda por la red: viene apagado, sólo sale el nombre que escribís, y una política de seguridad la limita a ese único servidor.
- **Resolver nombres con DNS:** un servidor DNS propio con su zona (registros A, CNAME, MX, NS y PTR) y, para los nombres de internet, la resolución por la jerarquía: consulta recursiva al servidor y consultas iterativas a la raíz, al TLD y al autoritativo, con caché. El DNS inverso también: un servidor con una zona `in-addr.arpa` responde qué nombre tiene una IP. **Consultar DNS** muestra la respuesta como `nslookup`, para cualquier tipo de registro.
- **Cortar y apagar en vivo:** un clic corta un cable o apaga un equipo, y otro lo restaura, sin cambiar el diseño; después se repite el ping, el DNS o la conexión para ver qué pasa cuando algo se cae.
- **Entender las fallas:** cada problema tiene un diagnóstico (D01 a D35) que explica qué pasó en lenguaje llano y sugiere qué revisar: máscara mal elegida, puerta de enlace fuera de la red, ruta de vuelta faltante, IP duplicada, cable caído, regla de filtrado, entre otros.
- **Calcular subredes** con el equipo seleccionado: IP y máscara en binario, clase de la IP (y si es privada o pública), red, broadcast, rango de hosts y si la puerta de enlace está en la red.
- **Ver DHCP** con los cuatro mensajes DORA animados sobre los cables.
- **Salir a internet con NAT:** el router o firewall de borde cambia la IP privada de origen por su IP pública, y a la respuesta la traduce de vuelta; se ve en el recorrido y en las tramas. Sin NAT, el pedido llega pero la respuesta no vuelve, y el simulador lo explica (D28).
- **Unir sitios por internet:** si la IP pública de destino es de un equipo del lienzo, la nube le lleva el paquete hasta su sitio. Cada sitio puede tener su nube, pero todas son la misma internet. El ejemplo *Dos sitios por internet* tiene una PC en su casa que consulta un servidor web de la oficina. Si internet no llega hasta ese equipo, el diagnóstico lo dice (D34).
- **Publicar un servidor con redirección de puertos:** en la pestaña *NAT* del router, lo que llega a su IP pública por un protocolo y un puerto se reenvía a un equipo de adentro. Las tramas muestran el cambio de IP y de puerto de destino en el borde. El ejemplo *Servidor publicado con redirección de puertos* lo arma con el servidor de la oficina en una IP privada.
- **Filtrar tráfico** con reglas por red de origen y destino, protocolo (ICMP, TCP, UDP), puerto de destino y puerto por el que entra el paquete, más una política por defecto (permitir o bloquear). El router revisa cada paquete; el firewall recuerda las conversaciones y deja volver las respuestas. Un firewall nuevo bloquea lo que entra por wan.
- **Verificar un diseño VLSM:** el de un desafío del docente o uno propio. En una red armada por vos, el simulador detecta los sectores solo y revisa subredes solapadas o desalineadas y puertas de enlace; si cargás los hosts de cada sector y el bloque, también revisa si alcanzan.
- **Resolver laboratorios de diagnóstico:** redes con fallas plantadas y objetivos que hay que cumplir. En un laboratorio el simulador no avisa las fallas mientras configurás: encontrarlas es el ejercicio.
- Exportar e importar la red como JSON, deshacer y rehacer, tema oscuro y modo presentación para el aula.

## Escenarios

En el selector **Ejemplos…** vienen redes listas: una básica, dos subredes, un complejo turístico completo, el mismo complejo con fallas, un desafío VLSM, un router de 8 puertos, una oficina con DNS propio y cuatro topologías: estrella, bus (con un hub), malla entre routers y dos LAN unidas por una WAN, y dos proveedores de internet unidos por peering, con un proveedor de tránsito.

En [`escenarios/`](escenarios/) hay archivos para abrir con **Importar** o arrastrándolos al lienzo:

| Archivo | Para qué |
|---|---|
| `lab1-ALUMNO.json` | Lab 1: un solo problema |
| `lab2-ALUMNO.json` | Lab 2: tres problemas |
| `lab3-ALUMNO.json` | Lab 3: el problema invisible |
| `lab4-ALUMNO.json` | Lab 4: la oficina sin servicios (intranet, DNS e internet) |
| `desafio-complejo-termal.json` | Desafío VLSM: Complejo Termal Río Verde, sin direccionar |

## Para docentes

- La [guía para docentes](docs/guia-docente.md) explica el uso en clase, cómo armar laboratorios y desafíos, y el formato de los archivos.
- En modo **Docente**, la pestaña **Laboratorio** arma fallas, objetivos y sectores en pantalla, eligiendo de la red abierta, y compara cada objetivo en la red sana y en la del alumno. El botón **Exportar para el alumno** genera la versión que se reparte: la red con las fallas aplicadas y sin la lista de fallas (en un desafío VLSM, sin direccionar).
- Las versiones docentes de los laboratorios incluidos, con la red resuelta, no se publican para que los alumnos no tengan las soluciones a mano. Si las necesitás, pedíselas al autor. Para armar las tuyas, el ejemplo **Complejo roto (docente)** sirve de plantilla.

## Cómo está hecho

Cinco capas en JavaScript sin dependencias. Cada una tiene sus propias autopruebas y no conoce a las siguientes:

| Capa | Archivo | Qué hace |
|---|---|---|
| 1 | [`capa1-red.js`](capa1-red.js) | Aritmética de direcciones: máscaras, subredes, binario |
| 2 | [`capa2-motor.js`](capa2-motor.js) | El motor: ping paso a paso, ARP, rutas, DHCP, DNS, filtrado y diagnósticos |
| 3 | [`capa3-escenarios.js`](capa3-escenarios.js) | Validación, importar y exportar, ejemplos, laboratorios, modelos de equipos y verificación VLSM |
| 4 | [`capa4-ui.js`](capa4-ui.js) | La interfaz: lienzo, paleta, propiedades y paneles |
| 5 | [`capa5-autotest.js`](capa5-autotest.js) | Arranque y Autotest |

`index.html` se genera a partir de las cinco capas; no se edita a mano. Después de cambiar una capa:

```sh
python3 herramientas/ensamblar.py              # reescribe index.html
python3 herramientas/ensamblar.py --verificar  # comprueba que coincida con las capas
```

Para probar, abrí `index.html` en el navegador. El botón **Autotest** muestra los casos de redes; en la consola, `Autotest.correr({ tecnico: true })` corre además los criterios de la interfaz y las autopruebas de las capas 1 a 3 (también disponibles por separado: `Red.autopruebas()`, `Motor.autopruebas()`, `Escenarios.autopruebas()`).

**Carpetas del repositorio:**

| Carpeta | Contenido |
|---|---|
| raíz | `index.html` y las cinco capas |
| [`docs/`](docs/) | Las guías para alumnos y docentes |
| [`escenarios/`](escenarios/) | Laboratorios y desafíos para importar |
| [`herramientas/`](herramientas/) | El ensamblador de `index.html` y las pruebas del simulador (`pruebas/`) |
| [`img/`](img/) | Logo (color y blanco), marca y favicons |

## Versiones

OpenRedLab numera sus versiones como MAYOR.MENOR.PARCHE. La versión actual figura al pie de la pestaña **Ayuda**, y en [`CHANGELOG.md`](CHANGELOG.md) está lo que trajo cada una. Cada versión publicada tiene su [release](https://github.com/fhleonardi/openredlab/releases).

- **Archivos de red:** llevan el número de su formato (`version`, hoy 1) y la versión del simulador que los exportó (`generador`).
  - El formato sólo cambia si un dato existente cambia o desaparece. Un archivo de un formato anterior se actualiza solo al abrirlo.
  - Un archivo de un formato más nuevo no se abre: el simulador dice con qué versión se hizo.
- **Para contribuir:** cada cambio a una capa sube la versión en `Escenarios.VERSION_APP` (`capa3-escenarios.js`) y suma su entrada al tope de `CHANGELOG.md`. Si no coinciden, `ensamblar.py` no arma el `index.html`. Al mergear, la versión se publica con su tag (`vX.Y.Z`) y su release.

## Simplificaciones

Es una herramienta para aprender, no un emulador: las rutas se cargan a mano (no hay OSPF, BGP ni RIP), no hay VLAN ni IPv6, el NAT es de salida y con redirección de puertos (sin otras formas de NAT de destino), no hay retransmisiones ni control de congestión en TCP, DHCP reparte un rango por router y sin relay, y el wireless se modela por distancia. La pestaña **Ayuda** del simulador lista todas.

## Reportar un problema

Si algo no funciona como esperabas o un diagnóstico explica mal lo que pasó, abrí un [issue](https://github.com/fhleonardi/openredlab/issues) con la red exportada (*Exportar*) y los pasos para reproducirlo.

## Quién lo hace

OpenRedLab lo desarrolla Francisco Leonardi con [Open Tecnología](https://opentecnologia.ar), una empresa de servicios de IT de Gualeguaychú, Entre Ríos. Nació para la cátedra de redes y se publica como código abierto para que cualquier docente o alumno lo use y lo mejore.

## Licencia

[MIT](LICENSE) © 2026 Francisco Leonardi

Los iconos de varios equipos son de [Tabler Icons](https://tabler.io/icons), también con licencia MIT: ver [AVISOS.md](AVISOS.md).
