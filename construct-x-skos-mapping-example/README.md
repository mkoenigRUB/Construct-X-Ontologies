# Construct-X SKOS Mapping Example

Das Paket enthält verschiedene Modellierungsoptionen:

1. `construct-x-area-type-vocab.ttl`
   - stabiles Construct-X-Vokabular
   - `skos:prefLabel`
   - `skos:altLabel`
   - `skos:broader`

2. `external-example-vocab.ttl`
   - fiktives externes Vokabular für das Mapping-Beispiel

3. `construct-x-area-type-mappings.ttl`
   - empfohlene separate Mapping-Datei
   - `skos:exactMatch`
   - `skos:closeMatch`
   - `skos:broadMatch`
   - `skos:narrowMatch`
   - `skos:relatedMatch`

4. `OPTION-inline-mappings.ttl`
   - technisch mögliche Inline-Alternative

5. `OPTION-owl-sameAs-not-recommended.ttl`
   - zeigt, warum `owl:sameAs` normalerweise nicht verwendet werden sollte

6. `SKOS-MAPPING-DOCUMENTATION.md`
   - vollständige Dokumentation und Entscheidungstabelle

7. `VALIDATION.md`
   - Parseprüfung der Turtle-Dateien
