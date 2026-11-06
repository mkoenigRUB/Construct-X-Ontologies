# Construct-X Integrated Audit

## Changes made from the supplied Construction Schedule document

1. Added `Activity.hierarchyCode : xsd:string`.
2. Added `Activity.description : xsd:string`.
3. Rebuilt Construction Schedule Core SHACL against ontology 0.5.0.
4. Removed stale validation dependencies on `WorkLocation` and `hasPrecedenceRelationship`.
5. Aligned Schedule vocabulary namespaces to:
   - `/vocab/construction-schedule/schedule-type#`
   - `/vocab/construction-schedule/activity-status#`
   - `/vocab/construction-schedule/precedence-relationship-type#`
6. Updated Progress Report's optional Activity Status profile to the same shared Activity Status vocabulary.
7. Aligned Breakdown node-type vocabularies to the namespaces documented in the latest Breakdown documentation.
8. Completed Schedule–Breakdown linking for WBS, LBS, SBS and CBS.
9. Kept BoQ price modeling, including `unitPrice`, `totalAmount`, `UnitPriceComponent` and its SKOS vocabulary.
10. Regenerated RDF/XML serializations and performed package-wide RDF parse and architecture checks.

## Changes made during the 2026-10-22 review (new Site/Delivery modules)

11. Added Construction Site 0.1.0 (domain ontology, 4 SKOS vocabularies, 3 SHACL profiles, example).
12. Added Construction Delivery 0.1.0 (domain ontology, 2 SKOS vocabularies, 2 SHACL profiles, example).
13. Added four new link ontologies (all 0.1.0): `site-breakdown-link`, `delivery-site-link`, `delivery-boq-link`, `schedule-delivery-link`, each with a Core SHACL profile.
14. Fixed prefix collision: `site-breakdown-link` preferred prefix changed from `conx-sbl` to `conx-sbdl` (TTL, SHACL, RDF/XML, integrated example).
15. Fixed example data: explicit `SiteInstallation` type in the site example; explicit `TransferPoint` type in the integrated link example.
16. Extended `link-ontologies-example.ttl` with Site/Delivery instances.
17. Updated MANIFEST.json, VALIDATION.md, README.md and the Confluence/HTML documentation.

## Changes made during the 2026-10-22 implementation of time-varying area allocation (Flächenbelegung)

18. Advanced Construction Site to 0.2.0: added `AreaAllocation` class with `allocatedArea`, `allocationType`, `allocationStatus`, `validFrom`, `validTo` and inverse `hasAreaAllocation`; updated `SiteArea` comment to distinguish the standard type from time-varying allocations.
19. Added SKOS vocabulary `construction-site-area-allocation-status` (`conx-aas`): `Planned`, `Actual`, `Released`.
20. Added SHACL profile `construction-site-shapes-area-allocation`: `validFrom <= validTo` constraint plus an overlap-conflict rule for allocations of the same `SiteArea`.
21. Added link ontology `schedule-site-link` (`conx-ssl`) with `allocatedForActivity` / `requiresAreaAllocation` and a Core SHACL profile.
22. Extended the site example with two non-overlapping `AreaAllocation` instances and the integrated link example with an `allocatedForActivity` link.
23. Added Built Asset domain 0.1.0 (domain ontology, 2 SKOS vocabularies, Core + Vocabulary SHACL profiles, example) and `site-built-asset-link` 0.1.0 to the validated package.
24. Bumped all `construction-site/0.1.0` imports to `0.2.0` across dependent link ontologies and SHACL profiles.
25. Updated MANIFEST.json (33 entries), VALIDATION.md, README.md and the Confluence/HTML documentation.
26. Reviewed the `construct-x-skos-mapping-example/` package (5 TTL files, all parse-checked) and integrated its modeling guidance (IRI-based identity, label/synonym rules, SKOS mapping properties, separate versioned mapping artifacts, `owl:sameAs` guidance) as a new subsection of section 12 (SKOS vocabularies) in the HTML documentation.

## Changes made during 2026-10-23 … 2026-10-28 (GAEB converter, use case)

27. Added the GAEB converter `Converter/` (Java 17, Maven multi-module, Apache Jena 4.10, Spring Boot 3.2.5):
    - `core`: `GaebXmlValidator` (official GAEB XSD schemas X80–X87, Lib 3.3, 2021-05), `GaebBoqConverter` (XML → TTL per `gaeb-boq` 0.5.0), `IriFactory`/`ConxNamespaces`, `GaebConverterCli`.
    - `web`: REST API (`/api/v1/convert/gaeb-boq`, `/api/v1/validate/gaeb-boq`, `/api/v1/converters`, `/api/v1/health`, sample file endpoint) plus static upload frontend.
