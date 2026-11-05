# Gesamtübersicht der zu entwickelnden Komponenten

Für die Umsetzung des Szenarios werden die vorhandenen Fachsysteme der drei Beteiligten grundsätzlich weiterverwendet. Es wird davon ausgegangen, dass bereits Systeme für Terminplanung, WBS-/LBS-Verwaltung, Baustellenplanung, Equipment-Verwaltung und Taktplanung vorhanden sind.

Die wesentliche Entwicklungsarbeit besteht daher nicht in der Neuentwicklung dieser Fachanwendungen, sondern in ihrer **semantischen Anbindung über Construct-X** sowie in den Diensten für die organisationsübergreifende Bereitstellung und Verarbeitung der Daten.

Dabei sollten drei Arten von Komponenten unterschieden werden:

```
1. Gemeinsame Construct-X-Komponenten

2. Wiederverwendbare Converter-Services

3. Unternehmensspezifische Fach- und Integrationsdienste
```

Die eigentliche Datenraumtechnik – insbesondere Identität, Katalog, Policies, Agreements und Datentransfer – sollte möglichst durch vorhandene Datenraumkomponenten bereitgestellt und lediglich integriert bzw. konfiguriert werden.

---

# Gemeinsame Construct-X-Komponenten

Diese Komponenten werden einmal entwickelt und anschließend von allen Teilnehmern verwendet.

Dazu gehören insbesondere:

- Construct-X Ontologien,
- Construct-X Link Ontologies,
- kontrollierte SKOS-Vokabulare,
- SHACL-Profile,
- JSON-LD-Kontexte,
- gemeinsame IRI-Konventionen,
- Provenance-Konventionen,
- Regeln zur Versionierung der Ontologien und Profile.

Zusätzlich bietet sich eine gemeinsame Softwarebibliothek bzw. ein **Construct-X SDK** an.

Dieses könnte beispielsweise Funktionen bereitstellen für:

```
Construct-X Daten lesen und schreiben
        ↓
Ontologien laden
        ↓
IRIs erzeugen und verwalten
        ↓
Vokabulare auflösen
        ↓
SHACL validieren
        ↓
Provenance erzeugen
        ↓
Semantic Profiles prüfen
```

Diese Funktionen müssen dann nicht von jedem Teilnehmer erneut implementiert werden.

---

# Wiederverwendbare Converter-Services

Converter zwischen bestehenden Fachsystemen und Construct-X sollten möglichst **nicht individuell für jedes Unternehmen entwickelt werden**.

Stattdessen sollten wiederverwendbare Converter für häufig eingesetzte Systeme oder Datenformate entstehen.

Beispiele:

```
Microsoft Project ↔ Construct-X

Primavera ↔ Construct-X

Metronom ↔ Construct-X

GAEB ↔ Construct-X

IFC ↔ Construct-X

Equipment-System ↔ Construct-X
```

Ein Converter enthält dabei die allgemeine Abbildungslogik zwischen einem Fachsystem und den Construct-X-Ontologien.

Beispielsweise:

```
Microsoft Project Task
        ↓
Construct-X Activity

Dependency
        ↓
PrecedenceRelationship

Start / Finish
        ↓
plannedStart / plannedFinish
```

Der gleiche Converter kann anschließend von mehreren Unternehmen eingesetzt werden.

---

## Konfigurierbare Mapping-Profile

Nicht alle Unternehmen verwenden ein Fachsystem auf dieselbe Weise.

Deshalb sollte zwischen

```
allgemeiner Converter-Logik
```

und

```
unternehmens- bzw.
projektspezifischer Konfiguration
```

unterschieden werden.

Beispielsweise:

```
MS Project → Construct-X Converter
                │
        ┌───────┼────────┐
        │       │        │
     Profil A Profil B Profil C
        │       │        │
        ▼       ▼        ▼
      GU A    GU B     GU C
```

Ein Mapping-Profil kann beispielsweise festlegen:

- welches Feld den WBS-Code enthält,
- welches Feld eine LBS-Referenz enthält,
- wie benutzerdefinierte Attribute abgebildet werden,
- welche internen Codes auf welche Construct-X-Vokabulare gemappt werden,
- wie vorhandene externe Identifikatoren behandelt werden.

Damit bleibt der Converter wiederverwendbar, während die Besonderheiten einzelner Unternehmen konfigurierbar bleiben.

