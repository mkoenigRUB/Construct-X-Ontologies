# Construct-X SKOS Vocabulary Mapping – Beispiel und Modellierungsoptionen

## Ziel

Dieses Beispiel zeigt, wie Begriffe in Construct-X-Vokabularen

1. eindeutig identifiziert,
2. mit Synonymen versehen,
3. hierarchisch strukturiert und
4. mit Concepts aus anderen Vokabularen verknüpft

werden können.

Die zentrale Regel lautet:

> **Ein Concept wird durch seine IRI eindeutig identifiziert. Labels sind nur sprachliche Bezeichnungen.**

Beispiel:

```text
IRI:
https://www.construct-x.org/vocab/construction-site/area-type#LoadingZone

Labels:
"Ladezone"@de
"Loading Zone"@en
"Entladezone"@de
```

Alle Bezeichnungen beziehen sich auf **dasselbe Concept**.

---

## Option 1 – Synonyme innerhalb desselben Vokabulars

Datei:

`construct-x-area-type-vocab.ttl`

```turtle
conx-area:LoadingZone
    a skos:Concept ;
    skos:prefLabel "Loading Zone"@en ;
    skos:prefLabel "Ladezone"@de ;
    skos:altLabel "Entladezone"@de ;
    skos:altLabel "Be- und Entladebereich"@de .
```

### Bedeutung

- `skos:prefLabel` = bevorzugte Bezeichnung eines Concepts in einer Sprache
- `skos:altLabel` = alternatives Label bzw. Synonym

### Verwenden, wenn

- fachlich dieselbe Bedeutung gemeint ist,
- nur unterschiedliche Benennungen existieren,
- keine zweite fachliche Identität erzeugt werden soll.

### Construct-X-Empfehlung

**Standardlösung für Synonyme innerhalb eines Construct-X-Vokabulars.**

---

## Option 2 – Concepts verschiedener Vokabulare verknüpfen

Datei:

`construct-x-area-type-mappings.ttl`

Die Concepts behalten ihre eigenen IRIs:

```text
Construct-X:
https://www.construct-x.org/vocab/construction-site/area-type#LoadingZone

Extern:
https://example.org/vocab/site-logistics#LoadingArea
```

Sie werden nicht zusammengeführt, sondern semantisch gemappt.

### 2a. `skos:exactMatch`

```turtle
conx-area:LoadingZone
    skos:exactMatch ext:LoadingArea .
```

Bedeutung:

> Beide Concepts können im vorgesehenen fachlichen Kontext als äquivalent behandelt werden.

**Typischer Einsatz:** Zwei unterschiedliche Vokabulare verwenden für fachlich denselben Begriff unterschiedliche IRIs.

---

### 2b. `skos:closeMatch`

```turtle
conx-area:WorkArea
    skos:closeMatch ext:ProductionArea .
```

Bedeutung:

> Die Concepts sind sehr ähnlich, aber nicht vollständig deckungsgleich.

**Typischer Einsatz:** Bedeutungsumfang oder Anwendungsbereich unterscheiden sich leicht.

---

### 2c. `skos:broadMatch`

```turtle
conx-area:EquipmentSetupArea
    skos:broadMatch ext:MaterialHandlingArea .
```

Bedeutung:

> Der externe Begriff ist allgemeiner.

```text
MaterialHandlingArea
       ▲
       │ broadMatch
EquipmentSetupArea
```

---

### 2d. `skos:narrowMatch`

```turtle
conx-area:StorageArea
    skos:narrowMatch ext:TemporaryStorageArea .
```

Bedeutung:

> Der externe Begriff ist spezieller.

```text
StorageArea
     │
     │ narrowMatch
     ▼
TemporaryStorageArea
```

---

### 2e. `skos:relatedMatch`

```turtle
conx-area:LoadingZone
    skos:relatedMatch ext:MaterialHandlingArea .
```

Bedeutung:

> Die Concepts sind fachlich verwandt, aber weder synonym noch eindeutig hierarchisch zugeordnet.

---

## Option 3 – Hierarchie innerhalb desselben Vokabulars

Datei:

`construct-x-area-type-vocab.ttl`

```turtle
conx-area:IntermediateStorageArea
    skos:broader conx-area:StorageArea .
```

Damit gilt:

```text
StorageArea
    └── IntermediateStorageArea
```

Die inverse Beziehung wäre:

```turtle
conx-area:StorageArea
    skos:narrower conx-area:IntermediateStorageArea .
```

Für die Modellierung genügt in der Regel eine Richtung.

Wichtig:

- `skos:broader` / `skos:narrower` → **innerhalb eines ConceptSchemes**
- `skos:broadMatch` / `skos:narrowMatch` → **zwischen unterschiedlichen Vokabularen**

---

## Option 4 – Mapping direkt im Construct-X-Vokabular

Datei:

`OPTION-inline-mappings.ttl`

Technisch kann ein Mapping direkt am Concept stehen:

```turtle
conx-area:LoadingZone
    skos:exactMatch ext:LoadingArea .
```

### Vorteile

- alle Informationen stehen direkt beim Concept,
- einfach zu lesen.

### Nachteile

- das Construct-X-Vokabular wird enger an externe Vokabulare gekoppelt,
- Änderungen externer Mappings können Änderungen am Core-Vokabular notwendig machen,
- bei vielen externen Standards wird das Vokabular schnell unübersichtlich.

