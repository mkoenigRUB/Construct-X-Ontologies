# Construct-X Integrated Validation Report

**Date:** 2026-11-14 (8 core-ontologies RDF/XML mirrors + draft examples enriched with core address/contact data, full package re-verification) / 2026-11-14 (core ontologies adopted into the package as `core-ontologies/`, `member` ranges typed to `conx-agent:Agent`, full package re-verification) / 2026-11-14 (Construction Contract 0.1.0: single-contract view — `subcontractOf`/`hasUpstreamContract` removed, ARGE = 1 IRI per party, full package re-verification) / 2026-11-11 (Construction Project 0.1.0 + Construction Contract 0.1.0 draft modules added, project vocab-property type correction, full package re-verification, SHACL environment note corrected) / 2026-11-06 (Construction Progress Extension `cxcp` + Baufortschritt example + ICDD container examples integration, full package re-verification) / 2026-11-05 (Construct-X SDK extraction, converter re-verification) / 2026-11-04 (notification-content integration, full package re-verification, JSON-LD context + Jena verification) / 2026-10-30 (package re-verification) / 2026-10-28 (converter re-verification) / 2026-10-22 (ontology package)  
**Status:** PASS

## Scope

Checked the integrated draft package containing:
- Construction Project 0.1.0 (draft, `construction-project/`, 2026-11-11: domain ontology, 6 SKOS vocabularies, 2 SHACL profiles, example, 7 RDF/XML mirrors)
- Construction Contract 0.1.0 (draft, `construction-contract/`, 2026-11-11: domain ontology, 4 SKOS vocabularies, 2 SHACL profiles, example, 5 RDF/XML mirrors)
- Construction Schedule 0.5.0
- Breakdown Structure 0.7.0
- GAEB BoQ 0.5.0
- Construction Progress Report 0.1.0
- Construction Site 0.2.0
- Construction Delivery 0.1.0
- Built Asset 0.1.0
- Notification Content 0.1.1
- Schedule–Breakdown Link 0.6.0
- Schedule–BoQ Link 0.2.1
- Schedule–Progress Report Link 0.1.0
- Site–Breakdown Link 0.1.0
- Delivery–Site Link 0.1.0
- Delivery–BoQ Link 0.1.0
- Schedule–Delivery Link 0.1.0
- Schedule–Site Link 0.1.0
- Site–Built Asset Link 0.1.0
- Built Asset–Breakdown Link 0.1.0
- associated SKOS vocabularies and SHACL profiles (incl. the six Construction Project vocabularies)
- SKOS mapping example package (`construct-x-skos-mapping-example/`, 5 TTL files,
  parse-checked; documents the recommended pattern for external vocabulary alignment)
- Construction Progress Extension `cxcp` 0.1.0 (`extensions/construct-x-construction-progress/`,
  external IoC/BOT-based extension, 1 ontology + 1 SHACL profile + example, 8 context terms)
- Baufortschritt end-to-end example (`examples/construct-x-baufortschritt-beispiel/`,
  3 Plain-JSON data revisions + 3 Tractus-X notifications + result)
- ICDD container examples (`examples/construct-x-icdd-beispiele/`, 2 ISO 21597 containers:
  Baufortschritt + Doppelboden, each Index.rdf + links.rdf + checksummed payload documents)
- GAEB converter (in the separate `Construct-X-Converters` repo, `Converter/`, Java 17 / Maven, Jena 4.10, Spring Boot 3.2.5)
- Construct-X SDK (in the `Construct-X-Converters` repo, `construct-x-sdk/`, 0.1.0-SNAPSHOT, Java 25 / Maven, Jena 4.10.0, no Spring): shared `ConxCurieRegister`, `IriFactory`, `OntologyRegistry`, `ShaclValidatorHelper`, `ProvenanceHelper`, `RdfInput`, `PlainJsonModelWriter`, base `ConxNamespaces`
- JSON-LD context (`contexts/construct-x-context.jsonld`, 0.1.0) with its self-contained Jena verification project (`contexts/validation/`, Java 25 / Maven 3.9.9, Jena 4.10.0)

## Construction Schedule document conformance

- Required documented terms missing: none
- Obsolete terms remaining in Schedule core: none
- `hierarchyCode` added to `Activity`.
- `description` added to `Activity`.
- Milestone constraint `plannedStart = plannedFinish` is represented in Core SHACL.
- Schedule vocabulary namespaces are aligned to `/vocab/construction-schedule/...`.

## Package validation