---

## Betriebsmodelle der Converter

Ein Converter kann technisch auf unterschiedliche Weise bereitgestellt werden.

### Zentraler Converter-Service

```
Fachsystem
     ↓
zentraler Converter-Service
     ↓
Construct-X
```

Mehrere Unternehmen verwenden denselben betriebenen Dienst.

Dies reduziert den Installationsaufwand, setzt jedoch voraus, dass die zu konvertierenden Daten an diesen Dienst übertragen werden dürfen.

### Lokale Instanz eines gemeinsamen Converter-Services

Alternativ kann dieselbe Converter-Software als Container oder Service beim jeweiligen Unternehmen betrieben werden:

```
Fachsystem
     ↓
lokale Instanz des
gemeinsamen Converters
     ↓
Construct-X
     ↓
Datenraum
```

Damit verlassen die Daten das Unternehmen erst nach ihrer Umwandlung in das vereinbarte Austauschmodell.

Für sensible Projektdaten ist dieses Modell besonders geeignet.

Die Converter sollten daher möglichst als **portabel deploybare Services bzw. Container** entwickelt werden.

---

# Generalunternehmer

Beim Generalunternehmer entsteht weiterhin der größte unternehmensspezifische Entwicklungsumfang, da hier mehrere Informationsquellen zu einem gemeinsamen Planungskontext zusammengeführt werden.

## Vorhandene Systeme

Es wird angenommen, dass bereits vorhanden sind:

- Terminplanungssystem,
- WBS-System,
- LBS-System,
- System für Baustellen- bzw. Baustelleneinrichtungsplanung.

Diese Systeme bleiben unverändert bestehen.

---

## Wiederverwendbare Converter

Der Generalunternehmer verwendet geeignete gemeinsame Converter-Services:

```
Terminplanung
      ↓
Terminplanung ↔ Construct-X Converter


WBS/LBS-System
      ↓
Breakdown Structure ↔ Construct-X Converter


Baustellenplanung
      ↓
Construction Site ↔ Construct-X Converter
```

Hier muss grundsätzlich nur dann ein neuer Converter entwickelt werden, wenn für das verwendete Fachsystem noch keiner verfügbar ist.

Für die konkrete Nutzung werden gegebenenfalls Mapping-Profile des Generalunternehmers erstellt.

---

## Unternehmensspezifisch zu entwickeln

### Planning Assignment Service

Dieser Dienst verwaltet die konkreten Planungsaufträge.

Er legt beispielsweise fest:

```
welcher Nachunternehmer
        ↓
welche Rahmenaktivität
        ↓
mit welchem Kontext
        ↓
detaillieren soll
```

Er verwaltet insbesondere:

- zu detaillierende Aktivitäten,
- Kontextaktivitäten,
- Nachunternehmer,
- benötigte WBS-/LBS-Informationen,
- benötigte Site-Informationen,
- benötigte Equipment-Typen,
- Planungszweck.

---

### Semantic Integration Service

Dieser Dienst verbindet die bereits nach Construct-X konvertierten Daten.

Beispielsweise:

```
Schedule Graph ─────────┐
                       │
WBS/LBS Graph ─────────┼──► Semantic Integration
                       │
Site Graph ────────────┘
```

Er nutzt insbesondere die Construct-X Link Ontologies.

Dadurch können beispielsweise Beziehungen ermittelt werden:

```
Activity
   ↓
LBSNode
   ↑
SiteArea
   ↑
SiteEquipment
```

---

### Context Selection Service

Dieser Dienst bestimmt auf Grundlage eines konkreten Planungsauftrags, welche Informationen tatsächlich benötigt werden.

Beispielsweise:

```
PA-100
   ↓
Activity A100
   ↓
relevante WBS/LBS
   ↓
relevante SiteAreas
   ↓
benötigtes Equipment
```

Damit wird nicht der gesamte Projektdatenbestand übertragen, sondern nur der erforderliche Teilgraph.

---

### External Data Client

Der Generalunternehmer benötigt eine Funktion, mit der externe Datenangebote aufgerufen werden können.

Im Szenario betrifft dies insbesondere:

```
Equipment Data Service
des Baulogistikdienstleisters
```

Der Client fragt die für den konkreten Planning Context benötigten Daten ab.

---

### Planning Context Service