28. Verified the converter on 2026-10-28 with `mvn clean verify`: BUILD SUCCESS — core 13/13 tests (converter 8, SHACL 2, XSD validator 3), web 7/7 tests (REST API).
29. Added the use case documentation `usecase/` (2026-10-27): example scenario (GU → NU → logistics provider), component overview in three layers (shared Construct-X components/SDK, reusable converter services, company-specific services), interactive `index.html`.
30. Updated README.md, VALIDATION.md and the HTML documentation (new sections 14 "GAEB-Converter" and 15 "Use Case").

## Changes made during the 2026-10-30 review (manifest alignment for built-asset-breakdown-link)

31. Registered `built-asset-breakdown-link` 0.1.0 in `MANIFEST.json` (`link_ontologies`): the module (TTL + RDF/XML mirror + Core SHACL profile) was on disk since the Built Asset revision of 2026-10-22 and referenced by the Confluence documentation, the use case and `RdfApiTest` of the rdf-converter-service, but missing from the manifest. Manifest now has 34 entries (7 domain + 10 link + 17 vocabulary ontologies).
32. Re-verified the module end-to-end: RDF parse of all package files (76 TTL + 32 RDF/XML, no errors); TTL/RDF/XML mirror isomorphic (54 triples); imports exactly `built-asset/0.1.0` and `breakdown-structure/0.7.0`; no redefinitions, no prefix collisions; linking-rule architecture checks pass; SHACL: `built-asset-links-example.ttl` vs. site-built-asset-link + built-asset-breakdown-link profiles and `link-ontologies-example.ttl` vs. all 10 link profiles: 0 violations.
33. Fixed example data: `breakdown-structure-example.ttl` — added `nodeType` (`conx-de-wbs:Phase` for `ex:wbs-1`, `conx-de-wbs:Subphase` for `ex:wbs-1-1`) to satisfy the Node-Types SHACL profile (`minCount 1`, `inVocabulary`); the full SHACL suite now conforms 9/9.
34. Updated README.md (module table lists all 10 link ontologies) and VALIDATION.md (scope, SHACL run list, manifest entry count, 2026-10-30 re-verification).

## Changes made during the 2026-10-30 review (serialization completion)

35. Added the two missing RDF/XML mirrors: `link-ontologies/schedule-site-link.owl` (27 triples) and `construction-site/construction-site-area-allocation-status.owl` (25 triples); both are triple-isomorphic to their TTL sources. All 34 in-scope ontologies now have a TTL/RDF/XML pair.
36. Fixed the stale `SiteArea` comments in `construction-site/construction-site.owl` (en/de) to match the current TTL wording (stable spatial entity; `hasAreaType` as standard type; time-varying usage via AreaAllocations).
37. Re-verified the full package: 116 files parsed without errors, MANIFEST ↔ in-file `versionInfo` consistent (34 entries), no prefix collisions, all 34 TTL/RDF/XML pairs isomorphic (overall PASS).

## Changes made during the 2026-11-04 integration of notification-content

38. Registered `notification-content` 0.1.1 (domain ontology) and its four SKOS vocabularies (`notification-type`, `subject-role`, `task-status`, `task-type`, all 0.1.0) in `MANIFEST.json` — the module was on disk and referenced by the Converters' `ConxCurieRegister` (`conx-nc/nt/sr/ts/tt`) and by `examples/construct-x-doppelboden-beispieldaten/notification/doppelboden-task-request.json`, but missing from the manifest and validation scope. Manifest now has 39 entries (8 domain + 10 link + 21 vocabulary ontologies).
39. Added the Core SHACL profile mirror: RDF/XML serializations for all five TTL files of the module (ontology, 4 vocabularies), each triple-isomorphic to its TTL source. The package now has 39 in-scope TTL/RDF/XML pairs.
40. Added `notification-content-example.ttl` (three `NotificationContent` instances: `TaskRequested`/`DetailedScheduling` mirroring the doppelboden reference notification, `TaskStatusChanged`/`InProgress`, `ResultAvailable`) and re-verified the full package: 83 TTL + 39 RDF/XML parsed without errors; SHACL now 10/10 runs conform, 0 violations (new 10th run: notification example vs. Core profile, with a negative test confirming the SPARQL constraints are active); MANIFEST ↔ in-file `versionInfo` consistent (39 entries); no prefix collisions.