- Turtle files parsed: 112 (86 + 10 Construction Project files + 8 Construction Contract files + 8 core ontologies, `core-ontologies/`)
- RDF/XML files parsed: 59 (39 + 7 Construction Project + 5 Construction Contract + 8 core-ontologies mirrors)
- Turtle parse errors: none
- RDF/XML parse errors: none
- SHACL (no OWL inference; 2026-11-12 re-run with corrected `shacl_graph=` keyword, after the notification-content SPARQL fix, see Notes item 36; 15/15 runs conform, 0 violations each):
  - Construction Schedule example vs. all 4 profiles (Core, Schedule-Type, Activity-Status, Precedence-Relationship-Type)
  - Breakdown Structure example vs. Core + Node-Types profiles
  - GAEB BoQ example vs. Core + Price-Component-Type profiles
  - Construction Progress Report example vs. Core + Activity-Status profiles
  - Construction Site example vs. Core + Vocabulary + Site-Logistics + Area-Allocation profiles
  - Construction Delivery example vs. Core + Vocabulary profiles
  - Built Asset example vs. Core + Vocabulary profiles
  - integrated Link example vs. all ten link SHACL profiles
  - Built Asset Links example (`built-asset-links-example.ttl`) vs. Site–Built Asset + Built Asset–Breakdown link profiles
  - Notification Content example vs. Core profile (negative test: `TaskRequested` without `taskType`/Target correctly violated)
  - Construction Progress Extension example (`extensions/construct-x-construction-progress/examples/construction-progress-example.ttl`) vs. cxcp SHACL profile (run with `advanced=True`, the profile carries a `sh:sparql`/`sh:select` constraint: a TransportProcess must keep at least one element as both input and output; negative test: a TransportProcess whose input and output element differ correctly violated that SPARQL constraint)
  - Construction Project example vs. Core SHACL profile (38 property constraints across the 4 target classes + 3 `sh:sparql` date-order constraints — 2 on `Project`, 1 on `ProjectPhase`, `advanced=True`)
  - Construction Project example vs. Vocabularies SHACL profile (6 `sh:in` vocabulary checks; SKOS vocabularies loaded into the data graph)
  - Construction Contract example vs. Core SHACL profile (34 property constraints across the 4 target classes + 2 `sh:sparql` date-order constraints, `advanced=True`)
  - Construction Contract example vs. Vocabularies SHACL profile (4 `sh:in` vocabulary checks: contract type 9, contractual role 9, subject type 9, pricing model 4; SKOS vocabularies loaded into the data graph)
  - Negative tests (all correctly violated): `identifier` missing on `Project` (minCount 1); `progress` = 150 (maxInclusive 100); `plannedStart` > `plannedEnd` (`sh:sparql` constraint); `phaseType` from a foreign vocabulary (`sh:in`); `identifier` missing on `Contract`; `validFrom` > `validUntil` (`sh:sparql` constraint); `contractType` missing (minCount 1); `subjectType` from a foreign vocabulary (`sh:in`)
- SHACL note: SKOS vocabularies are loaded into the data graph for the `sh:class skos:Concept` / `sh:in` checks
- Architecture issues: none
- Namespace/prefix issues: none (prefix collision `conx-sbl` resolved, see Notes)
- Manifest entries: 62 (10 domain + 8 core + 10 link + 31 vocabulary ontologies + 1 extension + 1 JSON-LD context + 1 SDK); every declared namespace is registered and every manifest entry is present in the package; MANIFEST ↔ in-file `versionInfo` consistent (checked incl. the new `project_vocabularies`, `contract_vocabularies` and `core_ontologies` sections; the cxcp ontology carries `owl:versionInfo "0.1.0"` + `owl:versionIRI <…/construction-progress/0.1.0>`)
- TTL/RDF/XML pairs: 59, all triple-isomorphic (checked with `rdflib.isomorphic`)
- Construct-X SDK + converter re-verification (2026-11-05, after SDK extraction, Maven 3.9.9, JDK 25, Jena 4.10.0): all builds BUILD SUCCESS
  - `construct-x-sdk`: 81/81 tests (ConxCurieRegisterTest 27, IriFactoryTest 18, OntologyRegistryTest 10, PlainJsonModelWriterTest 13, RdfInputTest 9, ProvenanceHelperTest 4)
  - GAEB converter (`Converter/`): core 17/17 (GaebBoqConverterTest 8, GaebBoqReverseConverterTest 4, GaebBoqShaclValidationTest 2, GaebXmlValidatorTest 3) + web 15/15 (ConverterApiTest)
  - MS-Project converter (`msproject-converter-service`): 33/33 (MsProjectApiTest 17, MsProjectConverterTest 9, MsProjectReverseConverterTest 7)
  - RDF converter (`rdf-converter-service`): 15/15 (RdfApiTest)
  - The duplicated unit tests (RdfInput, PlainJsonModelWriter) were removed from the three converter builds and now run once in the SDK; per-build totals dropped accordingly (104 → 80 converter tests + 81 SDK tests)

## Architecture

- Domain ontologies do not import other Construct-X domain ontologies.
- Cross-domain relations are defined only in dedicated link ontologies.
- Link ontologies import exact source ontology versions.
- Schedule remains the primary integration axis for Breakdown, BoQ and Progress Report.
- Delivery is integrated through three dedicated link ontologies:
  - `schedule-delivery-link` (LogisticsRequirement ↔ Activity)
  - `delivery-site-link` (LogisticsOperation ↔ TransferPoint)
  - `delivery-boq-link` (LogisticsLoadItem ↔ QuantitySplit)
