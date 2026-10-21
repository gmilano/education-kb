# @nor-data/udir-mcp

MCP-server som wrapper UDIRs åpne registre — bygget for Nabodata-kartleggingen (#4: skoler/barnehager).

- **NSR** (Nasjonalt skoleregister): `https://data-nsr.udir.no/v3`
- **NBR** (Nasjonalt barnehageregister): `https://data-nbr.udir.no/v3`

Begge er åpne, auth-frie REST-API-er.

## Verktøy

| Verktøy | Beskrivelse |
|---|---|
| `sok_skole` | Skoler per kommune (4-sifret kommunenr, normaliserer ledende null). Filter: navn-delstreng, type (grunnskole/videregaaende/privat/offentlig/spesialskole), inkluder_inaktive |
| `hent_skole` | Full detalj per orgnr: adresse, **koordinater (lat/lon, GeoNorge)**, **elevtall**, ansatte-intervall, målform, kontakt |
| `sok_barnehage` | Barnehager per kommune. Filter: navn, eierform (privat/offentlig), inkluder_inaktive |
| `hent_barnehage` | Full detalj per orgnr: adresse, koordinater, eierform, kategorier |

## Datakvalitets-merknader (verifisert 6. juni 2026)

- UDIR leverer `{Lengdegrad:0, Breddegrad:0, GeoKilde:"Undefined"}` for ikke-geokodede enheter — serveren behandler dette som **manglende koordinat** (utelater feltet).
- `Navn`-queryparam på `/v3/enheter` ignoreres av UDIR — navnefilter gjøres derfor klientside per kommune.
- Registrene inneholder test-enheter (orgnr `U999…`, kommune 2599) — filtreres implisitt bort ved kommune-søk.

## Bygg & test

```bash
npm install && npm run build
npm test   # E2E med ekte UDIR-kall (11 sjekker)
```

## Nabodata-bruk

`sok_grunnkrets` (kartverket) → kommunenr → `sok_skole`/`sok_barnehage` → `hent_*` for koordinater → avstandsberegning klientside. Fremtidig fase B: `skoler_naer_punkt` med batch-detaljhenting og haversine-radius.