Der zentrale neue Dienst des Generalunternehmers ist der **Planning Context Service**.

Er kombiniert:

```
Planning Assignment
        +
Schedule
        +
WBS/LBS
        +
Site Data
        +
autorisierte externe Daten
        ↓
Construct-X Planning Context
```

Der Dienst übernimmt insbesondere:

- semantische Auswahl der relevanten Daten,
- Zusammenführung der Teilgraphen,
- Berücksichtigung von Nutzungsrechten,
- Provenance,
- SHACL-Prüfung,
- Erzeugung eines eindeutigen Snapshots,
- Bereitstellung über den Datenraum.

---

### Detailed Schedule Integration Service

Für den Rückweg benötigt der Generalunternehmer einen Dienst zur Verarbeitung der Detailplanung des Nachunternehmers.

Dieser übernimmt:

```
Construct-X Detailed Schedule
        ↓
Validierung
        ↓
Zuordnung zur Framework Activity
        ↓
Konsistenzprüfung
        ↓
Converter
        ↓
internes Terminplanungssystem
```

Der eigentliche technische Import in das Terminplanungssystem kann wiederum über den gemeinsamen Terminplan-Converter erfolgen.

---

## Übersicht Generalunternehmer

### Gemeinsame Komponenten nutzen

- Terminplan ↔ Construct-X Converter
- WBS/LBS ↔ Construct-X Converter
- Site ↔ Construct-X Converter
- Construct-X SDK
- SHACL-Profile
- Ontologien und Vokabulare

### Unternehmensspezifisch entwickeln

- Mapping-Profile,
- Planning Assignment Service,
- Semantic Integration Service,
- Context Selection Service,
- External Data Client,
- Planning Context Service,
- Rights-aware Data Selection,
- Snapshot- und Provenance-Verwaltung,
- Detailed Schedule Integration Service.

---

# Baulogistikdienstleister

Der Baulogistikdienstleister besitzt bereits ein System zur Verwaltung seiner Geräte und Baustellenressourcen.

## Vorhandenes System

Beispielsweise:

```
Equipment Management System

Equipment
Equipment Type
Projekt
Standort
Status
Verfügbarkeit
```

---

## Wiederverwendbarer Converter

Für dieses System wird ein:

```
Equipment System
        ↔
Construct-X
```

Converter benötigt.

Ist das eingesetzte Equipment-System auch bei anderen Unternehmen verbreitet, sollte dieser Converter als allgemeiner wiederverwendbarer Service entwickelt werden.

Er bildet beispielsweise ab:

```
internes Equipment
        ↓
SiteEquipment

interner Equipment Type
        ↓
Construct-X SKOS Concept

Standort
        ↓
SiteArea
```

Unternehmensspezifisch ist lediglich das dazugehörige Mapping-Profil.

---

## Unternehmensspezifisch zu entwickeln

### Equipment Data Service

Der wichtigste Dienst beim Baulogistikdienstleister ist der:

```
Equipment Data Service
```

Er ermöglicht beispielsweise Abfragen nach:

- Projekt,
- Baustellenbereich,
- Equipment-Typ,
- Status,
- Verfügbarkeit.

Er verwendet den Converter, um die Ergebnisse in Construct-X bereitzustellen.

---

### Policy-Konfiguration

Der Baulogistikdienstleister definiert, welche Informationen unter welchen Bedingungen genutzt werden dürfen.

Beispielsweise:

```
Generalunternehmer darf

Equipment-Daten nutzen
        +
für Project-X verwenden
        +
in Planning Context integrieren
        +
an berechtigte Nachunternehmer weitergeben
```

Hier ist überwiegend Konfiguration und keine eigene Fachsoftwareentwicklung erforderlich.

---

### Provenance

Der Dienst muss sicherstellen, dass die Equipment-Ressourcen ihre ursprünglichen Identitäten behalten.

Beispielsweise:

```
https://data.logistics-provider.example/
equipment/4711
```

Damit bleibt der Baulogistikdienstleister auch nach der Integration in einen Planning Context eindeutig als Datenquelle erkennbar.

---

## Übersicht Baulogistikdienstleister

### Gemeinsame Komponenten nutzen

- Equipment ↔ Construct-X Converter,
- Construct-X SDK,
- Construction Site Ontology,
- Equipment-Vokabulare,
- SHACL-Profile.