- Site is integrated with Breakdown through `site-breakdown-link` (SiteArea ↔ LBSNode).
- Site is integrated with Schedule through `schedule-site-link` (AreaAllocation ↔ Activity) for time-varying area allocation.
- Built Asset is integrated with Site through `site-built-asset-link` (SiteArea ↔ SpatialStructureElement).
- Built Asset is integrated with Breakdown Structure through `built-asset-breakdown-link` (SpatialStructureElement ↔ LBSNode, TechnicalSystem ↔ SBSNode, BuiltAsset/TechnicalSystem/Component ↔ CBSNode).
- No direct BoQ↔Breakdown, Progress↔Breakdown or Progress↔BoQ link ontology is introduced.

## JSON-LD context validation (2026-11-04, re-verified 2026-11-06 with cxcp)

- Context: `contexts/construct-x-context.jsonld` (0.1.0), context IRI `https://www.construct-x.org/context/construct-x/0.1.0`, `@version: 1.1`.
- Single combined context covering all domain ontologies (8 published + the 2026-11-11 `construction-project` and `construction-contract` drafts, which are **not yet** part of the context — to be added with the context bump), all 10 link ontologies, all 27 SKOS vocabularies and — since 2026-11-06 — the Construction Progress Extension `cxcp` (prefix `cxcp` → `https://w3id.org/construct-x/construction-progress#` + 8 bare terms: `TransportProcess`, `InstallationProcess`, `ProgressEvidence`, `hasExecutionSpace`, `hasExecutionSpaceValue`, `hasProgressEvidence`, `hasProgressEvidenceValue` and `ifcGlobalId`).
- 380 `@context` entries = 1 `@version` + 55 prefixes (15 standard, 8 domain, 10 link, 21 SKOS-vocabulary, 1 extension `cxcp`) + 208 bare term→IRI string mappings + 116 object definitions; 324 bare term keys in total, 0 prefixed string mappings. (Delta vs. 2026-11-04: +9 entries, all `cxcp`.)
- Verification: self-contained Jena 4.10.0 project `contexts/validation/` (Java 25 / Maven 3.9.9). `Main` expands the test document `test/test-doc.jsonld` (references the context via relative path `../../construct-x-context.jsonld`) against the context, asserts the 75 expected IRIs (one-way check: additional IRIs allowed; +11 `cxcp` IRIs for the new test node N11 `InstallationProcess`), and re-serializes the result.
- Result (2026-11-06): **PASS** — the test document expands to 48 triples / 77 IRIs, roundtrip 48 → 48, exit code 0.
- **Environment note (Jena `@version` quirk, 2026-11-06):** Jena 4.10.0's JSON-LD loader accepts the non-standard context field `@version` **only** with the value `1.1` (number or string); any other value (`1.2`, `1.0`, `2`, …) aborts with `LOADING_REMOTE_CONTEXT_FAILED`. The context therefore keeps `@version: 1.1` while gaining the `cxcp` terms; the versioned context IRI (`@id`, still `0.1.0`) remains the authoritative version marker.

Verification command (PowerShell, workdir `contexts/validation`; delete `target/` afterwards):

```powershell
$env:JAVA_HOME='<jdk25 install>'
& '<maven install>\bin\mvn.cmd' -q compile exec:java '-Dexec.args=test\test-doc.jsonld'
# -> ERGEBNIS: PASS, exit code 0
```

## ICDD container validation (2026-11-06)

- Containers: `examples/construct-x-icdd-beispiele/` — `construct-x-baufortschritt-beispiel.icdd` and `construct-x-doppelboden-feinterminplanung.icdd` (ISO 21597 containers, ZIP format; `Index.rdf` = container description + checksummed internal documents, `Payload triples/links.rdf` = linkset, `Ontology resources/` = embedded ontology copy).
- Integrity check per container: `Index.rdf` parsed as RDF/XML (Baufortschritt 111 triples, Doppelboden 49 triples); every `ct:InternalDocument` with a `ct:checksum` verified by recomputing SHA-256 over the `Payload documents/…` payload (Baufortschritt 8/8 OK, Doppelboden 3/3 OK); `links.rdf` parsed as RDF/XML (Baufortschritt 78 triples / 10 LinkElement / 5 DirectedBinaryLink, Doppelboden 34 triples / 4 LinkElement / 2 DirectedBinaryLink); embedded ontology parsed as TTL (Baufortschritt: `cxcp` 0.1.0, 58 triples; Doppelboden: notification-content 0.1.1, 90 triples).
- **Doppelboden container synced to the current ontology (2026-11-06, per project premise "nothing published, example may be adjusted"):** the embedded `Ontology resources/notification-content-ontology.ttl` was replaced from 0.1.0 to the repo's 0.1.1 (adds `contextResource`). The ontology copy is **not** a checksummed `ct:InternalDocument`, so no `Index.rdf` checksum needed to change; all three payload-document checksums re-verified OK afterwards. The `informationContainer` back-reference fields in the notifications are kept (they point to the container's own UUID — the intentional ICDD feature).
- The Baufortschritt container was already consistent (embedded `cxcp` ontology bit-identical to `extensions/…`, all payload checksums OK) and was left unchanged.

