# Construct-X Integrated Validation Report

**Date:** 2026-11-06 (Construction Progress Extension `cxcp` + Baufortschritt example + ICDD container examples integration, full package re-verification) / 2026-11-05 (Construct-X SDK extraction, converter re-verification) / 2026-11-04 (notification-content integration, full package re-verification, JSON-LD context + Jena verification) / 2026-10-30 (package re-verification) / 2026-10-28 (converter re-verification) / 2026-10-22 (ontology package)  
**Status:** PASS

## Scope

Checked the integrated draft package containing:
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
- associated SKOS vocabularies and SHACL profiles
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

- Turtle files parsed: 86 (83 + 3 cxcp module files: ontology, shapes, example)
- RDF/XML files parsed: 39
- Turtle parse errors: none
- RDF/XML parse errors: none
- SHACL (2026-11-06 re-run, pySHACL 0.28.1 / rdflib 6.3.2 via dedicated venv, no OWL inference; 11/11 runs conform, 0 violations each):
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
- SHACL note: SKOS vocabularies are loaded into the data graph for the `sh:class skos:Concept` / `sh:in` checks
- Architecture issues: none
- Namespace/prefix issues: none (prefix collision `conx-sbl` resolved, see Notes)
- Manifest entries: 41 (8 domain + 10 link + 21 vocabulary ontologies + 1 extension); every declared namespace is registered and every manifest entry is present in the package; MANIFEST ↔ in-file `versionInfo` consistent (checked incl. the new `extensions` section; the cxcp ontology carries `owl:versionInfo "0.1.0"` + `owl:versionIRI <…/construction-progress/0.1.0>`)
- TTL/RDF/XML pairs: 39, all triple-isomorphic (checked with `rdflib.isomorphic`)
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
- Single combined context covering all 8 domain ontologies, all 10 link ontologies, all 21 SKOS vocabularies and — since 2026-11-06 — the Construction Progress Extension `cxcp` (prefix `cxcp` → `https://w3id.org/construct-x/construction-progress#` + 8 bare terms: `TransportProcess`, `InstallationProcess`, `ProgressEvidence`, `hasExecutionSpace`, `hasExecutionSpaceValue`, `hasProgressEvidence`, `hasProgressEvidenceValue` and `ifcGlobalId`).
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
18. **Environment note:** the 2026-11-04 SHACL runs used a dedicated Python venv (rdflib 6.3.2 + pySHACL 0.28.1) because the system-wide rdflib 7.6.0 silently finds 0 shapes in pySHACL 0.40.1 (validated: minimal counterexample correctly rejected only in the venv).

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