### Unternehmensspezifisch entwickeln

- Mapping-Profil,
- Equipment Data Service,
- Abfrage-/Filterlogik,
- Policy-Konfiguration,
- Provenance- und Identitätskonfiguration.

Der Entwicklungsumfang bleibt damit vergleichsweise gering.

---

# Nachunternehmer

Beim Nachunternehmer wird davon ausgegangen, dass bereits ein Taktplanungssystem wie Metronom vorhanden ist.

## Vorhandenes System

```
Metronom
```

wird weiterhin für die eigentliche Detail- bzw. Taktplanung verwendet.

---

## Wiederverwendbarer Metronom-Converter

Für Construct-X sollte ein gemeinsamer bidirektionaler Converter entwickelt werden:

```
Construct-X
        ↓
Metronom Converter
        ↓
Metronom

und

Metronom
        ↓
Metronom Converter
        ↓
Construct-X
```

Dieser Converter sollte nicht speziell für einen einzelnen Nachunternehmer entwickelt werden.

Alle Unternehmen, die Metronom verwenden, könnten denselben Converter nutzen.

---

## Mapping-Profile

Auch hier können projektspezifische bzw. unternehmensspezifische Einstellungen erforderlich sein.

Beispielsweise:

```
Construct-X LBSNode
        ↓
welche Metronom-Struktur?

Construct-X Activity
        ↓
welcher Metronom-Aktivitätstyp?

externe IRI
        ↓
welches Metronom Custom Field?
```

Diese Einstellungen werden als Mapping-Profil hinterlegt.

---

## Unternehmensspezifisch zu entwickeln

### Planning Context Client

Der Nachunternehmer benötigt einen einfachen Client bzw. Integrationsdienst, der einen Planning Context für einen konkreten Planungsauftrag anfordert und übernimmt.

```
Planning Assignment
       ↓
Planning Context anfordern
       ↓
Planning Context empfangen
```

---

### Identity Mapping

Beim Import müssen die ursprünglichen Construct-X-Identitäten erhalten bleiben.

Beispielsweise:

```
Construct-X Activity A100
        ↓
Metronom Object 4711

External IRI:
.../activity/A100
```

Diese Mapping-Information wird benötigt, damit die Detailplanung anschließend wieder eindeutig auf die ursprüngliche Rahmenaktivität verweisen kann.

---

### Detailplanung exportieren

Neue Aktivitäten des Nachunternehmers erhalten eigene stabile Identitäten:

```
Metronom Activity
        ↓
Nachunternehmer-IRI
        ↓
Construct-X Activity
```

Zusätzlich werden die Beziehungen zur Rahmenaktivität erzeugt.

---

### Detailed Schedule Service

Das erzeugte Planungsergebnis wird anschließend über einen:

```
Detailed Schedule Service
```

für den Generalunternehmer bereitgestellt.

Dieser übernimmt insbesondere:

- Ausgabe des Construct-X Graphen,
- Bezug zum Planungsauftrag,
- Bezug zum Planning-Context-Snapshot,
- SHACL-Prüfung,
- Provenance.

---

## Übersicht Nachunternehmer

### Gemeinsame Komponenten nutzen

- Metronom ↔ Construct-X Converter,
- Construct-X SDK,
- Ontologien und Link Ontologies,
- Vokabulare,
- SHACL-Profile.

### Unternehmensspezifisch entwickeln

- Metronom-Mapping-Profil,
- Planning Context Client,
- Identity Mapping,
- Verwaltung eigener IRIs,
- Bezug zu Framework Activities,
- Bezug zum Planning-Context-Snapshot,
- Detailed Schedule Service.

---

# Datenraumkomponenten bei allen Teilnehmern

Jeder Teilnehmer benötigt zusätzlich eine Datenraumkomponente bzw. einen Connector.

Benötigt werden grundsätzlich:

```
Identity
Catalog
Policy / Agreement
Transfer
```

Diese Funktionen sollten jedoch **nicht projektspezifisch neu programmiert** werden.

Die projektspezifische Integration besteht im Wesentlichen darin, die eigenen Construct-X-Dienste an den Datenraum anzubinden:

```
Construct-X Service
        ↕
Dataspace Connector
```

Beispielsweise:

```
Planning Context Service
        ↕
Connector
```

oder:

```
Equipment Data Service
        ↕
Connector
```

---