## Changes made during the 2026-11-04 JSON-LD context work

41. Added `contexts/construct-x-context.jsonld` (context `https://www.construct-x.org/context/construct-x/0.1.0`, `@version: 1.1`): a single combined JSON-LD context covering all 8 domain ontologies, all 10 link ontologies and all 21 SKOS vocabularies. 371 `@context` entries = 1 `@version` + 54 prefixes (15 standard, 8 domain, 10 link, 21 SKOS-vocabulary) + 204 bare term→IRI mappings + 112 object definitions; colliding bare term names usable only via their module prefix (316 bare term keys in total). IRI bases: `https://www.construct-x.org/ontology/<module>#<Name>` for ontology terms and `https://www.construct-x.org/vocab/<module>/<vocab>#<Concept>` for SKOS concepts.
42. Added `contexts/validation/`: a self-contained Jena 4.10.0 verification project — `pom.xml`, `src/main/java/Main.java` (expands the test document against the context, asserts 64 expected IRIs, re-serializes and checks the roundtrip), `test/test-doc.jsonld` (a minimal multi-module example document referencing the context via relative path `../../construct-x-context.jsonld`) and `test/test-doc-reference.md` (expected-IRI reference). No `target/` committed.
43. Verified the context with Jena 4.10.0 (JDK 25, Maven 3.9.9): the test document expands to 42 triples, all 64 expected IRIs are present (plus 2 additional IRIs, allowed by the one-way assertion), roundtrip 42→42, exit code 0 — result `ERGEBNIS: PASS` (2026-11-04).
44. Registered the context in `MANIFEST.json` as section `json_ld_context` (`construct-x-context: 0.1.0`; the 39 ontology entries remain unchanged) and updated README.md, VALIDATION.md and `documentation/CONSTRUCT-X-ONTOLOGIES.html` (new section 18, navigation entry).
45. Performed a consistency check of item 44 against the current state (2026-11-04): `MANIFEST.json` carries the `json_ld_context` section (lines 61–62) with all 39 ontology entries (8 domain + 10 link + 21 vocabulary) unchanged; README.md documents the context (line 45); VALIDATION.md carries the Jena validation section (lines 84–98); the HTML documentation has the section 18 anchor (lines 2230–2297) and its navigation entry (line 140). All sub-claims of item 44 confirmed.

## Changes made during the 2026-11-05 Construct-X SDK work (converter repo)

46. Created the Construct-X SDK as a new Maven module `construct-x-sdk/` in the separate `Construct-X-Converters` repo (`org.construct-x:construct-x-sdk:0.1.0-SNAPSHOT`, Java 25, Maven, Jena 4.10.0, Jackson 2.17.2, JUnit 5.10.2, no Spring) — the shared library layer ("Ebene 1" of the use-case architecture) below the converter services. Main classes: `ConxCurieRegister`, `IriFactory`, `OntologyRegistry`, `ShaclValidatorHelper`, `ProvenanceHelper`, `RdfInput`, `PlainJsonModelWriter`, base `ConxNamespaces`; 6 test classes, 81 tests.
47. De-duplicated the byte-identical copies across the three converter builds: `ConxCurieRegister` (was ×3, now extended with `prefixFor()`/`namespaceFor()`), `RdfInput` (×2), `PlainJsonModelWriter` (×3) and the base part of the GAEB `ConxNamespaces` (the GAEB-specific term constants `P_IDENTIFIER`, `BILL_OF_QUANTITIES`, … remain in the GAEB `core` module). The 12 duplicated source files (main + test) were deleted from the converter builds; the SDK was wired in as a dependency of `Converter/core`, `msproject-converter-service` and `rdf-converter-service`, with the `org.constructx.sdk` imports added at the 12 affected usage sites.
48. Re-verified all builds on 2026-11-05 (Maven 3.9.9, JDK 25): `construct-x-sdk` 81/81, GAEB converter core 17/17 + web 15/15, MS-Project 33/33, RDF 15/15 — all BUILD SUCCESS (converter test total dropped from 104 to 80 because the duplicated unit tests now run once in the SDK). Registered the SDK as a new `sdk` section in `MANIFEST.json` and updated VALIDATION.md accordingly.