### Construct-X-Empfehlung

**Nur für wenige, sehr stabile externe Referenzen verwenden.**

---

## Option 5 – Separates Mapping-Artefakt

Das ist die **empfohlene Construct-X-Lösung**.

```text
Construct-X Vocabulary
        │
        │ SKOS mapping
        ▼
External Vocabulary
```

Beispiel:

```text
construction-site/
└── vocab/
    └── area-type.ttl

mappings/
└── construction-site/
    ├── area-type-to-standard-A.ttl
    ├── area-type-to-standard-B.ttl
    └── area-type-to-company-C.ttl
```

### Vorteile

- Core-Vokabular bleibt unabhängig,
- Mappings sind separat versionierbar,
- mehrere externe Vokabulare können parallel angebunden werden,
- Mappingfehler verändern nicht das Construct-X-Core-Vokabular,
- nationale oder organisationsspezifische Mappings sind möglich.

Beispiel:

```turtle
conx-area:LoadingZone
    skos:exactMatch ext:LoadingArea .
```

steht dann **nur in der Mapping-Datei**.

### Construct-X-Empfehlung

**Dies sollte das Standardverfahren für externe Vocabulary Mappings sein.**

---

## Option 6 – `owl:sameAs`

Datei:

`OPTION-owl-sameAs-not-recommended.ttl`

Theoretisch:

```turtle
conx-area:LoadingZone
    owl:sameAs ext:LoadingArea .
```

Für normale Vokabular-Mappings ist dies **nicht zu empfehlen**.

`owl:sameAs` bedeutet vollständige logische Identität beider RDF-Ressourcen.

Das ist stärker als:

```turtle
skos:exactMatch
```

### Construct-X-Regel

Für Begriffs-Mappings:

```text
skos:exactMatch
```

bevorzugen.

`owl:sameAs` nur verwenden, wenn tatsächlich **dieselbe RDF-Ressource** unter zwei unterschiedlichen IRIs bezeichnet wird.

---

## Entscheidungstabelle

| Situation | Empfohlene Modellierung |
|---|---|
| anderer Name für dasselbe Concept | `skos:altLabel` |
| bevorzugte Bezeichnung | `skos:prefLabel` |
| Ober-/Unterbegriff im selben Vokabular | `skos:broader` / `skos:narrower` |
| gleiche Bedeutung in anderem Vokabular | `skos:exactMatch` |
| sehr ähnliche Bedeutung | `skos:closeMatch` |
| anderes Concept ist allgemeiner | `skos:broadMatch` |
| anderes Concept ist spezieller | `skos:narrowMatch` |
| nur fachlich verwandt | `skos:relatedMatch` |
| vollständige RDF-Ressourcenidentität | `owl:sameAs` – Ausnahmefall |

---

## Empfohlene Construct-X-Modellierungsregel

### Englisch

> **Concepts in Construct-X controlled vocabularies MUST be identified by stable IRIs. Preferred terms SHOULD be represented using `skos:prefLabel`; synonyms and alternative terms SHOULD be represented using `skos:altLabel`. Hierarchical relations within a vocabulary SHOULD use `skos:broader` and `skos:narrower`. Semantic correspondences to concepts in external vocabularies SHOULD use SKOS mapping properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`). External mappings SHOULD normally be maintained in separately versioned mapping artifacts. `owl:sameAs` SHOULD NOT be used for ordinary vocabulary alignment.**

### Deutsch

> **Begriffe in kontrollierten Construct-X-Vokabularen MÜSSEN durch stabile IRIs eindeutig identifiziert werden. Vorzugsbezeichnungen SOLLTEN mit `skos:prefLabel`, Synonyme und alternative Bezeichnungen mit `skos:altLabel` modelliert werden. Hierarchische Beziehungen innerhalb eines Vokabulars SOLLTEN mit `skos:broader` und `skos:narrower` beschrieben werden. Semantische Entsprechungen zu Concepts anderer Vokabulare SOLLTEN mit den SKOS-Mapping-Properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) beschrieben werden. Externe Mappings SOLLTEN grundsätzlich als separat versionierte Mapping-Artefakte gepflegt werden. `owl:sameAs` SOLLTE nicht für gewöhnliche Vokabularabgleiche verwendet werden.**

---

## Beispielabfragen

### Alle deutschen Bezeichnungen eines Concepts

```sparql
SELECT ?label
WHERE {
  conx-area:LoadingZone
      (skos:prefLabel|skos:altLabel) ?label .
  FILTER (lang(?label) = "de")
}
```

### Alle exakt gemappten externen Concepts

```sparql
SELECT ?externalConcept
WHERE {
  conx-area:LoadingZone
      skos:exactMatch ?externalConcept .
}
```

### Alle Unterbegriffe von `StorageArea`

```sparql
SELECT ?concept
WHERE {
  ?concept skos:broader+ conx-area:StorageArea .
}
```

---

## Empfehlung für Construct-X

Für Construct-X würde ich folgende Reihenfolge festlegen:

```text
1. Stable IRI
   ↓
2. prefLabel
   ↓
3. altLabel für Synonyme
   ↓
4. broader/narrower für interne Hierarchien
   ↓
5. separate Mapping-Dateien für externe Vokabulare
   ↓
6. exactMatch / closeMatch / broadMatch / narrowMatch / relatedMatch
```

Damit bleiben **Identität, Terminologie und externe Interoperabilität sauber getrennt**.
