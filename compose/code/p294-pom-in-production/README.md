---
industry: education
region: Global
updated: 2026-10-04
---

# `pom.xml` en el camino de PRODUCCIÓN — pase 97

```sh
python3 test_wiring.py            # 27/27, sin red
sh sweep_pom_production.sh        # el camino real, contra raw.githubusercontent.com
```

## Por qué existe

El pase 96 **diagnosticó** que el barrido manifiesto-consciente de esta base es ciego a
Java/Maven (tendencia **750**), **escribió el lector correcto** —
[`p289-maven-manifest/`](../p289-maven-manifest/), **11/11**, con su control negativo — y **no
lo conectó**. Medido en el pase 97, antes de tocar nada:

| Medición | Resultado |
|---|---|
| nombres en `PARSERS` de `p283/manifest_license.py` | **5** — 🔴 sin `pom.xml` |
| referencias a `maven_license.py` fuera de `p289/` | 🔴 **0** |
| suite de `p289` | 🟢 **11/11** — el lector era correcto |

🔵 **Un control que no está en el camino por donde pasan los datos no es un control: es una
demostración.** Eso es `P294`.

## El defecto que este cableado tuvo que esquivar

La identidad natural de un artefacto Maven *parece* ser el `artifactId`. Con eso como identidad
única, **2 de 6** repos Java del inventario salen `FOREIGN` **siendo propios**:

| Repo | `artifactId` | P280 con `artifactId` solo | realidad |
|---|---|---|---|
| `kuali/kc` | `coeus` | 🔴 `FOREIGN` | 🟢 propio — *Kuali **Coeus*** |
| `sakaiproject/sakai` | `base` | 🔴 `FOREIGN` | 🟢 propio — es su pom raíz |

🔴 **Y `FOREIGN` significa *no atribuir* (P280):** el cableado obvio habría leído bien la
`AGPL-3.0` de `kuali/kc` y se habría **negado a publicarla** — la licencia más consecuente del
inventario, porque §13 obliga a publicar el fuente a los usuarios de un servidor y un ERP
universitario se entrega como SaaS.

## Lo que hace el cableado

1. **No reimplementa el XML (`P237`).** Importa `declared_license_names` de `p289`, que
   conserva su suite como el control de la lectura. Una aserción afirma que el import resuelve
   a ese archivo, para que mover `p289` **falle en voz alta** en vez de dejar dos lectores
   divergentes.
2. **Resuelve la identidad con tres candidatos** —`groupId`, `artifactId`, `<name>`— y contra
   los **dos** segmentos del slug. El `groupId` es un namespace reverse-DNS que suele codificar
   a la organización (`org.kuali.coeus`), y `ownership()` descartaba el segmento de
   organización. **Gana el `groupId` en 5 de 6.**
3. **Ignora el `<parent>`.** `SafeExamBrowser/seb-server` hereda de
   `org.springframework.boot`: tomar esa identidad como propia es el error que P280 existe para
   impedir, y arrastraría una licencia ajena.
4. **No toca `ownership()`.** Sus 34 aserciones siguen valiendo y las 200 filas ya publicadas
   no se mueven: `ownership_any` es una capa **encima**, no un cambio de regla.
5. **No responde `P279`.** Un pom no nombra archivos de licencia, así que `license_files` es
   siempre `[]`. De esta capa sale la **declaración**, no el nombre del archivo.

## El resultado: dos canales independientes, y concuerdan

`sweep_pom_production.sh` corre el módulo de producción sobre los **payloads reales** y compara
contra lo que esta base ya publica (que viene del **otro** canal: el archivo de licencia).

| Repo | declara | familia | publicado | acuerdo |
|---|---|---|---|---|
| `kuali/kc` | `GNU Affero General Public License, Version 3` | `AGPL-3.0` | `AGPL-3.0` | 🟢 ACUERDO |
| `sakaiproject/sakai` | `Educational Community License, Version 2.0` | `ECL-2.0` | `ECL-2.0` | 🟢 ACUERDO |
| `UniTime/unitime` | `Apache Software License (ASL), Version 2.0` | `Apache-2.0` | `Apache-2.0` | 🟢 ACUERDO |
| `OpenOLAT/OpenOLAT` | `Apache 2.0 Open Source L6icense` | `Apache-2.0` | `Apache-2.0` | 🟢 ACUERDO |
| `DSpace/DSpace` | `DSpace BSD License` | `BSD` | `BSD-3-Clause` | 🔵 familia, menos preciso |
| `SafeExamBrowser/seb-server` | *(sin `<licenses>`)* | — | `MPL-2.0` | ⚠️ sin declaración |

🟢 **6 de 6 `OWN`, 4 acuerdos exactos, 0 contradicciones.** El manifiesto es un canal
**corroborante**: donde el archivo de licencia existe lo confirma; donde no existe
(`kuali/kc`), es la única fuente.

⚠️ **Límites declarados.** `DSpace BSD License` es un nombre de fantasía y de un nombre no sale
el número de cláusulas — `BSD-3-Clause` sólo lo da el payload. Y `OpenOLAT` declara
`Apache 2.0 Open Source L6icense`, con la errata **de upstream** (mismo `sha256` en dos
lecturas): no rompe el veredicto sólo porque el respaldo de `lib/license_family.sh` ancla en el
token de familia (`*apache*`) y no en la palabra «License» — un classificador por bloque de
título devuelve `UNCLASSIFIED` sobre esa cadena.

## El orden en `MANIFESTS`, y por qué queda sin ejercitar

`pom.xml` se agregó **al final**. El bucle corta en el primer manifiesto que parsea, así que el
orden sólo decide cuando hay **colisión** — y medido en los seis repos Java, `package.json` y
`composer.json` en la raíz dan **404 en 6/6**. 🔵 **La colisión no está observada y esta
elección queda sin ejercitar:** si aparece un repo poliglota, el orden pasa a ser una decisión
con consecuencia y hay que medirla, no heredarla de acá.

## Los negativos de la suite

| Control | Qué afirma |
|---|---|
| `fixtures/vendored-foreign.pom.xml` | un pom de un tercero vendorizado **sigue** `FOREIGN` y su GPL-2 **se lee pero no se atribuye** — P280 sigue cerrado |
| `fixtures/parent-identity.pom.xml` | el `<parent>` (`org.springframework.boot`) **no** presta identidad |
| `alfredang/ai-mms` vs `openmage/magento-lts` | el caso original de P280, en versión Maven: ni el segmento de organización crea propiedad falsa |
| `<settings>` y XML roto | no dan identidad ni revientan |
| pom vacío | devuelve `None`, no una fila fantasma |