## Notes

This is a **draft package**. Version numbers have been kept where the corresponding ontology is still an unpublished draft; the Schedule–Breakdown link is advanced to 0.6.0 because WBS/LBS coverage was extended to SBS/CBS, and Schedule–BoQ is 0.2.1 because its exact GAEB BoQ import is 0.5.0.

Changes made during the 2026-10-22 review of the new Site/Delivery modules:

1. **Prefix collision fixed:** `site-breakdown-link` used the prefix `conx-sbl`, which is already the preferred prefix of `schedule-breakdown-link`. It is now `conx-sbdl` (TTL, SHACL, RDF/XML and the integrated example).
2. **Example data fixed:** `construction-site-example.ttl` — `ex:crane-01` and `ex:site-electricity-01` now carry the explicit `SiteInstallation` type required by the Core SHACL profile (`SiteEquipment`/`UtilitySupply` are subclasses, but the example is validated without OWL inference).
3. **Example data fixed:** `link-ontologies-example.ttl` — `ex:transfer-point-01` now carries the explicit `TransferPoint` type required by the Delivery–Site link SHACL profile.

Changes made during the 2026-10-22 implementation of time-varying area allocation (Flächenbelegung):

4. **Construction Site advanced to 0.2.0:** new `AreaAllocation` class with `allocatedArea`, `allocationType`, `allocationStatus`, `validFrom`, `validTo` and the inverse `hasAreaAllocation`. `SiteArea.hasAreaType` remains the standard (time-independent) type; time-varying usage is now modeled through `AreaAllocation` instances.
5. **New SKOS vocabulary:** `construction-site-area-allocation-status` (`conx-aas`) with `Planned`, `Actual`, `Released`.
6. **New SHACL profile:** `construction-site-shapes-area-allocation` enforces `validFrom <= validTo` and flags overlapping allocations of the same `SiteArea` (conflict rule).
7. **New link ontology:** `schedule-site-link` (`conx-ssl`) connects `AreaAllocation` ↔ `Activity` via `allocatedForActivity` / `requiresAreaAllocation`.
8. **Example data extended:** `construction-site-example.ttl` now contains two non-overlapping `AreaAllocation` instances for the same loading zone; `link-ontologies-example.ttl` links one allocation to an activity.
9. **Built Asset domain added:** `built-asset` 0.1.0 (domain ontology, 2 SKOS vocabularies, Core + Vocabulary SHACL profiles, example) and `site-built-asset-link` 0.1.0 are now part of the validated package.

Changes made during the 2026-10-30 review (manifest alignment):

10. **Manifest aligned:** `built-asset-breakdown-link` 0.1.0 (TTL + RDF/XML mirror + Core SHACL profile, on disk since the Built Asset revision of 2026-10-22) was registered in `MANIFEST.json`; the module is also referenced by the Confluence documentation and by `RdfApiTest` of the rdf-converter-service.
11. **Module re-verified:** all 11 files of the module parse cleanly; the RDF/XML mirror is isomorphic to the TTL (54 triples); imports are `built-asset/0.1.0` and `breakdown-structure/0.7.0` (exact released versions, no redefinitions); SHACL validation of `built-asset-links-example.ttl` and of the integrated link example: 0 violations.
12. **Example data fixed:** `breakdown-structure-example.ttl` — `ex:wbs-1` and `ex:wbs-1-1` now carry the `nodeType` values (`conx-de-wbs:Phase`, `conx-de-wbs:Subphase`) required by the Node-Types SHACL profile (`minCount 1`, `inVocabulary`).

Changes made during the 2026-10-30 re-verification (serialization completion):

13. **RDF/XML mirrors completed:** added the two missing mirrors `link-ontologies/schedule-site-link.owl` (27 triples) and `construction-site/construction-site-area-allocation-status.owl` (25 triples); the package now contains 34 in-scope RDF/XML files and all 34 TTL/RDF/XML pairs are triple-isomorphic.
14. **Stale comment fixed:** the `SiteArea` comments in `construction-site/construction-site.owl` (en/de) now match the TTL (stable spatial entity; `hasAreaType` as standard type; time-varying usage via AreaAllocations).

Changes made during the 2026-11-04 integration of notification-content:

