# Construct-X Ontologies

Das Construct-X Ontologie-Paket: 10 Domänen-Ontologien, 8 Core-Ontologien (übergeordnete Konzepte), 10 Link-Ontologien, 31 SKOS-Vokabulare und 1 externe Extension (Stand `MANIFEST.json`), jeweils mit SHACL-Profilen und Beispieldaten.

Starten mit:

- `MANIFEST.json` — Modul-Register mit Versionen
- `VALIDATION.md` / `AUDIT.md` — Validierungsstatus
- `documentation/ONTOLOGY-LINKING-RULE.md` — Architekturregeln für Link-Ontologien
- `documentation/CONSTRUCT-X-ONTOLOGIES.html` — interaktive Übersicht (nur Ontologien; cxcp in Sektion 7 „Construction Progress")
- `documentation/ICDD-EXAMPLES.md` — ICDD-Beispiele, eigenständige Doku (getrennt von der Ontologie-Übersicht)
- `usecase/` — Anwendungszenario und Komponentenüberblick
- `examples/construct-x-doppelboden-beispieldaten/` — durchgängiges Beispiel inkl. Exchange-Package-Dokumentation (u. a. §6.1 „Plain JSON v2 / Envelope")
- `extensions/construct-x-construction-progress/` — Baufortschritt-Extension auf Basis der IoC Process Ontology (externes IRI-Schema `w3id.org/construct-x/construction-progress#`)
- `examples/construct-x-baufortschritt-beispiel/` — End-to-End-Beispiel: Lieferung → Transport → Einbau bis zum BIM-Konstruktionselement
- `examples/construct-x-icdd-beispiele/` — zwei ICDD-Container (ISO 21597) als Beispiel für die Liefer-/Verknüpfungsschicht

## Modules (as of 2026-11-11)

| Module                          | Type            | Version |
|---------------------------------|-----------------|---------|
| `construction-contract`         | Domain ontology | 0.1.0 (draft) |
| `construction-project`          | Domain ontology | 0.1.0 (draft) |
| `construction-schedule`         | Domain ontology | 0.5.0   |
| `breakdown-structure`           | Domain ontology | 0.7.0   |
| `gaeb-boq`                      | Domain ontology | 0.5.0   |
| `construction-progress-report`  | Domain ontology | 0.1.0   |
| `construction-site`             | Domain ontology | 0.2.0   |
| `construction-delivery`         | Domain ontology | 0.1.0   |
| `built-asset`                   | Domain ontology | 0.1.0   |
| `notification-content`          | Domain ontology | 0.1.1   |
| `agent` (`core-ontologies/`)    | Core ontology   | 0.1.0   |
| `person`                        | Core ontology   | 0.1.0   |
| `organization`                  | Core ontology   | 0.1.0   |
| `address`                       | Core ontology   | 0.1.0   |
| `participation`                 | Core ontology   | 0.2.0   |
| `contact`                       | Core ontology   | 0.1.0   |
| `document`                      | Core ontology   | 0.1.0   |
| `vso`                           | Core ontology   | 0.1.0   |
| `schedule-breakdown-link`       | Link ontology   | 0.6.0   |
| `schedule-boq-link`             | Link ontology   | 0.2.1   |
| `schedule-progress-report-link` | Link ontology   | 0.1.0   |
| `site-breakdown-link`           | Link ontology   | 0.1.0   |
| `delivery-site-link`            | Link ontology   | 0.1.0   |
| `delivery-boq-link`             | Link ontology   | 0.1.0   |
| `schedule-delivery-link`        | Link ontology   | 0.1.0   |
| `schedule-site-link`            | Link ontology   | 0.1.0   |
| `built-asset-breakdown-link`    | Link ontology   | 0.1.0   |
| `site-built-asset-link`         | Link ontology   | 0.1.0   |
| `construct-x-construction-progress` | Extension     | 0.1.0   |

> `construct-x-construction-progress` ist eine **Extension** (keine der 10 Domänen): eine schlanke Erweiterung der externen IoC Process Ontology (`w3id.org/ioc`) und von BOT (`w3id.org/bot`) mit eigenem IRI-Schema (`w3id.org/construct-x/construction-progress#`). Deshalb eigener `extensions/`-Ordner und eigene `MANIFEST.json`-Sektion — die Linking Rule (Querrelationen nur in Link-Ontologien zwischen Construct-X-Domänen) greift nicht.

> Die **Core-Ontologien** (`core-ontologies/`, Stand 2026-11-14) sind die „übergeordneten Konzepte" des Construct-X-Ontologienetzwerks (Confluence: Status Ontologieentwicklung, „Übergeordnete Konzepte"): Agent (gemeinsame Oberklasse für alle Akteure, ⊑ foaf:Agent), Person, Organization (inkl. LegalEntity, Membership, LegalRepresentation), Address, Participation, Contact, Document und Value Semantics (QUDT/OPM). Sie sind **keine Domänen-Ontologien** — die Linking Rule greift nicht — und werden von den Domänen direkt als Range referenziert (Präzedenz: `skos:Concept` in allen Vokabular-Properties, GeoSPARQL in Built Asset/Site). Seit 2026-11-14 haben `ContractParty.member` und `ProjectParticipation.member` den Range `conx-agent:Agent`; die Beispiele typisieren die Instanzen als `conx-org:LegalEntity`, die ARGE als `conx-org:Organization` mit drei `conx-org:Membership`. SHACL prüft bewusst `sh:nodeKind sh:IRI` ohne `sh:class` (pySHACL mit `infer='none'` wendet Subklassen-Ergebnisse nicht an).

The Construction Site and Construction Delivery modules (plus their four link ontologies and six SKOS vocabularies) were added on 22 Oct 2026 from the working document "Ontologien & Standards für Baustellen".

On 22 Oct 2026 the Construction Site module was advanced to 0.2.0 to support **time-varying area allocation (Flächenbelegung)**: a new `AreaAllocation` class, the `area-allocation-status` SKOS vocabulary, a dedicated SHACL profile (with an overlap-conflict rule) and the `schedule-site-link` link ontology. The Built Asset domain (0.1.0) and the `site-built-asset-link` link ontology were added in the same revision.

On 30 Oct 2026 the `built-asset-breakdown-link` ontology (0.1.0, added to the package together with the Built Asset domain) was registered in `MANIFEST.json` and re-verified end-to-end (RDF parse, isomorphic RDF/XML mirror, SHACL against `built-asset-links-example.ttl` and the integrated link example, linking-rule architecture checks).

On 4 Nov 2026 the `notification-content` module (0.1.1, on disk since the exchange-package work and already referenced by the Converters' CURIE register and the doppelboden example notification) was registered in `MANIFEST.json`, gained RDF/XML mirrors for all five TTL files and the example data file `notification-content-example.ttl`; the full package was re-verified (SHACL 10/10 runs conform, 0 violations).

On 4 Nov 2026 the combined JSON-LD context `contexts/construct-x-context.jsonld` (0.1.0, `@version: 1.1`, context IRI `https://www.construct-x.org/context/construct-x/0.1.0`) was added. It covers all 8 domain ontologies, all 10 link ontologies and all 21 SKOS vocabularies in a single file (371 `@context` entries). Bare term names that collide across modules are mapped to exactly one bare term entry and remain usable via their module prefix. The context is registered in `MANIFEST.json` under `json_ld_context` and verified end-to-end by the self-contained Jena 4.10.0 project `contexts/validation/` (PASS on 2026-11-04: test document expands to 42 triples / 64 IRIs, roundtrip 42 → 42).

On 5 Nov 2026 the shared **Construct-X SDK** was extracted from the converter builds into the new `construct-x-sdk/` module of the `construct-x-converters` repository (`org.construct-x:construct-x-sdk:0.1.0-SNAPSHOT`, Java 25 / Jena 4.10.0, no Spring) as "Ebene 1" of the use-case architecture. It de-duplicates `ConxCurieRegister`, `RdfInput`, `PlainJsonModelWriter` and the base `ConxNamespaces`, and adds the shared helpers `IriFactory`, `OntologyRegistry`, `ShaclValidatorHelper` and `ProvenanceHelper` (PROV-O annotations). The SDK is registered in `MANIFEST.json` under `sdk`; all four builds re-verified on 2026-11-05 (SDK 81/81, GAEB 32/32, MS-Project 33/33, RDF 15/15 — 161/161 tests, BUILD SUCCESS).

On 6 Nov 2026 the **Construction Progress Extension** `cxcp` (0.1.0) was integrated under `extensions/construct-x-construction-progress/` and registered in `MANIFEST.json` (new `extensions` section, 41 entries). The combined JSON-LD context was extended with the `cxcp` prefix + 8 terms (380 `@context` entries; `@version` stays 1.1 due to a Jena 4.10.0 loader quirk) and re-verified (PASS: 48 triples / 77 IRIs, roundtrip 48 → 48). The end-to-end Baufortschritt example (`examples/construct-x-baufortschritt-beispiel/`) and two ICDD container examples (`examples/construct-x-icdd-beispiele/`, ISO 21597) were added; the Doppelboden container's embedded notification-content ontology was synced to 0.1.1. Full package re-verified: 86 TTL + 39 RDF/XML parsed, SHACL 11/11 conform (incl. a new cxcp run with `sh:sparql` constraint + negative test), all ICDD payload checksums OK. On the same day the HTML documentation was restructured per user feedback (nothing published yet; no fachliche changes): `cxcp` is now described in exactly one place — section 7 of `CONSTRUCT-X-ONTOLOGIES.html`, renamed "Construction Progress" and covering CPR + cxcp as one cohesive concept — the former section 19 (cxcp + ICDD) was removed, and ICDD now lives in the separate `documentation/ICDD-EXAMPLES.md` (main doc = ontologies only, 18 sections).

On 11 Nov 2026 the **Construction Contract** draft module `construction-contract/` (0.1.0, not yet published) was added per the Confluence working document x_Idee_Vertragsontologie (3.4.7): domain ontology (4 classes `Contract`/`ContractParty`/`ContractItem`/`Obligation`, prefix `conx-con` — deliberately trimmed from ~15–20 classes to answer the document's 9 core questions), four SKOS vocabularies (`conx-ct`, `conx-crt`, `conx-cst`, `conx-cpm`), Core + Vocabularies SHACL profiles, Brücke-XY example and five triple-isomorphic RDF/XML mirrors. Deferred to 0.2.0: clause hierarchy, compensation breakdown, contract documents/changes. No cross-domain ObjectProperties (future `project-contract-link` per the Linking Rule). Validated 2026-11-11 (SHACL conform, 4 negative tests violated). The same day an all-ontology review corrected five vocabulary references in the `construction-project` draft (`DatatypeProperty` → `ObjectProperty`, package-wide convention); no other module needed slimming. On 14 Nov 2026 the contract module was switched to the **single-contract view** per project direction: contracts are modeled in isolation; the contract chain (main/sub-contracts) is aggregated at project level (future `project-contract-link`), so `subcontractOf`/`hasUpstreamContract` were removed from the ontology and Core SHACL profile (example shows the three Brücke-XY contracts without chain edges); the ARGE/joint-venture special case stays one untyped IRI per `ContractParty.member` (functional) — its composition belongs to the planned core organization/agent ontology. Later the same day the **core ontologies** (the "Übergeordnete Konzepte" of the Construct-X ontology network — Confluence status page) were added to the package under `core-ontologies/`: `agent` 0.1.0 (common superclass for all actors, subclass of `foaf:Agent`), `person` 0.1.0, `organization` 0.1.0 (incl. `LegalEntity`, `Membership`, `LegalRepresentation`), `address` 0.1.0, `participation` 0.2.0, `contact` 0.1.0, `document` 0.1.0, `vso` 0.1.0 (value semantics via QUDT/OPM). They are core/network concepts, not domain ontologies, so the Linking Rule does not apply and the domain ontologies reference them directly as ranges (precedent: `skos:Concept` everywhere, GeoSPARQL in built-asset/site). `ContractParty.member` and `ProjectParticipation.member` now carry `rdfs:range conx-agent:Agent`; both draft examples type their organization instances as `conx-org:LegalEntity`, and the ARGE as a `conx-org:Organization` with three `conx-org:Membership` (Porr/Strabag/Züblin). SHACL profiles stay `sh:nodeKind sh:IRI` without `sh:class` (pySHACL with `infer='none'` does not apply subclass results, so a `sh:class conx-agent:Agent` would reject merely `LegalEntity`-typed nodes). Registered in `MANIFEST.json` (new `core_ontologies` section, 54 → 62 entries); full package re-verified: 112 TTL + 51 RDF/XML parse-clean, 51 isomorphic pairs, SHACL 15/15 conform, 10 negative tests violated, 62 manifest entries / 0 version mismatches. Same day: eight triple-isomorphic RDF/XML mirrors were added for the core ontologies (51 → 59 TTL/RDF/XML pairs) and the draft examples were enriched with core address/contact data — structured `conx-addr:Address`/`AddressAssignment` per reference organization (linked via the deliberately domain-free `conx-addr:hasAddressAssignment`) and `conx-contact:ContactPoint`s (via domain-free `conx-contact:hasContactPoint`) — no schema or SHACL change; re-verified: 112 TTL + 59 RDF/XML parse-clean, 59 isomorphic pairs, SHACL 15/15 conform, 10 negative tests violated, 62 manifest entries / 0 version mismatches.

On 11 Nov 2026 the **Construction Project** draft module `construction-project/` (0.1.0, not yet published) was added per the Confluence working documents (3.4.7 Scope 728301589, Arbeitsdokument "Project" 934248456): domain ontology (4 classes `Project`/`ProjectPhase`/`ProjectParticipation`/`ProjectDeliverable`, prefix `conx-proj`), six SKOS vocabularies (`conx-pt`, `conx-pht`, `conx-phs`, `conx-ps`, `conx-si`, `conx-por`), Core + Vocabularies SHACL profiles (incl. 3 `sh:sparql` date-order constraints), example data, and seven triple-isomorphic RDF/XML mirrors. No cross-domain ObjectProperties (future `project-*-link` link ontologies per the Linking Rule); `member` is an untyped IRI reference pending the planned core organization/agent ontology. Validated 2026-11-11: module SHACL runs conform, 4 negative tests correctly violated. The same re-diagnosis corrected the old SHACL "0 shapes" environment note: it was a wrong `shapes_graph=` keyword (correct: `shacl_graph=`), no pySHACL/rdflib version bug — the repository `.venv` works (see VALIDATION.md notes 18, 30–32).

## Related repository: Construct-X Converters

Die Konverter-Dienste (GAEB BoQ, MS Project, RDF) mit ihren Web-Frontends und Docker-Compose-Setups sind im separaten Repository **`construct-x-converters`** (Java 25 / Spring Boot 3.5 / Apache Jena 4.10). Dort auch die vollständige Spezifikation des Plain-JSON-Formats v2 und der Exchange-Package-Envelope; die Beispiel-Daten in `examples/` folgen derselben Konvention.

## Use Case (as of 2026-10-27)

`usecase/` documents an end-to-end scenario (general contractor → subcontractor → logistics provider) showing how the ontologies enable cross-organisation data exchange, plus a component overview in three layers (shared Construct-X components incl. an SDK, reusable converter services, company-specific integration services). See `usecase/index.html` for the interactive version.
