# 🚌 Trasporte Chile (DaaS)
> **Infraestructura comunitaria de datos abiertos de transporte para democratizar la movilidad en regiones.**

[![License: AGPL v3] pendiente

---

## 📌 Visión & Misión

En Chile, la brecha de información de transporte entre la capital y las regiones es crítica. Mientras Santiago cuenta con sistemas avanzados de telemetría, en las provincias, zonas rurales y periferia en general los recorridos de micros, colectivos y transporte informal vecinal operan sin visibilidad digital.

**Nuestra misión** es construir un espacio colaborativo donde los ciudadanos puedan informar e informarse sobre sus opciones de movilidad. No desarrollamos una aplicación de usuario final cerrada: operamos como una **Plataforma de Datos como Servicio (Data-as-a-Service - DaaS)**. El valor de nuestro proyecto no reside en una pantalla, sino en la **información estructurada, limpia, georreferenciada y estandarizada.**

---

## ⚙️ Arquitectura del Motor de Datos (Pipeline DaaS)

El backend opera como un motor invisible dividido en cuatro capas esenciales:

[ WhatsApp / Telegram / QRs ] ──> ( 1. Ingesta )
│
▼
( 2. Validación & NLP )
│
▼
( 3. Estandarización ) ──> [ GTFS / GTFS-RT ]
│
▼
( 4. Distribución ) ────> [ Google Maps / MTT / APIs ]


1. **Ingesta Multi-Canal (Zero-Friction):** Captura de datos no estructurados y de telemetría ciudadana a través de interfaces conversacionales (WhatsApp, Telegram) y puntos de acceso físico (códigos QR en garitas, paraderos y terminales).
2. **Procesamiento, NLP y Validación:** Extracción de entidades con procesamiento de lenguaje natural, georreferenciación y filtros algorítmicos de consenso espacial/temporal para descartar reportes falsos y mitigar ruido.
3. **Estandarización:** Modelado topológico y conversión automática al estándar internacional de la industria: **GTFS Schedule** (estático) y **GTFS-Realtime** (dinámico).
4. **Distribución ("as a Service"):** Exposición de feeds y endpoints seguros (REST APIs) para consumo de terceros, entidades públicas y plataformas globales de mapas.

---

## 📡 Canales de Recopilación y Tipología de Datos

### Canales
* **Bots Conversacionales (WhatsApp / Telegram):** Operan de forma bidireccional. Permiten al usuario reportar eventos (desvíos, atochamientos, aforo, rutas) y compartir viajes en vivo (Live Location), además de consultar recorridos y horarios estimados en lenguaje natural.
* **QRs Físicos en Terreno:** Desplegados en paradas, garitas y terminales para disparar flujos prellenados de reporte comunitario o consulta rápida sin descarga de apps.

### Datos Capturados
* Rutas y frecuencias de buses regionales, provinciales e interurbanos.
* Líneas y variantes de taxis colectivos locales.
* Redes de transporte particular y vecinal (apoyo comunitario).

---

## 🛠️ Stack Tecnológico

* **Análisis y Grafos de Rutas:** [NetworkX](https://networkx.org/) para el modelado de redes y conectividad topológica.
* **Georreferenciación Base:** [OpenStreetMap (OSM)](https://www.openstreetmap.org/) para el trazado vial y cálculo de distancias de shapes.
* **Manipulación y Procesamiento de Datos:** [Pandas](https://pandas.pydata.org/) para limpieza, filtrado y consolidación tabular.
* **Datos Base de Calibración:** Feeds oficiales DTPM (GTFS Santiago, corte julio del año en curso) utilizados como benchmark y validación de esquemas.
* **Uso de la librería de Telegram, Folium, Osmnx, NetworkX, Pandas, SQLALSCHMI, Math, REREQUEST, DATACLASSES, GEOPY, HASHLIB, Login, SQLITE3 y 5PSYCOPG2 

---

## 💼 Casos de Uso y Modelo de Impacto

### 🏛️ B2G (Licitaciones y Gobiernos Regionales / MTT)
* **Dolor:** Equipar flotas completas con hardware GPS propietario implica costos millonarios en adquisición y mantención para las regiones.
* **Solución:** Telemetría comunitaria y feeds GTFS certificados sin inversión en hardware, habilitados en semanas.

### 🗺️ B2B / Partners de Movilidad (Google Transit / Plataformas de Mapas)
* **Dolor:** Vacíos cartográficos y falta de datos en tiempo real en ciudades intermedias y periferias.
* **Solución:** Provisión de feeds validados de última milla listos para integración directa.

---

## 🔄 Política de Liberación de Datos

* **Cadencia de Publicación:** Actualizaciones y liberaciones trimestrales (**cada 3 meses**) de datasets consolidados en formato GTFS abierto para la comunidad e investigadores.
* **Tiempo Real:** Canales dinámicos accesibles para endpoints autorizados.

## Declaración de uso de IA

* **Uso de IA para la elaboración del código y del README, se empleó Cloud, Gemine y ChatGPT.

---

## 📄 Licencia

Este proyecto está liberado bajo la licencia **GNU Affero General Public License v3.0 (AGPLv3)** para proteger la integridad del código fuente en entornos de red y servicios en la nube.