## Changes made during the 2026-11-06 integration of the Construction Progress Extension, the Baufortschritt example and the ICDD container examples

49. Integrated the supplied `construct-x-construction-progress` extension (0.1.0) as a new module under `extensions/construct-x-construction-progress/` (internal structure kept as delivered: `ontology/`, `shapes/`, `examples/`, `queries/`, README, documentation.html, technical-check.txt). It is an external extension of the IoC Process Ontology (`w3id.org/ioc`) and BOT (`w3id.org/bot`) with its own IRI scheme (`w3id.org/construct-x/construction-progress#`), not one of the 8 domain ontologies — the Linking Rule (relations only in link ontologies between Construct-X domains) does not apply to it. Added the package-standard `owl:versionIRI <…/construction-progress/0.1.0>` to the ontology (it previously only carried `owl:versionInfo "0.1.0"`).
50. Integrated the supplied Baufortschritt end-to-end example as `examples/construct-x-baufortschritt-beispiel/` (3 Plain-JSON data revisions delivery→transport→installation, 3 Tractus-X-header notifications, `result/example-answer.json`, README, documentation.html) and the two ICDD container examples as `examples/construct-x-icdd-beispiele/` (README, documentation.html, technical-check.txt, `construct-x-baufortschritt-beispiel.icdd`, `construct-x-doppelboden-feinterminplanung.icdd`; the `.icdd` files are ISO 21597 ZIP containers and are committed despite the `*.zip` ignore rule).
51. Synced the Doppelboden ICDD container to the current ontology (per project premise: nothing is published, examples may be adjusted): the embedded `Ontology resources/notification-content-ontology.ttl` was replaced 0.1.0 → 0.1.1 (adds `contextResource`). The ontology copy is not a checksummed `ct:InternalDocument`, so no `Index.rdf` change was needed; all 3 payload-document SHA-256 checksums were re-verified OK. The `informationContainer` back-reference fields in the container notifications are kept (they point to the container's own UUID). The Baufortschritt container was left unchanged (embedded `cxcp` ontology bit-identical to the extension module, all 8 payload checksums already OK).
52. Extended the JSON-LD context `contexts/construct-x-context.jsonld` with the `cxcp` prefix and 8 bare terms (`TransportProcess`, `InstallationProcess`, `ProgressEvidence`, `hasExecutionSpace`, `hasExecutionSpaceValue`, `hasProgressEvidence`, `hasProgressEvidenceValue`, `ifcGlobalId`) — 371 → 380 `@context` entries. `@version` was **not** bumped: Jena 4.10.0 (the repo's verification gate) accepts the non-standard `@version` field only with the value `1.1` (verified by a value matrix); the versioned context `@id` IRI (0.1.0) remains the version marker.
53. Extended the Jena verification project: `test/test-doc.jsonld` gained node N11 (`cxcp:InstallationProcess` with all 7 property uses), `Main.java` now asserts 75 expected IRIs (was 64), `test/test-doc-reference.md` updated (N11 row, §3.5 cxcp evidence, IRI count). Verification (Jena 4.10.0, JDK 25, Maven 3.9.9): **PASS** — 48 triples / 77 IRIs expanded, all 75 expected IRIs present, roundtrip 48 → 48, exit code 0.
54. Re-verified the full package (2026-11-06, dedicated venv rdflib 6.3.2 + pySHACL 0.28.1): 86 TTL + 39 RDF/XML parsed without errors; SHACL 11/11 runs conform, 0 violations (new 11th run: cxcp example vs. cxcp profile with `advanced=True` for the `sh:sparql` Transport constraint, plus a negative test proving that constraint is active); MANIFEST ↔ in-file `versionInfo` consistent (41 entries incl. the new `extensions` section); ICDD integrity check: both containers parse (Index.rdf, links.rdf, embedded ontology), all 11 payload-document SHA-256 checksums OK.
55. Registered the extension in `MANIFEST.json` (new `extensions` section, date advanced to 2026-11-06) and updated README.md, VALIDATION.md (scope, SHACL run 11, manifest count 41, new ICDD validation section, Notes 25–29), AUDIT.md (this entry) and `documentation/CONSTRUCT-X-ONTOLOGIES.html` (new section 19 + navigation entry).

## Result

The package is internally consistent with the documented modularity rule: source ontologies remain independent and all cross-domain ObjectProperties reside in link ontologies.