15. **Module registered:** `notification-content` 0.1.1 + 4 SKOS vocabularies (all 0.1.0) added to `MANIFEST.json` (39 entries). The module was on disk since the exchange-package work, referenced by the Converters' `ConxCurieRegister` (prefixes `conx-nc/nt/sr/ts/tt`) and by the doppelboden example notification, but absent from manifest and validation scope.
16. **Serialization + example completed:** RDF/XML mirrors for all five module TTLs (isomorphic to their sources) and new `notification-content-example.ttl` (TaskRequested/DetailedScheduling mirroring the doppelboden reference, TaskStatusChanged/InProgress, ResultAvailable) — the module now follows the package-wide TTL/RDF/XML-pair convention (39 pairs total).
17. **Full package re-verified:** 83 TTL + 39 RDF/XML parsed without errors; SHACL 10/10 runs conform, 0 violations (10th run = notification example vs. Core profile, plus a negative test proving the SPARQL constraints are active); MANIFEST ↔ `versionInfo` consistent; no prefix collisions (40 registered prefixes).
18. **Environment note (corrected 2026-11-11):** the 2026-11-04 SHACL runs used a dedicated Python venv (rdflib 6.3.2 + pySHACL 0.28.1) because the repository `.venv` (pySHACL 0.40.1 / rdflib 7.6.0) reported "Found 0 SHACL Shapes" and returned vacuous "CONFORM". On 2026-11-11 the root cause was identified and the earlier diagnosis corrected: **no pySHACL/rdflib version bug exists.** The validator entrypoint is `validate(data_graph, *, shacl_graph=None, …)` — scripts that pass the shapes under the wrong keyword `shapes_graph=` silently drop the parameter into `**kwargs`, so pySHACL falls back to the data graph as shapes source and finds 0 shapes. Minimal counterexample (a `sh:targetNode` + `minCount 1` violation) is correctly rejected by **both** the repository `.venv` (0.40.1/7.6.0) and the dedicated venv (0.28.1/6.3.2) when the `shacl_graph=` keyword is used.

Changes made during the 2026-11-04 JSON-LD context work:

19. **Combined context + collision design:** the new context is a single file covering all 8 domain ontologies, all 10 link ontologies and all 21 SKOS vocabularies. Bare term names that collide across modules are intentionally mapped to exactly one bare term entry; colliding names are usable via their module prefix only (documented in the HTML documentation, section 18).
20. **Jena verification project:** `contexts/validation/` (`pom.xml`, `src/main/java/Main.java`, `test/test-doc.jsonld`, `test/test-doc-reference.md`) verifies the context end-to-end with Jena 4.10.0 — PASS on 2026-11-04 (42 triples / 64 IRIs expanded, roundtrip 42 → 42, exit code 0).
21. **Registration + documentation:** the context (0.1.0) is registered in `MANIFEST.json` under `json_ld_context`; README, this file and the HTML documentation (new section 18) were updated accordingly.

Changes made during the 2026-11-05 Construct-X SDK work (converter repo):

22. **SDK extracted:** the duplicated shared classes of the three converter builds (GAEB, MS-Project, RDF) were de-duplicated into the new module `construct-x-sdk/` of the `Construct-X-Converters` repo (`org.construct-x:construct-x-sdk:0.1.0-SNAPSHOT`, Java 25, Jena 4.10.0, Jackson 2.17.2, no Spring): `ConxCurieRegister` (×3 copies → 1, extended with `prefixFor()`/`namespaceFor()`), `RdfInput` (×2 → 1), `PlainJsonModelWriter` (×3 → 1), base `ConxNamespaces` (GAEB-specific term constants remain in the GAEB `core` module). New helpers: `IriFactory` (generalized), `OntologyRegistry` (manifest-driven ontology root resolution), `ShaclValidatorHelper`, `ProvenanceHelper` (PROV-O annotations).
23. **Integration + verification:** the SDK was added as a dependency of `Converter/core`, `msproject-converter-service` and `rdf-converter-service`; the 12 duplicated source files (incl. duplicated test classes) were deleted from the converter builds. Re-verification on 2026-11-05 (Maven 3.9.9, JDK 25): SDK 81/81, GAEB 17/17 + 15/15, MS-Project 33/33, RDF 15/15 — all BUILD SUCCESS.
24. **Environment note:** on machines where the hard-coded `byte-buddy-agent.jar` path in the MS-Project/RDF Poms does not resolve, the converter builds require `-Dbyte-buddy-agent.jar=<local path to byte-buddy-agent-1.14.13.jar>` on the Maven command line (Poms unchanged); the SDK build is unaffected.

Changes made during the 2026-11-06 integration of the Construction Progress Extension, the Baufortschritt example and the ICDD container examples:

25. **Extension registered:** `construct-x-construction-progress` 0.1.0 added to `MANIFEST.json` as the new `extensions` section (41 entries total; it is not one of the 8 domain ontologies — it is an external IoC/BOT-based extension with its own IRI scheme `https://w3id.org/construct-x/construction-progress#`). The delivered ontology was given the package-standard `owl:versionIRI <…/construction-progress/0.1.0>` (it previously only had `owl:versionInfo`) so the MANIFEST ↔ `versionInfo` consistency check passes like for all other modules.
26. **Full package re-verified (2026-11-06):** 86 TTL + 39 RDF/XML parsed without errors; SHACL 11/11 runs conform, 0 violations (new 11th run: cxcp example vs. cxcp profile with `advanced=True` for its `sh:sparql` constraint, plus a negative test proving that constraint is active); MANIFEST ↔ `versionInfo` consistent (41 entries); no prefix collisions.
27. **JSON-LD context extended with `cxcp`:** prefix `cxcp` + 8 bare terms added (371 → 380 `@context` entries); test document gained node N11 (`InstallationProcess`), `Main.java` now asserts 75 expected IRIs (was 64). Jena verification: PASS (48 triples / 77 IRIs expanded, roundtrip 48 → 48, exit code 0).
28. **ICDD containers added + Doppelboden synced:** two ISO 21597 example containers landed in `examples/construct-x-icdd-beispiele/`; the Doppelboden container's embedded notification-content ontology was upgraded 0.1.0 → 0.1.1 (repo-aligned; the ontology copy is not a checksummed document, so no `Index.rdf` change) and all payload checksums were re-verified. Baufortschritt container left unchanged (already consistent).
29. **Environment note:** Jena 4.10.0's JSON-LD loader accepts the non-standard context field `@version` only with the value `1.1`; the context therefore keeps `@version: 1.1` (the versioned `@id` IRI remains the version marker) — documented in the JSON-LD context validation section.