# Gesamtübersicht der Implementierung

| Ebene | Generalunternehmer | Baulogistikdienstleister | Nachunternehmer |
| --- | --- | --- | --- |
| **Vorhandenes Fachsystem** | Terminplanung, WBS, LBS, Site | Equipment-System | Metronom |
| **Gemeinsamer Converter** | Terminplan, WBS/LBS, Site ↔ Construct-X | Equipment ↔ Construct-X | Metronom ↔ Construct-X |
| **Mapping-Profil** | GU-spezifisch | Logistik-spezifisch | NU-spezifisch |
| **Semantische Integration** | umfangreich | gering | gering |
| **Eigener Kerndienst** | Planning Context Service | Equipment Data Service | Detailed Schedule Service |
| **Zusätzlicher Dienst** | Planning Assignment / Context Selection | Query Service | Planning Context Client |
| **SHACL** | nutzen | nutzen | nutzen |
| **Provenance** | integrieren | Quelle kennzeichnen | Planung kennzeichnen |
| **Datenraum** | Connector konfigurieren | Connector konfigurieren | Connector konfigurieren |

---

# Empfohlene Aufteilung der Entwicklungsarbeit

Aus Implementierungssicht ergeben sich damit vier klar getrennte Arbeitspakete.

### A. Construct-X Semantic Core

Einmal gemeinsam entwickeln:

```
Ontologien
Link Ontologies
Vokabulare
SHACL
JSON-LD Context
IRI-Regeln
Provenance-Regeln
SDK
```

### B. Construct-X Converter Ecosystem

Als wiederverwendbare Dienste entwickeln:

```
MS Project ↔ Construct-X
WBS/LBS ↔ Construct-X
Construction Site ↔ Construct-X
Equipment ↔ Construct-X
Metronom ↔ Construct-X
```

Die Converter sollten konfigurierbare Mapping-Profile unterstützen und sowohl zentral als auch lokal deploybar sein.

### C. Unternehmensspezifische Services

Nur einmal pro Rolle bzw. Unternehmen entwickeln:

```
GENERALUNTERNEHMER

Planning Assignment Service
Planning Context Service
Semantic Integration
Context Selection
Detailed Schedule Integration


BAULOGISTIKDIENSTLEISTER

Equipment Data Service


NACHUNTERNEHMER

Planning Context Client
Detailed Schedule Service
```

### D. Datenraum-Integration

Vorhandene Datenraumtechnik konfigurieren und anbinden:

```
Identity
Catalog
Policy
Agreement
Transfer
Connector
```

---

# Zielarchitektur

Damit ergibt sich insgesamt:

```
                 GEMEINSAME CONSTRUCT-X BASIS

       Ontologien + Vokabulare + SHACL + SDK
                         │
                         │
              CONVERTER ECOSYSTEM
                         │
     ┌───────────────────┼──────────────────┐
     │                   │                  │
 Schedule Converter   Equipment          Metronom
 WBS/LBS Converter    Converter          Converter
 Site Converter
     │                   │                  │
     ▼                   ▼                  ▼

GENERALUNTERNEHMER   BAULOGISTIK-       NACHUNTERNEHMER
                    DIENSTLEISTER

bestehende Systeme   Equipment-System   Metronom
     │                   │                  │
     ▼                   ▼                  ▼
Converter            Converter          Converter
     │                   │                  │
     ▼                   ▼                  ▼
Construct-X          Construct-X        Construct-X
     │                   │                  │
     ▼                   ▼                  ▼
Planning Context     Equipment          Detailed Schedule
Service              Data Service       Service
     │                   │                  │
     └──────────── DATENRAUM ──────────────┘
```

Der wesentliche Implementierungsgedanke lautet damit:

> **Nicht jedes Unternehmen entwickelt eigene Schnittstellen zu allen anderen Unternehmen. Stattdessen werden Fachsysteme über wiederverwendbare Converter auf Construct-X abgebildet. Unternehmensspezifisch entwickelt werden nur die Dienste, die die jeweilige fachliche Rolle im Prozess abbilden.**

Dadurch entsteht aus Construct-X nicht nur ein gemeinsames Ontologiemodell, sondern ein **wiederverwendbares Ökosystem aus semantischen Modellen, Validatoren und Converter-Services**, das für weitere Unternehmen und Projekte wiederverwendet werden kann.