Changes made during the 2026-11-11 Construction Project 0.1.0 draft module work:

30. **Draft module added:** `construction-project/` 0.1.0 (first draft, not published): domain ontology `construction-project.ttl` (4 classes `Project`, `ProjectPhase`, `ProjectParticipation`, `ProjectDeliverable`; 15 object + 16 datatype properties; prefix `conx-proj`, all 7 module prefixes collision-checked against the 41 previously registered prefixes — 48 total, no collisions), six SKOS vocabularies (`conx-pt`, `conx-pht`, `conx-phs`, `conx-ps`, `conx-si`, `conx-por`), Core + Vocabularies SHACL profiles (per the package convention; the Vocabularies profile carries the six `sh:in` checks), and `construction-project-example.ttl`. No cross-domain ObjectProperties in the ontology itself — per the Linking Rule those belong to future `project-*-link` ontologies; `member` is an untyped IRI reference pending the planned core organization/agent ontology.
31. **Module validated (2026-11-11, repository `.venv` pySHACL 0.40.1 / rdflib 7.6.0 with the corrected `shacl_graph=` keyword; a dedicated temp venv 0.28.1/6.3.2 served as cross-check):** all 10 module TTL files parse (834 triples total); example conforms to the Core profile (38 property constraints + 3 `sh:sparql` date-order constraints) and to the Vocabularies profile (6 `sh:in` checks); four negative tests each correctly violate (missing `identifier`, `progress=150`, `plannedStart > plannedEnd`, `phaseType` from a foreign vocabulary). A minimal counterexample confirms shape detection is active in both environments.
32. **RDF/XML mirrors added:** seven triple-isomorphic `.owl` mirrors (ontology + six vocabularies), per the package convention (SHACL profiles and examples are TTL-only). Package totals updated: 96 TTL + 46 RDF/XML parsed, 46 isomorphic pairs, 49 manifest entries.

Changes made during the 2026-11-11 all-ontology review + Construction Contract 0.1.0 draft module work:

33. **Project draft correction (consistency):** a package-wide structural review (class/property count and property typing of all 10 domain modules) found that the `construction-project` draft declared five vocabulary references (`projectType`, `currentStatus`, `statusIndicator`, `phaseType`, `phaseStatus`) as `owl:DatatypeProperty` with `rdfs:range skos:Concept` — semantically invalid (a datatype property cannot take IRI values) and breaking the package-wide convention (all other modules use `owl:ObjectProperty` for vocabulary references: `nodeType`, `hasStatus`, `operationType`, `hasAreaType`, `allocationType`/`allocationStatus`, `hasPriceComponentType`, …). All five are now `owl:ObjectProperty, owl:FunctionalProperty` (ontology: 15 object + 16 datatype properties, 272 triples unchanged); OWL mirror re-serialized (isomorphic) and the module re-validated (SHACL Core + Vocabularies conform, negative tests still violated). The other modules passed the review: the blank-node "classes" in `breakdown-structure`/`gaeb-boq` are deliberate anonymous `owl:unionOf` domain expressions; `construction-site` (11 classes) and `gaeb-boq` (11 classes) are the heaviest modules but justified by their scope (area allocation/UTM, GAEB conformance) — no slimming action taken.
34. **Draft module added:** `construction-contract/` 0.1.0 (first draft, not published), deliberately trimmed from the ~15–20 classes of the working document (x_Idee_Vertragsontologie, Confluence 3.4.7 [1114210316]) to **4 classes** answering its 9 core questions: `Contract` (type, validity dates, value, pricing model, party/item/obligation references, `subcontractOf`/`hasUpstreamContract` — the contract hierarchy derived from contracts, not the org chart), `ContractParty` (`member` untyped IRI pending the core organization/agent ontology + `hasRole`), `ContractItem` (owed item with `subjectType`, quantity, unit, period) and `Obligation` (`obligatedParty`, `dueDate`). Four SKOS vocabularies from the document: contract-type (9 concepts, `conx-ct`), contractual-role (9, `conx-crt`), subject-type (9, `conx-cst`), pricing-model (4, `conx-cpm`) — all collision-checked against the 48 registered prefixes (53 total, no collisions). **Intentionally deferred to 0.2.0:** full `ContractualClause` hierarchy (Right/Prohibition/Permission/Condition), `Compensation` breakdown (retention, payment schedule), `ContractDocument`/`DocumentVersion`, `ContractChange`/amendments, typed `ContractSubject`→`ProjectDeliverable` reference (link ontology). No cross-domain ObjectProperties in the ontology (future `project-contract-link` per the Linking Rule). Core + Vocabularies SHACL profiles (36 property constraints + 2 `sh:sparql` date-order constraints) and a Brücke-XY example (contract chain DB→ARGE→Lindner→Zeppelin with sub-contracts, per the document's figure). Five triple-isomorphic RDF/XML mirrors. Module registered in `MANIFEST.json` (new `contract_vocabularies` section; 49 → 54 entries).
35. **Module validated (2026-11-11, repository `.venv` with the corrected `shacl_graph=` keyword):** all 8 module TTL files parse (680 triples total); example conforms to the Core profile and to the Vocabularies profile; four negative tests each correctly violate (missing `Contract.identifier`, `validFrom > validUntil`, missing `contractType`, `subjectType` from a foreign vocabulary). Full package re-verified: 104 TTL + 51 RDF/XML parsed without errors, 51 isomorphic pairs, 54 manifest entries, no prefix collisions.

Changes made during the 2026-11-12 documentation sync and SHACL fix:

36. **Dead SPARQL constraints fixed in the notification-content Core SHACL profile (2026-11-12, no version bump — still 0.1.1, same shape IRIs, no `MANIFEST.json` change):** the three `sh:sparql` count constraints in `notification-content/notification-content-shapes.ttl` referenced a SPARQL alias in `HAVING` (e.g. `… AS ?cnt … HAVING (?cnt != 1)`), which rdflib/pySHACL silently ignores, so the constraints were dead code (a `TaskRequested` without `taskType` was not rejected). Fixed to the aggregate form `HAVING (COUNT(?x) != 1)` with the alias removed from the SELECT. After the fix the negative test is correctly rejected and the full SHACL suite runs 15/15 conform, 0 violations (2026-11-12).
37. **Documentation synced (2026-11-12):** `documentation/CONSTRUCT-X-ONTOLOGIES.html` now documents both draft modules (sections 12/13 with T-Box, property tables, SHACL notes, vocab blocks and examples), carries 20 consistently numbered sections (nav, h2, all "Sektion N" cross-references), the corrected header counts (10 domain ontologies, 31 vocabularies, 104 Turtle files) and the updated Validierung section (status 2026-11-12, 104 TTL / 51 RDF/XML, 54 manifest entries). The JSON-LD context remains 0.1.0 and was deliberately not extended (the two drafts are added with the next context bump); the JSON-LD section body is unchanged apart from the h2 renumber.

Changes made during the 2026-11-14 single-contract view redesign of construction-contract:

38. **Contract module: single-contract view (2026-11-14, no version bump — still 0.1.0, no IRI/manifest change):** per project direction, contract chains are only assembled at project level; the contract domain models isolated contracts. `Contract.subcontractOf`/`Contract.hasUpstreamContract` removed from the ontology (TTL + isomorphic OWL) and the `subcontractOf` constraint removed from the Core SHACL profile; the Brücke-XY example now shows the three contracts (C01/C03/C04) without chain edges. ARGE/joint-venture special case: modeled as exactly one untyped IRI per `ContractParty.member` (functional, minCount/maxCount 1 unchanged); the JV composition belongs to the planned core organization/agent ontology. Re-verified 2026-11-14: 104 TTL + 51 RDF/XML parse-clean, 51 isomorphic pairs, SHACL 15/15 conform, 0 violations, 10 negative tests each violated, manifest 54 entries / 0 mismatches.

Changes made during the 2026-11-14 core ontologies adoption:

39. **Core ontologies adopted + `member` ranges typed (2026-11-14):** the eight core ontologies (the "Übergeordnete Konzepte" of the Construct-X ontology network — Confluence status page [1009549313]; author Sven Zentgraf (RUB), CC-BY-4.0; delivered in the repo `temp/` folder) were adopted into the package under `core-ontologies/`: `agent` 0.1.0, `person` 0.1.0, `organization` 0.1.0, `address` 0.1.0, `participation` 0.2.0, `contact` 0.1.0, `document` 0.1.0, `vso` 0.1.0. They are core/network concepts, not domain ontologies, so the Linking Rule does not apply and the domain ontologies reference them directly as ranges (precedent: `skos:Concept`, GeoSPARQL in built-asset/site). `ContractParty.member` and `ProjectParticipation.member` gained `rdfs:range conx-agent:Agent`; ontology descriptions/comments updated (en/de); both OWL mirrors re-serialized isomorphically (contract 236, project 273 triples). Examples type their organizations as `conx-org:LegalEntity`; the ARGE is a `conx-org:Organization` with three `conx-org:Membership` (Porr/Strabag/Züblin) — the single-contract-view decision (one IRI per member) is preserved. SHACL profiles keep `sh:nodeKind sh:IRI` **without** `sh:class` (pySHACL with `infer='none'` does not apply subclass results, so `sh:class conx-agent:Agent` would reject merely `LegalEntity`-typed nodes). No `owl:imports` (core not yet stably published). `MANIFEST.json` gained the `core_ontologies` section (54 → 62 entries) and `scripts/verify_manifest.py` the matching path rule. The JSON-LD context was deliberately not extended (next context bump). Re-verified 2026-11-14: 112 TTL + 51 RDF/XML parse-clean, 51 isomorphic pairs, SHACL 15/15 conform, 0 violations, 10 negative tests each violated, manifest 62 entries / 0 version mismatches, 80 construct-x prefix bindings, no new prefix collisions.

40. **Core ontologies: RDF/XML mirrors + example enrichment (2026-11-14, no version bump, no `MANIFEST.json` change):** (a) eight triple-isomorphic RDF/XML mirrors added for the core ontologies (`core-ontologies/*.owl`, per the package-wide TTL/RDF/XML-pair convention — SHACL profiles and examples remain TTL-only): 112 TTL + 59 RDF/XML parsed, 59 isomorphic pairs. (b) The two draft examples were enriched with data from the core address/contact ontologies — both properties are deliberately domain-free in the core ontologies and are therefore used here without any schema change: the contract example adds one `conx-addr:Address` + `conx-addr:AddressAssignment` per reference organization (DB, ARGE, Lindner, Zeppelin; linked via `conx-addr:hasAddressAssignment`) and two `conx-contact:ContactPoint`s (ARGE site management, DB project management) with `conx-contact:ContactMethod`s (E-Mail channel); the project example adds the site address (Campus, Gebäude V1) as an `AddressAssignment` with `attentionOf` on the project and one contact point (site management, phone) on the general contractor. SHACL profiles and negative tests are unaffected (15/15 conform, 10/10 violated). Re-verified 2026-11-14: 112 TTL + 59 RDF/XML parse-clean, 59 isomorphic pairs, SHACL 15/15 conform, manifest 62 entries / 0 version mismatches.

41. **Core ontologies domain audit (2026-11-14, read-only — no file changes, no version bump, no `MANIFEST.json` change):** structural + cross-reference audit of the eight adopted core ontologies against the whole package. Confirmed correct: reference direction strictly Domain → Core (0 core→domain references); all 8 carry `dcterms:license` = CC-BY 4.0 and `owl:versionIRI` + `owl:versionInfo` (participation 0.2.0, rest 0.1.0); core→core references coherent and cycle-free; the three inverse pairs (`subOrganizationOf`/`hasSubOrganization`, `unitOf`/`hasUnit`, `hasParticipation`/`context`) are each declared once — a single `a owl:inverseOf b` is semantically symmetric in OWL, so this is not a defect (the contact pair is redundantly declared twice, harmless); no functional properties (consistent with the "multiple assignments possible for matrix organizations" comments); domain-open properties are documented as intended broad anchoring. Findings (recommendation only, to raise with the core-ontology author — no change applied): (a) `rdfs:isDefinedBy` absent from all 8 core files (0) vs. full coverage in the domain ontologies (267+) — convention drift, documented not fixed (purely documentary, checked by no gate); (b) the publisher IRIs are externally-registered identities, not construct-x classes, defined nowhere in the repo: 25× `…/id/organization/construct-x` (domain files) and 8× `…/id/organization/ecbe8336-94ab-5c11-8220-94f260963eb2/revision/1` (core) — noted as references to an external identity registry, not dangling in-package terms; (c) `document`, `participation` and `vso` are not yet referenced by any domain or example file (only `address`, `contact`, `organization`, `agent` have live consumers) — intentional, they are the future anchor for the 0.2.0 ContractDocument / vso convergence links. Core OWL mirrors remain 59/59 isomorphic. See AUDIT.md item 67.

42. **Link ontologies: group audit + license fix (2026-11-15, no version bump):** group audit of the ten link ontologies. Confirmed correct: the Linking Rule is fully honored (0 cross-domain `rdfs:range` references and 0 domain→domain `owl:imports` in the domain ontologies); all 20 `owl:imports` point exactly at the current module versions per `MANIFEST.json` (0 drifts); all 10 carry `versionIRI` + `versionInfo` consistent with the manifest; `rdfs:isDefinedBy` fully covered (no core-ontology drift in the links); every inverse pair is semantically symmetric (unevenly-named pairs verified in the TTLs as genuine inverses with correct domain/range polarity); every link has a `-shapes-core.ttl` profile and a live example consumer. Finding + fix: 8 of the 10 link ontologies lacked `dcterms:license` — CC-BY 4.0 added to the 8 ontology headers (only `schedule-breakdown-link` and `schedule-progress-report-link` already carried it) and the 8 isomorphic `.owl` mirrors regenerated (+1 triple each). Re-verified 2026-11-15: 112 TTL + 59 RDF/XML parse-clean, 59 isomorphic pairs, SHACL 15/15 conform, 10/10 negative tests violated, manifest 62 entries / 0 version mismatches / 8 known naming-mismatches. See AUDIT.md item 68.
