# Beispiel Use Case für die Nutzung der Ontologien

# Problemstellung

Ein Generalunternehmer erstellt den übergeordneten Rahmenterminplan für ein Bauprojekt. Darin werden die wesentlichen Bauaktivitäten, ihre zeitlichen Abhängigkeiten sowie ihre Zuordnung zu Arbeits- und Ortsstrukturen festgelegt.

Bestimmte Arbeiten werden durch einen Nachunternehmer ausgeführt. Der Generalunternehmer gibt hierfür ausgewählte Rahmenaktivitäten einschließlich der relevanten zeitlichen und räumlichen Randbedingungen an den Nachunternehmer weiter. Der Nachunternehmer detailliert diese Aktivitäten in seiner eigenen Fein- bzw. Taktplanung.

Für die Ausführung benötigt der Nachunternehmer zusätzlich Informationen über die Baustellenlogistik. Ein Baulogistikdienstleister stellt beispielsweise Geräte und Einrichtungen wie einen Bauaufzug bereit. Der Generalunternehmer legt fest, welche dieser Ressourcen für die jeweiligen Arbeiten zur Verfügung stehen.

Der Nachunternehmer berücksichtigt die bereitgestellten Termine, Orte und Baustellenressourcen in seiner Detailplanung. Anschließend übergibt er die verfeinerte Planung an den Generalunternehmer zurück. Dieser integriert sie in den übergeordneten Rahmenterminplan.

# Herausforderung

Die beteiligten Unternehmen arbeiten in der Regel mit unterschiedlichen Fachanwendungen und eigenen Datenstrukturen. Der Generalunternehmer plant beispielsweise in einem Terminplanungswerkzeug, der Nachunternehmer nutzt ein anderes System für die Fein- oder Taktplanung und der Baulogistikdienstleister verwaltet seine Geräte- und Verfügbarkeitsdaten wiederum in eigenen Anwendungen.

Dadurch müssen relevante Informationen heute häufig manuell zusammengestellt, exportiert, per Datei übertragen und im Zielsystem erneut interpretiert werden. Dabei entstehen Medienbrüche, unterschiedliche Datenstände und zusätzlicher Abstimmungsaufwand.

Besonders problematisch ist, dass fachlich zusammengehörige Informationen in verschiedenen Systemen liegen. Eine Aktivität aus dem Terminplan muss beispielsweise mit ihrem Ausführungsort, der zugehörigen Arbeitsstruktur und den dort verfügbaren Baustellenressourcen in Beziehung gesetzt werden.

Für einen durchgängigen digitalen Prozess müssen daher nicht nur Daten übertragen werden. Es muss auch eindeutig beschrieben sein, welche Bedeutung die Daten haben, wie sie miteinander zusammenhängen und unter welchen Bedingungen sie von den beteiligten Unternehmen genutzt werden dürfen.

# **Zielstellung**

Ziel ist ein durchgängiger digitaler Informationsaustausch zwischen den beteiligten Unternehmen, ohne dass diese ihre jeweiligen Fachanwendungen aufgeben müssen.

Die Informationen verbleiben zunächst in den Systemen der Unternehmen. Für den Austausch werden nur die jeweils benötigten Daten bereitgestellt. Diese werden in eine gemeinsame, eindeutig beschriebene Struktur überführt, sodass ihre Bedeutung unabhängig vom ursprünglichen Fachsystem verstanden werden kann.

Der Generalunternehmer stellt dem Nachunternehmer beispielsweise nur die für dessen Arbeiten relevanten Aktivitäten, Orte und Baustellenressourcen zur Verfügung. Informationen eines Baulogistikdienstleisters können dabei einbezogen werden, sofern ihre Nutzung und Weitergabe entsprechend vereinbart ist.

Der Nachunternehmer erhält damit einen konsistenten Planungskontext, den er in seiner eigenen Anwendung weiterverarbeiten kann. Seine verfeinerte Planung wird anschließend in strukturierter Form an den Generalunternehmer zurückgegeben.

Das Zielbild basiert damit auf drei Grundprinzipien:

1. **Gemeinsame Semantik:** Die ausgetauschten Daten besitzen eine einheitlich beschriebene Bedeutung und können systemübergreifend interpretiert werden.
2. **Gezielte Datenbereitstellung:** Es werden nur die für den jeweiligen Anwendungsfall erforderlichen Informationen bereitgestellt.
3. **Kontrollierte Datennutzung:** Es ist festgelegt, welcher Teilnehmer welche Daten zu welchem Zweck verwenden darf.

Dadurch entsteht ein organisations- und systemübergreifender Prozess, bei dem die beteiligten Unternehmen weiterhin ihre eigenen Anwendungen nutzen, die relevanten Informationen jedoch eindeutig, nachvollziehbar und automatisiert austauschen können.

# Rolle der Ontologien

Die Ontologien bilden die gemeinsame fachliche Sprache für den Datenaustausch. Sie beschreiben nicht, in welchem Softwaresystem Informationen gespeichert sind, sondern welche fachliche Bedeutung einzelne Daten besitzen und wie sie miteinander zusammenhängen.

Für das Beispiel werden mehrere fachliche Sichten miteinander verknüpft:

- Die **Terminplanungsontologie** beschreibt Terminpläne, Aktivitäten, Meilensteine und Anordnungsbeziehungen.
- Die **Breakdown-Structure-Ontologie** beschreibt Arbeits- und Ortsstrukturen, beispielsweise WBS- und LBS-Knoten.
- Die **Construction-Site-Ontologie** beschreibt Baustellenbereiche, Baustelleneinrichtung und verfügbares Equipment.

Dadurch kann beispielsweise eine Aktivität nicht nur über ihren Namen und ihre Termine beschrieben werden. Sie kann zusätzlich mit dem zugehörigen Arbeitspaket, ihrem Ausführungsort und den dort verfügbaren Baustellenressourcen verknüpft werden.

Die Ontologien ermöglichen es damit, Informationen aus unterschiedlichen Fachsystemen zu einem gemeinsamen Planungskontext zusammenzuführen.

Ein Nachunternehmer erhält beispielsweise nicht nur die Information, dass eine Aktivität in einem bestimmten Zeitraum auszuführen ist. Er kann zusätzlich automatisiert erkennen:

- wo die Aktivität ausgeführt wird,
- welcher Arbeitsstruktur sie zugeordnet ist,
- welche Baustellenbereiche relevant sind,
- welches Equipment für die Ausführung zur Verfügung steht.

Die Ontologien dienen damit als **kanonisches Austauschmodell** zwischen den beteiligten Anwendungen. Jedes Unternehmen muss lediglich seine eigenen Systemdaten in dieses gemeinsame Modell überführen bzw. daraus wieder in das eigene Fachsystem transformieren.

Dadurch wird vermieden, dass für jede Kombination von zwei Fachsystemen eine individuelle Schnittstelle entwickelt werden muss.

# Rolle des Datenraums

Die Ontologien sorgen dafür, dass die ausgetauschten Informationen fachlich eindeutig beschrieben werden können. Sie legen jedoch nicht fest, **wer auf welche Daten zugreifen darf und unter welchen Bedingungen diese genutzt werden dürfen**. Diese Aufgabe übernimmt der Datenraum.

Der Datenraum bildet die vertrauenswürdige Infrastruktur für den organisationsübergreifenden Datenaustausch. Die beteiligten Unternehmen behalten dabei die Kontrolle über ihre eigenen Daten und Systeme. Es entsteht kein zentrales gemeinsames Projektsystem, in das alle Daten dauerhaft übertragen werden müssen.

Für den beschriebenen Anwendungsfall übernimmt der Datenraum insbesondere vier Aufgaben:

1. **Teilnehmer eindeutig identifizieren**  
Der Datenraum stellt sicher, dass Generalunternehmer, Nachunternehmer und Baulogistikdienstleister eindeutig identifiziert werden können. Zusätzlich können Rollen und Projektzugehörigkeiten berücksichtigt werden.
2. **Datenangebote bekannt machen**  
Ein Unternehmen kann beschreiben, welche Daten oder Datendienste es bereitstellen kann. Der Generalunternehmer kann beispielsweise einen „Planning Context“ für den Nachunternehmer anbieten. Die eigentlichen Daten müssen zu diesem Zeitpunkt noch nicht erzeugt oder übertragen werden.
3. **Zugriff und Nutzung regeln**  
Über Policies wird festgelegt, wer ein Datenangebot nutzen darf und für welchen Zweck. Beispielsweise kann der Nachunternehmer berechtigt werden, bestimmte Planungsdaten ausschließlich für die Detailplanung im Projekt zu verwenden.
4. **Datentransfer kontrolliert ausführen**  
Erst wenn der Zugriff zulässig ist, werden die benötigten Daten bereitgestellt und übertragen. Der Datenraum koordiniert diesen Austausch und stellt sicher, dass nur autorisierte Datenflüsse stattfinden.

Für das Beispiel ergibt sich damit folgender vereinfachter Ablauf:

```
Generalunternehmer
    │
    │ veröffentlicht Datenangebot
    ▼
Datenraum
    │
    │ prüft Identität,
    │ Rolle und Nutzungsbedingungen
    ▼
Nachunternehmer
    │
    │ fordert Daten an
    ▼
Datenraum
    │
    │ Zugriff erlaubt
    ▼
Generalunternehmer
    │
    │ stellt die benötigten Daten
    │ erst jetzt zusammen
    ▼
Nachunternehmer
```

Besonders wichtig ist, dass **Datenangebot und Datenbereitstellung voneinander getrennt sind**.

Der Generalunternehmer kann beispielsweise dauerhaft anbieten:

```
Planning Context
für Nachunternehmer
im Projekt X
```

Die konkreten Daten werden jedoch erst erzeugt, wenn ein berechtigter Nachunternehmer darauf zugreift. Zu diesem Zeitpunkt können aktuelle Informationen aus Terminplanung, WBS/LBS, Baustellenorganisation und weiteren Datenquellen zusammengestellt werden.

Damit können immer die zum Zeitpunkt des Zugriffs relevanten Daten verwendet werden.

## Einbindung von Daten Dritter

Der Datenraum ermöglicht außerdem, Daten mehrerer Unternehmen kontrolliert zusammenzuführen.

Ein Baulogistikdienstleister kann beispielsweise Daten zu einem Bauaufzug bereitstellen. Der Generalunternehmer besitzt aufgrund einer Datennutzungsvereinbarung das Recht, bestimmte Informationen über diesen Bauaufzug für die Projektplanung zu verwenden und an berechtigte Projektpartner weiterzugeben.

Der Nachunternehmer muss in diesem Fall nicht unmittelbar mit dem Baulogistikdienstleister Daten austauschen.

Vereinfacht:

```
Baulogistikdienstleister
        │
        │ stellt Equipment-Daten bereit
        │ und erlaubt definierte Weiterverwendung
        ▼
Generalunternehmer
        │
        │ kombiniert
        │
        ├─ Terminplandaten
        ├─ WBS/LBS
        ├─ Baustelleninformationen
        └─ freigegebene Equipment-Daten
        │
        ▼
gemeinsamer Planungskontext
        │
        ▼
Nachunternehmer
```

Der Generalunternehmer fungiert damit als **autorisierter Integrator** verschiedener Informationsquellen.

Die Herkunft der einzelnen Informationen bleibt weiterhin nachvollziehbar. So kann beispielsweise kenntlich gemacht werden, dass die Informationen zum Bauaufzug ursprünglich vom Baulogistikdienstleister stammen.

## Zusammenspiel von Datenraum und Ontologien

Datenraum und Ontologien erfüllen damit unterschiedliche, aber komplementäre Aufgaben:

```
ONTOLOGIEN
beschreiben:
Was bedeuten die Daten?
Wie hängen die Daten fachlich zusammen?

DATENRAUM
regelt:
Wer darf auf die Daten zugreifen?
Zu welchem Zweck dürfen sie genutzt werden?
Wann und wie werden sie übertragen?
```

Erst durch die Kombination beider Ansätze entsteht ein durchgängiger organisationsübergreifender Datenaustausch:

```
Fachsysteme
     ↓
Ontologien
     ↓
fachlich eindeutige Daten
     ↓
Datenraum
     ↓
kontrollierter Austausch
     ↓
Fachsysteme des Empfängers
```

Der Datenraum ersetzt damit weder die Fachanwendungen noch die Ontologien. Er bildet die **vertrauenswürdige und kontrollierte Austauschschicht zwischen den Unternehmen**.

# Struktur des Gesamtprozesses

Der gesamte Datenaustausch lässt sich in fünf Hauptprozesse gliedern. Dabei wird bewusst zwischen einer vorbereitenden Einrichtungsphase und dem später wiederkehrenden operativen Planungsprozess unterschieden.

Diese Trennung ist wichtig, weil grundlegende Vereinbarungen zur Zusammenarbeit, zu Datenangeboten und zu Nutzungsrechten nicht bei jedem einzelnen Planungsauftrag erneut getroffen werden müssen. Sie werden möglichst zu Beginn eingerichtet und können anschließend für viele konkrete Austauschvorgänge genutzt werden.

## Datenraumbeziehungen und Nutzungsrechte einrichten

Im ersten Schritt werden die organisatorischen und technischen Voraussetzungen für die Zusammenarbeit geschaffen.

Die beteiligten Unternehmen werden im Datenraum eindeutig identifiziert und ihre Rollen festgelegt. Gleichzeitig wird beschrieben, welche Daten oder Datendienste grundsätzlich angeboten werden und unter welchen Bedingungen diese genutzt werden dürfen.

Beispielsweise kann ein Baulogistikdienstleister Informationen zu einem Bauaufzug bereitstellen. In einer Datennutzungsvereinbarung wird festgelegt, dass der Generalunternehmer diese Informationen für das gemeinsame Bauprojekt verwenden und bestimmte Daten auch an berechtigte Nachunternehmer weitergeben darf.

Der Nachunternehmer muss diese grundsätzlichen Nutzungsrechte dann nicht für jeden einzelnen Planungsauftrag erneut mit dem Baulogistikdienstleister vereinbaren.

Am Ende dieses Hauptprozesses ist festgelegt:

- welche Unternehmen am Datenaustausch teilnehmen,
- welche Rollen sie im Projekt besitzen,
- welche Datenangebote vorhanden sind,
- zu welchen Zwecken Daten genutzt werden dürfen,
- ob und unter welchen Bedingungen Daten an weitere Projektpartner weitergegeben werden dürfen.

Diese Einrichtungsphase wird in der Regel nur einmal oder bei Änderungen der Zusammenarbeit erneut durchgeführt.

## Planungsauftrag und Datenumfang festlegen

Der zweite Hauptprozess beginnt mit einem konkreten Planungsbedarf.

Der Generalunternehmer legt fest, welche Aktivitäten seines Rahmenterminplans durch einen Nachunternehmer detailliert werden sollen.

Beispielsweise kann eine übergeordnete Aktivität wie

```
Ausbau 5. Obergeschoss
```

an einen Nachunternehmer zur weiteren Fein- oder Taktplanung übergeben werden.

Zusätzlich wird festgelegt, welche Informationen der Nachunternehmer für seine Planung benötigt.

Dazu können beispielsweise gehören:

- zeitliche Randbedingungen,
- Vorgänger- und Nachfolgeraktivitäten,
- WBS-Zuordnungen,
- LBS-Zuordnungen,
- Baustellenbereiche,
- verfügbare Baustelleneinrichtungen und Geräte.

Der Generalunternehmer definiert damit den fachlichen Umfang des späteren Datenaustauschs.

Wichtig ist, dass zu diesem Zeitpunkt noch kein vollständiges Datenpaket erzeugt werden muss. Es wird zunächst lediglich festgelegt, **welche Informationen bei einem späteren Zugriff bereitgestellt werden sollen**.

## Planungskontext erzeugen und bereitstellen

Der dritte Hauptprozess beginnt, wenn der Nachunternehmer die für ihn vorgesehenen Daten tatsächlich anfordert.

Zunächst wird geprüft, ob der Nachunternehmer für das entsprechende Datenangebot berechtigt ist und ob der angegebene Nutzungszweck zulässig ist.

Erst nach erfolgreicher Prüfung werden die benötigten Informationen aus den verschiedenen Quellsystemen zusammengestellt.

Dazu können beispielsweise gehören:

```
Terminplandaten
+
WBS/LBS
+
Baustelleninformationen
+
freigegebene Equipment-Daten
```

Die Informationen werden mithilfe der Construct-X-Ontologien semantisch miteinander verknüpft.

Dadurch kann aus einer freigegebenen Aktivität beispielsweise automatisch ermittelt werden:

```
Welche Aktivität ist betroffen?
        ↓
Zu welchem Arbeitspaket gehört sie?
        ↓
Wo findet sie statt?
        ↓
Welcher Baustellenbereich ist relevant?
        ↓
Welches Equipment steht dort zur Verfügung?
```

Auch Daten eines Baulogistikdienstleisters können in diesen Planungskontext aufgenommen werden, sofern deren Verwendung und Weitergabe zuvor erlaubt wurde.

Der vollständige Planungskontext wird anschließend geprüft und an den Nachunternehmer übertragen.

## Detailplanung durchführen und freigeben

Der Nachunternehmer übernimmt den bereitgestellten Planungskontext in sein eigenes Fachsystem.

Die übergeordnete Rahmenaktivität des Generalunternehmers wird dort weiter detailliert.

Aus einer Aktivität wie

```
Ausbau 5. Obergeschoss
```

können beispielsweise mehrere Detailaktivitäten entstehen:

```
Unterkonstruktion
Doppelboden
Trennwände
Decke
```

Der Nachunternehmer berücksichtigt dabei die übergebenen zeitlichen und räumlichen Randbedingungen sowie die zur Verfügung stehenden Baustellenressourcen.

Nach Abschluss der Planung werden die neuen Detailaktivitäten wieder in das gemeinsame semantische Austauschmodell überführt.

Dabei bleibt nachvollziehbar, auf welche Rahmenaktivität sich die jeweilige Detailaktivität bezieht.

Die fertige Feinplanung wird anschließend als neues Datenangebot bereitgestellt.

## Detailplanung übernehmen und integrieren

Im letzten Hauptprozess ruft der Generalunternehmer die vom Nachunternehmer bereitgestellte Feinplanung ab.

Auch dieser Datenaustausch erfolgt kontrolliert über den Datenraum.

Die empfangenen Daten werden zunächst formal und fachlich geprüft.

Beispielsweise kann überprüft werden:

- ob alle Detailaktivitäten einer freigegebenen Rahmenaktivität zugeordnet sind,
- ob die verwendeten Daten auf dem richtigen Planungskontext basieren,
- ob die zeitlichen und räumlichen Zuordnungen plausibel sind,
- ob die Daten den vereinbarten semantischen Strukturen entsprechen.

Anschließend werden die Detailaktivitäten in das Terminplanungssystem des Generalunternehmers übernommen.

Der ursprüngliche Rahmenterminplan bleibt dabei bestehen. Die vom Nachunternehmer erzeugten Detailaktivitäten werden darunter eingeordnet.

Damit entsteht ein durchgängiger Planungsprozess:

```
Rahmenterminplan
        ↓
Planungsauftrag
        ↓
Planungskontext
        ↓
Detailplanung
        ↓
Rückgabe
        ↓
integrierter Terminplan
```

## Zusammenfassung

Die fünf Hauptprozesse können damit wie folgt zusammengefasst werden:

```
1. Datenraumbeziehungen und Nutzungsrechte einrichten
        ↓
2. Planungsauftrag und Datenumfang festlegen
        ↓
3. Planungskontext erzeugen und bereitstellen
        ↓
4. Detailplanung durchführen und freigeben
        ↓
5. Detailplanung übernehmen und integrieren
```

Der erste Hauptprozess schafft die langfristigen Voraussetzungen für die Zusammenarbeit.

Die Hauptprozesse 2 bis 5 bilden den eigentlichen operativen Planungszyklus und können für unterschiedliche Aktivitäten, Nachunternehmer und Planungsaufgaben beliebig oft wiederholt werden.

# Hauptprozess 1 – Datenbeziehungen und semantische Grundlagen einrichten

Bevor konkrete Planungsdaten ausgetauscht werden können, müssen die drei beteiligten Unternehmen festlegen, **welche Informationen sie bereitstellen, wie diese Informationen semantisch beschrieben werden und unter welchen Bedingungen sie von anderen Projektpartnern genutzt werden dürfen**.

In dieser Phase werden noch keine konkreten Rahmenaktivitäten oder Detailpläne ausgetauscht. Stattdessen werden die Voraussetzungen dafür geschaffen, dass die Daten später automatisiert zusammengestellt, verstanden und verarbeitet werden können.

Die drei beteiligten Rollen sind:

- **Generalunternehmer**
- **Baulogistikdienstleister**
- **Nachunternehmer**

Für alle drei Teilnehmer gilt dasselbe Grundprinzip:

```
eigenes Fachsystem
      ↓
Adapter / Converter
      ↓
Construct-X Ontologien
      ↓
semantisch beschriebene Daten
      ↓
Datenraum
```

Die Construct-X-Ontologien bilden damit die gemeinsame fachliche Sprache zwischen den unterschiedlichen Systemen.

---

## Gemeinsame semantische Grundlage festlegen

Zu Beginn müssen die beteiligten Unternehmen festlegen, welche Construct-X-Ontologien für den Datenaustausch verwendet werden.

Für das vorliegende Szenario werden insbesondere benötigt:

```
Construction Schedule Ontology
        ↓
Terminpläne und Aktivitäten

Breakdown Structure Ontology
        ↓
WBS und LBS

Construction Site Ontology
        ↓
Baustellenbereiche und Equipment

Link Ontologies
        ↓
Verknüpfung der fachlichen Sichten
```

Dadurch können Daten aus unterschiedlichen Systemen miteinander verbunden werden.

Beispielsweise:

```
Activity
   │
   ├── isClassifiedByWBSNode
   │             ↓
   │          WBSNode
   │
   └── isPerformedIn
                 ↓
              LBSNode
                 ↑
                 │ isRepresentedByLBSNode
              SiteArea
                 ↑
                 │ usesSiteArea
              SiteEquipment
```

Damit ist fachlich eindeutig beschrieben:

> Eine Aktivität gehört zu einem Arbeitspaket, findet an einem bestimmten Ort statt und kann mit dort vorhandenen Baustellenressourcen verbunden werden.

Diese Beziehungen sind unabhängig davon, in welchem Softwareprodukt die Informationen ursprünglich gespeichert sind.

---

## Aufgaben des Generalunternehmers

Der Generalunternehmer besitzt mehrere Datenquellen, die später zu einem gemeinsamen Planungskontext zusammengeführt werden sollen.

Typische Systeme sind:

```
Microsoft Project
→ Terminplanung

WBS/LBS-System
→ Arbeits- und Ortsstruktur

Baustellen-/BE-System
→ Baustellenbereiche und Baustelleneinrichtung
```

Der Generalunternehmer muss für diese Systeme festlegen, wie deren Daten auf Construct-X abgebildet werden.

---

### Terminplandaten auf Construct-X abbilden

Die Informationen aus Microsoft Project werden auf die **Construction Schedule Ontology** abgebildet.

Beispielsweise:

```
Microsoft Project Task
        ↓
conx:Activity
```

Dabei werden insbesondere folgende Informationen benötigt:

```
Activity
├── identifier
├── name
├── description
├── plannedStart
├── plannedFinish
└── PrecedenceRelationships
```

Der Generalunternehmer benötigt dafür einen:

```
MS Project → Construct-X Converter
```

Für den späteren Rückweg wird zusätzlich benötigt:

```
Construct-X → MS Project Converter
```

---

### WBS und LBS abbilden

Die vorhandene Projektgliederung wird auf die **Breakdown Structure Ontology** abgebildet.

Beispielsweise:

```
interner WBS-Knoten
        ↓
WBSNode

interner Ortsknoten
        ↓
LBSNode
```

Der Generalunternehmer muss dabei sicherstellen, dass die Identitäten der Knoten stabil bleiben.

Beispielsweise:

```
WBS-03
Innenausbau

LBS-05
5. Obergeschoss
```

Die Terminplanaktivitäten werden anschließend über die Link-Ontologie mit diesen Strukturen verbunden:

```
Activity
    ── isClassifiedByWBSNode ──► WBSNode

Activity
    ── isPerformedIn ──────────► LBSNode
```

Damit wird aus einem reinen Terminplan ein räumlich und organisatorisch interpretierbarer Terminplan.

---

### Baustelleninformationen abbilden

Der Generalunternehmer beschreibt seine Baustellenbereiche und die von ihm verwalteten Baustelleneinrichtungen mit der **Construction Site Ontology**.

Beispielsweise:

```
Arbeitsbereich 5. OG
        ↓
SiteArea

Bauaufzug
        ↓
SiteEquipment
```

Ein Baustellenbereich kann mit einem LBS-Knoten verbunden werden:

```
SiteArea
    ── isRepresentedByLBSNode ──► LBSNode
```

Dadurch kann später ausgehend von einer Activity ermittelt werden, welcher Baustellenbereich relevant ist.

---

### Semantische Integrationsschicht vorbereiten

Der Generalunternehmer benötigt damit eine Integrationsschicht:

```
Microsoft Project ───┐
                     │
WBS/LBS-System ──────┼──► Construct-X Graph
                     │
Site-System ─────────┘
```

Diese Schicht muss insbesondere:

- Daten aus den Quellsystemen lesen,
- interne Identifikatoren auf stabile IRIs abbilden,
- Construct-X-Klassen und Properties erzeugen,
- Beziehungen zwischen den Ontologien herstellen,
- die erzeugten Daten mit SHACL prüfen.

Der Generalunternehmer ist damit derjenige Teilnehmer, der später den vollständigen **Planning Context** erzeugt.

---

## Aufgaben des Baulogistikdienstleisters

Der Baulogistikdienstleister stellt beispielsweise einen Bauaufzug bereit.

Die Informationen darüber liegen zunächst im eigenen System des Baulogistikdienstleisters.

Beispielsweise:

```
interne Equipment-ID:
ZEP-LIFT-4711

Typ:
Bauaufzug

Projekt:
Project-X

Status:
verfügbar
```

Diese Informationen müssen ebenfalls auf das gemeinsame Construct-X-Modell abgebildet werden.

---

### Equipment semantisch beschreiben

Der Bauaufzug wird als `SiteEquipment` beschrieben.

Beispielsweise:

```
Bauaufzug 1
        ↓
SiteEquipment
```

mit einem kontrollierten Equipment-Typ:

```
hasEquipmentType
        ↓
ConstructionLift
```

Damit verwendet der Baulogistikdienstleister dieselbe fachliche Bedeutung wie der Generalunternehmer.

Es wird also nicht lediglich übertragen:

```
"Gerät 4711"
```

sondern beispielsweise:

```
SiteEquipment
identifier = ZEP-LIFT-4711
name = Bauaufzug 1
equipmentType = ConstructionLift
```

---

### Eigene Identität des Equipments erhalten

Der Baulogistikdienstleister bleibt verantwortlich für die Identität seiner Daten.

Deshalb sollte das Equipment eine IRI aus dem Namensraum des Baulogistikdienstleisters erhalten.

Beispielsweise:

```
https://data.logistics-provider.example/
equipment/ZEP-LIFT-4711
```

Der Generalunternehmer erzeugt für denselben Bauaufzug keine neue unabhängige Identität.

Er referenziert die vom Baulogistikdienstleister bereitgestellte Ressource.

Damit bleibt eindeutig:

```
Datenquelle des Bauaufzugs
        =
Baulogistikdienstleister
```

---

### Daten für Construct-X bereitstellen

Der Baulogistikdienstleister benötigt einen Adapter zwischen seinem Equipment-System und Construct-X:

```
Equipment Management System
        ↓
Construct-X Adapter
        ↓
Construction Site Ontology
```

Dieser Adapter muss nur das eigene Fachsystem kennen.

Er muss weder Microsoft Project noch Metronom kennen.

Das ist ein wichtiger Vorteil des gemeinsamen Ontologiemodells.

---

### Nutzungs- und Weitergaberechte festlegen

Zusätzlich muss der Baulogistikdienstleister festlegen, wie seine Daten genutzt werden dürfen.

Für das Szenario wird beispielsweise vereinbart:

```
Generalunternehmer darf:

✓ Bauaufzugsdaten verwenden
✓ für Project-X nutzen
✓ in einen Planning Context integrieren
✓ definierte Informationen an
  berechtigte Nachunternehmer weitergeben
```

Damit kann der Generalunternehmer später Equipment-Daten in seinen Planning Context integrieren.

Der Nachunternehmer muss nicht selbst eine separate Datenbeziehung mit dem Baulogistikdienstleister aufbauen.

---

## Aufgaben des Nachunternehmers

Der Nachunternehmer arbeitet in seinem eigenen Planungssystem, beispielsweise mit einer Taktplanungssoftware.

Für ihn muss zunächst sichergestellt werden, dass sein System Construct-X-Daten verarbeiten kann.

---

### Construct-X in das eigene Planungssystem importieren

Der Nachunternehmer benötigt einen:

```
Construct-X → Taktplanungssystem Converter
```

Dieser übersetzt beispielsweise:

```
Construct-X Activity
        ↓
Planungsaktivität

LBSNode
        ↓
Planungsbereich / Taktbereich

plannedStart
plannedFinish
        ↓
zeitliche Randbedingungen
```

Auch Informationen zu Baustellenbereichen und Equipment können auf diese Weise in der Planungsanwendung verfügbar gemacht werden.

---

### Construct-X für den Rückweg erzeugen

Nach Abschluss der Feinplanung benötigt der Nachunternehmer auch den umgekehrten Converter:

```
Taktplanungssystem
        ↓
Taktplanungssystem → Construct-X Converter
        ↓
Construction Schedule Ontology
```

Neue Aktivitäten erhalten eigene Identitäten aus dem Namensraum des Nachunternehmers.

Beispielsweise:

```
https://data.subcontractor.example/
activity/LIN-A100-01
```

Die Beziehung zur Aktivität des Generalunternehmers wird anschließend explizit beschrieben:

```
DetailActivity
    ── isSubActivityOf ──►
FrameworkActivity
```

Damit bleiben Verantwortlichkeiten und Herkunft eindeutig.

---

## Gemeinsame Vokabulare verwenden

Neben den Ontologien müssen die Teilnehmer auch dieselben kontrollierten Vokabulare verwenden.

Beispielsweise:

```
Construction Site Equipment Type

ConstructionLift
Crane
Forklift
...
```

Dadurch wird verhindert, dass unterschiedliche Systeme beispielsweise folgende Begriffe verwenden:

```
Bauaufzug
Construction Lift
Lift
Material Hoist
```

ohne zu wissen, ob damit fachlich dasselbe gemeint ist.

Ein Construct-X Concept besitzt deshalb eine stabile IRI:

```
.../equipment-type#ConstructionLift
```

Unterschiedliche Bezeichnungen können über SKOS als Synonyme hinterlegt werden.

---

## Unterschiedliche externe Vokabulare abbilden

Wenn ein Unternehmen bereits ein eigenes Vokabular verwendet, muss dieses nicht ersetzt werden.

Es kann auf Construct-X gemappt werden.

Beispielsweise:

```
Baulogistikdienstleister:

internal:MaterialHoist

        │
        │ skos:exactMatch
        ▼

Construct-X:
ConstructionLift
```

Damit kann jedes Unternehmen intern weiterhin seine vorhandenen Begriffe verwenden.

Construct-X bildet die gemeinsame Austauschsemantik.

---

## SHACL-Profile vereinbaren

Zusätzlich zu den Ontologien müssen die Teilnehmer wissen, welche Daten für einen konkreten Austausch mindestens vorhanden sein müssen.

Dafür werden gemeinsame SHACL-Profile verwendet.

Beispielsweise kann für einen Planning Context verlangt werden:

```
Activity
✓ identifier
✓ name
✓ plannedStart
✓ plannedFinish

Activity
✓ LBS-Verknüpfung

SiteArea
✓ areaType

SiteEquipment
✓ identifier
✓ equipmentType
```

Damit kann jeder Teilnehmer automatisch prüfen:

> Sind die Daten strukturell vollständig und entsprechen sie dem vereinbarten Construct-X-Profil?

---

## Ontologie- und Profilversionen festlegen

Alle Teilnehmer müssen dieselben bzw. kompatible Versionen der semantischen Modelle verwenden.

Beispielsweise:

```
Construction Schedule 0.5.0
Breakdown Structure 0.7.0
Construction Site 0.1.0
```

Ein Datenangebot sollte deshalb angeben:

```
conformsTo:
Construction Schedule 0.5.0
Breakdown Structure 0.7.0
Construction Site 0.1.0
```

Dadurch weiß der Empfänger bereits vor dem Abruf, welches semantische Modell er verarbeiten können muss.

---

## Welche Datenraumfunktionen werden zusätzlich benötigt?

Die eigentlichen Datenraumdienste können für diesen Hauptprozess relativ kompakt beschrieben werden.

Benötigt werden im Wesentlichen:

```
Identity
    ↓
Wer ist der Teilnehmer?

Catalog
    ↓
Welche Daten oder Dienste werden angeboten?

Policy / Agreement
    ↓
Wer darf sie wofür verwenden?

Transfer
    ↓
Wie werden die Daten übertragen?
```

Die Datenraumdienste beschreiben also **nicht die fachliche Bedeutung der Informationen**.

Diese Aufgabe übernehmen die Construct-X-Ontologien.

Die Aufgabenteilung lautet:

```
DATENRAUM

Wer darf welche Daten
unter welchen Bedingungen nutzen?


CONSTRUCT-X ONTOLOGIEN

Was bedeuten die Daten
und wie hängen sie fachlich zusammen?
```

---

## Was müssen die drei Teilnehmer am Ende eingerichtet haben?

### Generalunternehmer

Der Generalunternehmer benötigt:

```
MS Project Adapter
WBS/LBS Adapter
Site Adapter
        ↓
Construct-X Converter
        ↓
Semantic Graph Builder
        ↓
SHACL Validator
        ↓
Planning Context Service
```

Zusätzlich kennt er die Nutzungsrechte externer Daten, beispielsweise des Baulogistikdienstleisters.

---

### Baulogistikdienstleister

Der Baulogistikdienstleister benötigt:

```
Equipment-System
        ↓
Construct-X Adapter
        ↓
Construction Site Ontology
        ↓
Equipment Data Service
```

Zusätzlich definiert er, unter welchen Bedingungen der Generalunternehmer diese Daten verwenden und weitergeben darf.

---

### Nachunternehmer

Der Nachunternehmer benötigt:

```
Construct-X Planning Context
        ↓
Converter
        ↓
Taktplanungssystem

und für den Rückweg:

Taktplanungssystem
        ↓
Converter
        ↓
Construct-X Detail Schedule
```

---

## Ergebnis von Hauptprozess 1

Nach Abschluss dieses Hauptprozesses können sich die drei Teilnehmer semantisch verstehen.

Die Situation ist dann:

```
BAULOGISTIKDIENSTLEISTER
Equipment-System
      │
      ▼
Construct-X Equipment Data
      │
      │ Nutzung durch Generalunternehmer erlaubt
      ▼

GENERALUNTERNEHMER
MS Project + WBS/LBS + Site Data
      │
      ▼
Construct-X Semantic Integration
      │
      ▼
Planning Context Service
      │
      │ Nutzung durch Nachunternehmer erlaubt
      ▼

NACHUNTERNEHMER
Construct-X Adapter
      │
      ▼
Taktplanungssystem
```

Zu diesem Zeitpunkt wurden noch keine konkreten Aktivitäten ausgetauscht.

Aber es ist festgelegt:

- wie Terminplandaten semantisch beschrieben werden,
- wie WBS und LBS beschrieben werden,
- wie Baustellenbereiche und Equipment beschrieben werden,
- wie diese Informationen miteinander verknüpft werden,
- welche Vokabulare verwendet werden,
- welche SHACL-Profile gelten,
- welche Teilnehmer die Daten nutzen dürfen,
- welche Daten des Baulogistikdienstleisters weiterverwendet werden dürfen.

Damit ist die technische und semantische Grundlage geschaffen, um anschließend einen konkreten Planungsauftrag zu definieren.

# Hauptprozess 2 – Planungsauftrag und Datenumfang festlegen

Nachdem die grundsätzlichen Datenbeziehungen, semantischen Modelle und Nutzungsrechte eingerichtet sind, wird im zweiten Hauptprozess ein **konkreter Planungsauftrag** vorbereitet.

Der Generalunternehmer legt fest,

- welche Rahmenaktivitäten durch den Nachunternehmer detailliert werden sollen,
- welche weiteren Aktivitäten nur als Kontext benötigt werden,
- welche räumlichen und organisatorischen Informationen benötigt werden,
- welche Baustellenressourcen für die Planung relevant sind.

In diesem Hauptprozess werden die benötigten Daten **fachlich ausgewählt und beschrieben**. Der eigentliche Planungskontext muss jedoch noch nicht erzeugt werden. Dies erfolgt erst beim späteren Zugriff durch den Nachunternehmer.

Der Hauptprozess beantwortet damit im Wesentlichen die Frage:

> **Was soll der Nachunternehmer planen und welche Informationen benötigt er dafür?**

---

## Ausgangssituation

Der Generalunternehmer besitzt einen übergeordneten Rahmenterminplan.

Beispielsweise:

```
A090   Rohbau 5. OG fertig
A100   Ausbau 5. OG
A110   Ausbau 6. OG
A120   Übergabe 5. OG
```

Der Generalunternehmer entscheidet, dass der Nachunternehmer die Aktivität

```
A100 Ausbau 5. OG
```

im Detail planen soll.

Diese Aktivität wird damit Bestandteil eines konkreten Planungsauftrags.

---

## Aufgaben des Generalunternehmers

Der Generalunternehmer ist in diesem Hauptprozess der zentrale Akteur.

Er definiert den fachlichen Umfang des Datenaustauschs.

---

### Zu detaillierende Rahmenaktivitäten auswählen

Zunächst werden die Aktivitäten festgelegt, die der Nachunternehmer weiter detaillieren darf.

Beispielsweise:

```
delegatedActivities

A100 Ausbau 5. OG
```

Die Aktivität bleibt weiterhin eine Aktivität des Generalunternehmers.

Der Nachunternehmer erhält lediglich den Auftrag, darunter eigene Detailaktivitäten zu planen.

Semantisch handelt es sich weiterhin um eine Instanz der Construct-X `Activity`:

```
A100
    a Activity
```

Später können die vom Nachunternehmer erzeugten Aktivitäten darauf verweisen:

```
DetailActivity
    isSubActivityOf
    A100
```

Damit bleibt die Verantwortung für die Rahmenaktivität eindeutig beim Generalunternehmer.

---

### Kontextaktivitäten festlegen

Für die Detailplanung reicht die einzelne Rahmenaktivität häufig nicht aus.

Der Nachunternehmer muss beispielsweise wissen, was vorher abgeschlossen sein muss oder welcher Folgetermin einzuhalten ist.

Deshalb kann der Generalunternehmer zusätzliche Aktivitäten als reine Kontextinformationen festlegen.

Beispiel:

```
delegatedActivity

A100 Ausbau 5. OG


contextActivities

A090 Rohbau 5. OG fertig
A120 Übergabe 5. OG
```

Der Unterschied ist wichtig:

```
delegatedActivity
→ darf durch den Nachunternehmer detailliert werden

contextActivity
→ dient nur als Randbedingung
```

Beide sind fachlich `Activity`-Instanzen der Construction Schedule Ontology.

Die Unterscheidung zwischen `delegated` und `context` sollte jedoch **nicht dauerhaft als Eigenschaft der Activity selbst modelliert werden**.

Sie gehört zum konkreten Planungsauftrag.

Eine Aktivität kann beispielsweise in einem Austausch delegiert und in einem anderen Austausch lediglich Kontext sein.

---

## Zeitlichen Planungskontext festlegen

Für die ausgewählten Aktivitäten werden die relevanten Terminplaninformationen bestimmt.

Die **Construction Schedule Ontology** beschreibt beispielsweise:

```
Activity
├── identifier
├── name
├── description
├── plannedStart
├── plannedFinish
└── PrecedenceRelationships
```

Der Generalunternehmer legt fest, welche dieser Informationen für den Planungsauftrag benötigt werden.

Für den einfachen Anwendungsfall können dies sein:

```
Rahmenaktivität
+
Starttermin
+
Endtermin
+
relevante Vorgänger
+
relevante Nachfolger
```

Damit erhält der Nachunternehmer später einen zeitlich abgegrenzten Planungskorridor.

Beispielsweise:

```
A100 Ausbau 5. OG

Start:
02.11.2026

Ende:
27.11.2026
```

Die Feinplanung muss sich innerhalb dieses Rahmens bewegen, sofern keine andere Vereinbarung getroffen wird.

---

## WBS-Kontext bestimmen

Der Generalunternehmer legt zusätzlich fest, zu welchem Arbeitspaket die Aktivität gehört.

Über die Link-Ontologie kann die Beziehung beschrieben werden:

```
Activity
    ── isClassifiedByWBSNode ──►
WBSNode
```

Beispielsweise:

```
A100 Ausbau 5. OG
        │
        └── WBS
             ↓
        03 Innenausbau
```

Damit weiß der Nachunternehmer später nicht nur, **wann** eine Aktivität stattfindet, sondern auch, welchem fachlichen Arbeitspaket sie zugeordnet ist.

---

## Räumlichen Kontext über die LBS bestimmen

Für die Feinplanung ist insbesondere relevant, **wo** die Arbeit ausgeführt werden soll.

Der Generalunternehmer ordnet deshalb die Aktivität einem LBS-Knoten zu.

Semantisch:

```
Activity
    ── isPerformedIn ──►
LBSNode
```

Beispielsweise:

```
A100 Ausbau 5. OG
        │
        └── isPerformedIn
                  ↓
             LBS-05
             5. Obergeschoss
```

Diese Beziehung ist besonders wichtig, weil sie später als Ausgangspunkt für die Ermittlung weiterer räumlicher Kontextinformationen genutzt werden kann.

---

## Benötigte Baustelleninformationen festlegen

Aus der räumlichen Zuordnung kann anschließend bestimmt werden, welche Baustellenbereiche für die Planung relevant sind.

Über die vorhandenen Ontologien kann beispielsweise folgende Verbindung genutzt werden:

```
Activity
      ↓
LBSNode
      ↑
SiteArea
```

genauer:

```
Activity
    ── isPerformedIn ─────────────► LBSNode

SiteArea
    ── isRepresentedByLBSNode ────► LBSNode
```

Dadurch kann festgelegt werden:

> Für die Aktivität sollen beim späteren Abruf alle relevanten Baustellenbereiche berücksichtigt werden, die dem entsprechenden LBS-Knoten zugeordnet sind.

Der Generalunternehmer muss damit nicht notwendigerweise bereits konkrete SiteAreas manuell auswählen.

Er kann vielmehr eine **semantische Auswahlregel** definieren.

---

## Relevantes Equipment festlegen

Für bestimmte Aktivitäten werden zusätzlich Baustellenressourcen benötigt.

Beispielsweise benötigt der Nachunternehmer für Arbeiten im 5. Obergeschoss einen Bauaufzug.

Der Zusammenhang kann über die Construction Site Ontology bestimmt werden:

```
SiteEquipment
      │
      │ usesSiteArea
      ▼
SiteArea
```

Zusammen mit der räumlichen Aktivitätszuordnung ergibt sich:

```
Activity
   ↓
LBSNode
   ↑
SiteArea
   ↑
SiteEquipment
```

Damit kann für den Planungsauftrag beispielsweise definiert werden:

> Beim späteren Aufbau des Planning Context sollen alle für den relevanten Baustellenbereich verfügbaren `SiteEquipment`-Ressourcen berücksichtigt werden.

Oder enger:

> Es sollen nur Ressourcen vom Typ `ConstructionLift` berücksichtigt werden.

Damit kann der Planungsauftrag bereits fachlich beschreiben:

```
Required Context:
SiteEquipment

EquipmentType:
ConstructionLift
```

ohne dass der aktuelle Bauaufzug bereits aus dem System des Baulogistikdienstleisters abgerufen werden muss.

---

## Rolle des Baulogistikdienstleisters

Der Baulogistikdienstleister hat in diesem Hauptprozess nur eine begrenzte aktive Rolle.

Die grundsätzlichen Datenangebote und Nutzungsrechte wurden bereits in Hauptprozess 1 vereinbart.

Der Generalunternehmer nutzt nun diese vorhandenen Informationen, um festzustellen:

```
Für den Planungsauftrag wird
ein ConstructionLift benötigt.

Für ConstructionLift-Daten existiert
ein zugelassenes Datenangebot
des Baulogistikdienstleisters.
```

Der Baulogistikdienstleister muss zu diesem Zeitpunkt noch keine aktuellen Daten liefern.

Er muss lediglich sicherstellen, dass sein bereits eingerichteter Equipment Data Service später erreichbar ist.

Der konkrete Abruf erfolgt erst in Hauptprozess 3.

---

## Rolle des Nachunternehmers

Auch der Nachunternehmer erhält in Hauptprozess 2 noch nicht zwingend die vollständigen Planungsdaten.

Er muss jedoch als Adressat des Planungsauftrags eindeutig festgelegt werden.

Beispielsweise:

```
Planning Assignment

Project:
Project-X

Provider:
Generalunternehmer

Consumer:
Nachunternehmer A

Purpose:
DetailedScheduling
```

Optional kann der Nachunternehmer den Planungsauftrag zunächst bestätigen.

Damit kann beispielsweise fachlich festgehalten werden:

```
Planungsauftrag angefragt
        ↓
Nachunternehmer bestätigt
        ↓
Planning Context darf abgerufen werden
```

Ob eine solche Bestätigung notwendig ist, ist eine Prozessentscheidung und keine zwingende Eigenschaft der Ontologien.

---

## Planungsauftrag als eigenes Austauschobjekt

Für den Gesamtprozess ist es sinnvoll, den konkreten Planungsauftrag als eigenes Objekt zu behandeln.

Er beschreibt nicht selbst die eigentlichen Terminplandaten, sondern referenziert die zu verwendenden Informationen.

Vereinfacht:

```
PlanningAssignment
│
├── Project-X
├── Generalunternehmer
├── Nachunternehmer
│
├── delegatedActivities
│      └── A100
│
├── contextActivities
│      ├── A090
│      └── A120
│
├── requiredContext
│      ├── WBS
│      ├── LBS
│      ├── SiteArea
│      └── SiteEquipment
│
└── purpose
       └── DetailedScheduling
```

Dieses Objekt gehört **nicht in die Construction Schedule Ontology**.

Es beschreibt den organisationsübergreifenden Austauschprozess.

Dafür könnte später entweder

- ein kleines Construct-X Exchange/Collaboration Model oder
- ein entsprechendes Manifest des Datenprodukts

verwendet werden.

---

## Ontologien werden für die Auswahlregeln verwendet

Eine wichtige Funktion der Ontologien besteht in diesem Hauptprozess darin, nicht nur konkrete Ressourcen auszuwählen, sondern **fachliche Auswahlregeln zu definieren**.

Beispielsweise kann der Generalunternehmer festlegen:

```
Für Activity A100:

1. liefere den zugehörigen WBSNode,
2. liefere den zugehörigen LBSNode,
3. ermittle alle relevanten SiteAreas,
4. ermittle das dort verfügbare SiteEquipment,
5. berücksichtige Equipment vom Typ ConstructionLift.
```

Diese Regel kann später automatisch ausgeführt werden.

Vereinfacht:

```
A100
 │
 ├─ WBS?
 │
 ├─ LBS?
 │
 ├─ SiteArea?
 │
 └─ Equipment?
```

Die Ontologien liefern die Beziehungen, über die diese Informationen gefunden werden können.

---

## Es wird noch kein vollständiger Planning Context erzeugt

Ein zentraler Punkt des zweiten Hauptprozesses ist:

> Der Generalunternehmer definiert **was benötigt wird**, erzeugt aber noch nicht zwingend die tatsächlichen Daten.

Beispielsweise wird lediglich festgelegt:

```
A100
+
WBS
+
LBS
+
SiteArea
+
ConstructionLift
```

Erst wenn der Nachunternehmer später auf den Planning Context Service zugreift, werden die aktuellen Informationen tatsächlich zusammengestellt.

Damit bleibt der spätere Planning Context aktuell.

---

## Datenraumfunktion in diesem Hauptprozess

Die Datenraumtechnik spielt in Hauptprozess 2 nur eine unterstützende Rolle.

Benötigt wird im Wesentlichen:

```
Identität des Nachunternehmers
        +
bestehende Nutzungsrechte
        +
Planning Context Service
        +
Planungsauftrag
```

Es muss noch kein eigentlicher Datentransfer stattfinden.

Der Generalunternehmer hinterlegt lediglich, dass ein bestimmter Nachunternehmer für einen bestimmten Planungsauftrag auf den später erzeugten Planning Context zugreifen darf.

---

## Technische Aufgaben der drei Teilnehmer

### Generalunternehmer

Der Generalunternehmer muss:

```
Rahmenaktivitäten auswählen
        ↓
delegated / context unterscheiden
        ↓
WBS-Zuordnung bestimmen
        ↓
LBS-Zuordnung bestimmen
        ↓
benötigten Site-Kontext festlegen
        ↓
benötigtes Equipment definieren
        ↓
Planungsauftrag speichern
```

Dabei werden insbesondere die Construction Schedule-, Breakdown Structure- und Construction Site Ontologien verwendet.

---

### Baulogistikdienstleister

Der Baulogistikdienstleister muss in diesem Hauptprozess lediglich sicherstellen:

```
Equipment Data Service
ist verfügbar

+
vereinbarte Equipment-Typen
sind semantisch beschrieben

+
Nutzungsrechte aus Hauptprozess 1
sind weiterhin gültig
```

Ein konkreter Datenabruf findet noch nicht statt.

---

### Nachunternehmer

Der Nachunternehmer muss:

```
als Consumer des Planungsauftrags
eindeutig festgelegt sein

+
über die erforderliche
Projektrolle verfügen

+
den Planning Context
später semantisch verarbeiten können
```

Optional bestätigt er die Übernahme des Planungsauftrags.

---

## Ergebnis von Hauptprozess 2

Am Ende des zweiten Hauptprozesses existiert ein eindeutig beschriebener Planungsauftrag.

Beispielsweise:

```
PLANUNGSAUFTRAG

Projekt:
Project-X

Nachunternehmer:
Subcontractor-A

Zu detaillieren:
A100 Ausbau 5. OG

Kontextaktivitäten:
A090
A120

WBS:
Innenausbau

LBS:
5. Obergeschoss

zusätzlicher Kontext:
SiteArea
ConstructionLift

Purpose:
DetailedScheduling
```

Noch nicht enthalten sind die aktuellen Daten zu:

```
konkreter SiteArea
aktuellem Bauaufzug
aktueller Equipment-Verfügbarkeit
vollständigem Planning Context
```

Diese werden erst im nächsten Hauptprozess ermittelt.

# Hauptprozess 3 – Planungskontext erzeugen und bereitstellen

Im dritten Hauptprozess fordert der Nachunternehmer den für seinen Planungsauftrag benötigten Planungskontext an.

Der Generalunternehmer stellt daraufhin die benötigten Informationen **dynamisch aus den aktuellen Datenquellen** zusammen. Dabei werden eigene Daten des Generalunternehmers mit – soweit erforderlich und zulässig – Daten des Baulogistikdienstleisters kombiniert.

Die Construct-X-Ontologien bilden dabei die gemeinsame semantische Struktur, über die die relevanten Informationen gefunden, miteinander verknüpft und anschließend an den Nachunternehmer übertragen werden.

Der Hauptprozess beantwortet damit die Frage:

> **Welche aktuellen Informationen benötigt der Nachunternehmer für den konkreten Planungsauftrag und wie werden diese automatisiert zu einem konsistenten Planungskontext zusammengestellt?**

---

## Ausgangssituation

Aus Hauptprozess 2 liegt ein konkreter Planungsauftrag vor.

Beispielsweise:

```
Planungsauftrag

Nachunternehmer:
Subcontractor-A

zu detaillierende Aktivität:
A100 Ausbau 5. OG

Kontextaktivitäten:
A090 Rohbau 5. OG fertig
A120 Übergabe 5. OG

benötigter Kontext:
WBS
LBS
SiteArea
ConstructionLift
```

Zusätzlich bestehen aus Hauptprozess 1 bereits:

- die Datenraumbeziehungen,
- die Nutzungsrechte,
- die Datenangebote,
- die verwendeten Construct-X-Ontologien,
- die benötigten Adapter,
- die vereinbarten semantischen Profile.

Der eigentliche Planning Context wurde jedoch noch nicht erzeugt.

---

## Nachunternehmer fordert den Planungskontext an

Der Prozess beginnt mit dem Nachunternehmer.

In seinem Planungssystem (z.B. Metronom) bzw. über die angebundene Datenraumkomponente fordert er den für den Planungsauftrag vorgesehenen Planning Context an.

Vereinfacht:

```
Nachunternehmer
       │
       │ Planning Context anfordern
       ▼
Planning Context Service
des Generalunternehmers
```

Bei der Anfrage wird mindestens referenziert:

```
Projekt
Planungsauftrag
Nachunternehmer
Nutzungszweck
```

Beispielsweise:

```
Project:
Project-X

PlanningAssignment:
PA-100

Consumer:
Subcontractor-A

Purpose:
DetailedScheduling
```

Der Nachunternehmer muss dabei nicht wissen, aus welchen einzelnen Systemen die Informationen beim Generalunternehmer stammen.

---

## Generalunternehmer prüft den Zugriff

Der Connector des Generalunternehmer prüft zunächst, ob der Zugriff zulässig ist.

Dabei wird beispielsweise geprüft:

```
Ist der Teilnehmer eindeutig identifiziert?
        ↓
Gehört er zum Projekt?
        ↓
Ist er der Nachunternehmer des Planungsauftrags?
        ↓
Ist der Zweck DetailedScheduling zulässig?
        ↓
Besteht ein gültiges Nutzungsrecht?
```

Erst wenn diese Bedingungen erfüllt sind, wird der Planning Context erzeugt.

Die Datenraumdienste übernehmen an dieser Stelle insbesondere:

- Identifikation des Teilnehmers,
- Prüfung der Berechtigung,
- Zuordnung zum vorhandenen Datenangebot,
- Autorisierung des Datentransfers.

Die eigentliche fachliche Zusammenstellung der Daten erfolgt dagegen über die Construct-X-basierte Integrationsschicht des Generalunternehmers.

---

## Planungsauftrag auswerten

Der Planning Context Service liest zunächst den in Hauptprozess 2 definierten Planungsauftrag.

Daraus ist bekannt:

```
zu detaillierende Activity
+
Kontextaktivitäten
+
benötigte fachliche Informationen
```

Beispielsweise:

```
A100
+
A090
+
A120
+
WBS
+
LBS
+
SiteArea
+
ConstructionLift
```

Damit besitzt der Dienst eine fachliche Vorgabe dafür, welche Daten aus den verschiedenen Quellen benötigt werden.

---

## Aktuelle Terminplandaten abrufen

Der Generalunternehmer liest zunächst die aktuellen Informationen zu den relevanten Aktivitäten aus seinem Terminplanungssystem (z.B. MS Project).

```
Terminplanungssystem
        ↓
Schedule Adapter
        ↓
Construction Schedule Ontology
```

Beispielsweise werden folgende Aktivitäten übernommen:

```
A090
A100
A120
```

mit Informationen wie:

```
identifier
name
plannedStart
plannedFinish
PrecedenceRelationships
```

Wichtig ist:

> Es werden die zum Zeitpunkt des Abrufs aktuellen Daten verwendet und nicht eine zuvor erzeugte Kopie des Terminplans.

Damit können zwischen Hauptprozess 2 und Hauptprozess 3 eingetretene Änderungen berücksichtigt werden.

---

## WBS- und LBS-Kontext ermitteln

Anschließend werden die organisatorischen und räumlichen Zuordnungen der ausgewählten Aktivitäten über ein anderes System ermittelt.

Über die Construct-X Link Ontology kann beispielsweise festgestellt werden:

```
Activity A100
       │
       ├──────────────► WBSNode
       │
       └──────────────► LBSNode
```

Beispielsweise:

```
A100 Ausbau 5. OG
       │
       ├── WBS → Innenausbau
       │
       └── LBS → 5. Obergeschoss
```

Diese Informationen können aus einem separaten WBS/LBS-System stammen.

```
WBS/LBS-System
       ↓
Breakdown Structure Adapter
       ↓
Breakdown Structure Ontology
```

Die Ontologien ermöglichen damit die Verbindung zwischen Terminplanung und Projektstruktur, obwohl die Informationen ursprünglich aus unterschiedlichen Anwendungen stammen.

---

## Relevanten Baustellenbereich semantisch bestimmen

Auf Basis der LBS-Zuordnung kann anschließend der relevante Baustellenbereich ermittelt werden. Hierzu wird auch ein System beim Generalunternehmen genutzt.

Die vorhandenen Beziehungen ermöglichen beispielsweise:

```
Activity
   │
   │ isPerformedIn
   ▼
LBSNode
   ▲
   │ isRepresentedByLBSNode
   │
SiteArea
```

Für die Aktivität

```
A100 Ausbau 5. OG
```

kann damit beispielsweise ein

```
SiteArea:
Arbeitsbereich 5. Obergeschoss
```

ermittelt werden.

Der Generalunternehmer muss diesen Zusammenhang nicht erneut manuell herstellen.

Er ergibt sich aus den bereits vorhandenen semantischen Beziehungen.

Das ist eine wesentliche Funktion der Ontologien in diesem Prozess:

> Nicht alle benötigten Informationen müssen direkt am Planungsauftrag hinterlegt werden. Weitere relevante Informationen können über die semantischen Beziehungen ermittelt werden.

---

## Benötigtes Equipment bestimmen

Aus dem relevanten `SiteArea` kann anschließend ermittelt werden, welches `SiteEquipment` für diesen Bereich relevant ist.

Semantisch besteht beispielsweise folgende Beziehung:

```
SiteEquipment
      │
      │ usesSiteArea
      ▼
SiteArea
```

Zusammen ergibt sich damit die vollständige semantische Kette:

```
Activity
   │
   ▼
LBSNode
   ▲
   │
SiteArea
   ▲
   │
SiteEquipment
```

Der Planungsauftrag kann zusätzlich festlegen, dass nur Equipment eines bestimmten Typs berücksichtigt werden soll.

Beispielsweise:

```
EquipmentType:
ConstructionLift
```

Der Planning Context Service sucht deshalb nach:

> Equipment vom Typ ConstructionLift, das für den für A100 relevanten Baustellenbereich zur Verfügung steht.

---

## Aktuelle Daten beim Baulogistikdienstleister abrufen

Die benötigten Equipment-Informationen stammen in diesem Beispiel vom Baulogistikdienstleister.

Der Generalunternehmer besitzt aus Hauptprozess 1 bereits die erforderlichen Nutzungsrechte.

Der Generalunternehmer kann deshalb den Equipment Data Service des Baulogistikdienstleisters aufrufen.

```
Generalunternehmer
       │
       │ Anfrage:
       │ Project-X
       │ SiteArea
       │ ConstructionLift
       ▼
Baulogistikdienstleister
```

Der Baulogistikdienstleister prüft die Anfrage und liefert anschließend die aktuellen Informationen.

Beispielsweise:

```
ConstructionLift-4711

type:
ConstructionLift

relevant SiteArea:
Arbeitsbereich 5. OG

status:
available
```

Diese Daten werden bereits auf Grundlage der Construct-X Construction Site Ontology bereitgestellt.

---

## Rolle des Baulogistikdienstleisters

Der Baulogistikdienstleister muss in diesem Hauptprozess insbesondere:

1. die Anfrage des Generalunternehmers entgegennehmen,
2. die vorhandenen Nutzungsrechte prüfen,
3. die aktuellen Equipment-Daten aus seinem Fachsystem lesen,
4. diese über seinen Construct-X-Adapter semantisch bereitstellen,
5. die ursprünglichen Identitäten der Ressourcen beibehalten.

Die Verarbeitung sieht vereinfacht so aus:

```
Equipment-System
       ↓
Equipment Adapter
       ↓
Construct-X
       ↓
Equipment Data Service
       ↓
Generalunternehmer
```

Der Baulogistikdienstleister liefert nur die benötigten Informationen.

Er muss weder den Terminplan des Generalunternehmers noch das Planungssystem des Nachunternehmers kennen.

---

## Daten verschiedener Quellen zusammenführen

Der Generalunternehmer verfügt nun über Informationen aus mehreren Systemen:

```
Terminplanungssystem
        │
        ├── Activities
        │
WBS/LBS-System
        │
        ├── WBSNodes
        ├── LBSNodes
        │
Site-System
        │
        ├── SiteAreas
        │
Baulogistikdienstleister
        │
        └── SiteEquipment
```

Diese Daten werden nun in einem gemeinsamen Construct-X-Graph zusammengeführt.

Vereinfacht:

```
                Construct-X Planning Context

A100 ───────────────► WBS Innenausbau

 │
 └──────────────────► LBS 5. OG
                            ▲
                            │
                     SiteArea 5. OG
                            ▲
                            │
                     ConstructionLift
```

Entscheidend ist dabei:

> Die einzelnen Datenquellen werden nicht in ein neues proprietäres Datenmodell übersetzt. Sie werden über die gemeinsamen Construct-X-Ontologien miteinander verbunden.

---

## Identitäten der ursprünglichen Daten erhalten

Beim Zusammenführen der Daten erzeugt der Generalunternehmer nicht für alle Ressourcen neue Identitäten.

Beispielsweise:

```
Activity A100
→ Identität des Generalunternehmers

WBSNode
→ Identität des Generalunternehmers

SiteArea
→ Identität des Generalunternehmers

ConstructionLift-4711
→ Identität des Baulogistikdienstleisters
```

Dadurch bleibt erkennbar, welcher Teilnehmer eine Information ursprünglich bereitgestellt hat.

Beispielsweise:

```
Generalunternehmer:
https://data.general-contractor.example/activity/A100

Baulogistikdienstleister:
https://data.logistics-provider.example/equipment/4711
```

Der Planning Context verbindet diese Ressourcen lediglich miteinander.

---

## Herkunft der Informationen dokumentieren

Zusätzlich zur fachlichen Semantik sollte die Herkunft der Informationen dokumentiert werden.

Beispielsweise:

```
Activity A100
        ↓
Quelle:
Terminplanung Generalunternehmer

ConstructionLift-4711
        ↓
Quelle:
Baulogistikdienstleister
```

Hierfür kann eine Provenance-Beschreibung verwendet werden.

Damit bleibt später nachvollziehbar:

- wer eine Information bereitgestellt hat,
- aus welchem System sie stammt,
- wann sie abgerufen wurde,
- auf welchem Datenstand sie basiert.

Dies ist insbesondere bei Daten mehrerer Unternehmen wichtig.

---

## Nur den erforderlichen Teilgraphen erzeugen

Der Nachunternehmer erhält nicht sämtliche Daten des Gesamtprojekts.

Aus dem gesamten Wissensgraphen wird nur der für den Planungsauftrag benötigte Teil ausgewählt.

Beispielsweise:

```
Gesamtprojekt

10.000 Activities
500 LBSNodes
200 SiteAreas
100 SiteEquipment

        ↓ semantische Auswahl

Planning Context PA-100

3 Activities
1 WBSNode
1 LBSNode
1 SiteArea
1 ConstructionLift
```

Die Ontologien ermöglichen damit nicht nur die Integration, sondern auch eine **gezielte fachliche Selektion**.

---

## Nutzungsrechte externer Daten berücksichtigen

Bevor die Daten des Baulogistikdienstleisters in den Planning Context aufgenommen werden, prüft der Generalunternehmer zusätzlich die in Hauptprozess 1 vereinbarten Weitergaberechte.

Beispielsweise:

```
ConstructionLift Data

Nutzung durch Generalunternehmer:
✓

Integration in Planning Context:
✓

Weitergabe an Nachunternehmer:
✓

Purpose:
DetailedScheduling
```

Nur wenn diese Bedingungen erfüllt sind, wird die entsprechende Information in den Planning Context aufgenommen.

Damit wird die semantische Graphbildung mit den Nutzungsrechten kombiniert.

Vereinfacht:

```
fachlich relevant?
       +
Nutzung erlaubt?
       ↓
in Planning Context aufnehmen
```

---

## Planning Context mit SHACL prüfen

Der erzeugte Teilgraph wird anschließend gegen das vereinbarte SHACL-Profil geprüft.

Beispielsweise wird kontrolliert:

```
Activity vorhanden?
✓

Start und Ende vorhanden?
✓

LBS-Zuordnung vorhanden?
✓

SiteArea vorhanden?
✓

Equipment-Typ vorhanden?
✓
```

Fehlen verpflichtende Informationen oder sind Beziehungen formal ungültig, wird der Planning Context nicht unmittelbar übertragen.

Die SHACL-Prüfung stellt damit sicher, dass der Nachunternehmer eine technisch verarbeitbare Datenstruktur erhält.

---

## Übertragungssnapshot erzeugen

Der Planning Context ist dynamisch erzeugt worden.

Für den konkreten Datenaustausch sollte daraus jedoch ein **eindeutig referenzierbarer Snapshot** erzeugt werden.

Beispielsweise:

```
PlanningContextSnapshot:
PCS-2026-10-27-001
```

Der Snapshot dokumentiert unter anderem:

```
Planning Assignment:
PA-100

generatedAt:
2026-10-27 ...

Ontology Versions:
Construction Schedule 0.5.0
Breakdown Structure 0.7.0
Construction Site 0.1.0

Sources:
Terminplan-Version ...
WBS/LBS-Version ...
Equipment-Service-Abruf ...

Consumer:
Subcontractor-A
```

Dadurch ist später eindeutig nachvollziehbar, **auf welchem Datenstand die Feinplanung des Nachunternehmers basiert**.

Dies ist wichtig, weil sich die Quellsysteme nach der Übertragung weiter verändern können.

---

## Planungskontext übertragen

Nach erfolgreicher Prüfung wird der Planning Context über den Datenraum an den Nachunternehmer übertragen.

Als Austauschformat kann beispielsweise JSON-LD verwendet werden.

Vereinfacht:

```
Construct-X Graph
       ↓
JSON-LD
       ↓
Data Transfer
       ↓
Nachunternehmer
```

Der Datenraum übernimmt dabei den kontrollierten Transfer.

Die fachliche Struktur des Inhalts wird dagegen durch Construct-X bestimmt.

---

## Nachunternehmer prüft den empfangenen Planning Context

Nach dem Empfang prüft der Nachunternehmer zunächst die Daten.

Dazu kann er dasselbe SHACL-Profil verwenden.

```
Planning Context
       ↓
SHACL Validation
       ↓
gültig?
```

Damit prüft sowohl der Sender als auch der Empfänger gegen dieselben semantischen Anforderungen.

---

## Planning Context in das Fachsystem übernehmen

Nach erfolgreicher Prüfung werden die Construct-X-Daten in das interne Planungssystem des Nachunternehmers überführt (z.B. Metronom).

```
Construct-X Planning Context
        ↓
Construct-X Adapter
        ↓
Taktplanungssystem
```

Dabei werden beispielsweise umgesetzt:

```
Activity
        ↓
Planungsaktivität

LBSNode
        ↓
Planungs-/Taktbereich

plannedStart / plannedFinish
        ↓
zeitliche Randbedingungen

SiteEquipment
        ↓
verfügbare Planungsressource
```

Der Nachunternehmer kann anschließend vollständig in seinem eigenen Fachsystem weiterarbeiten.

---

## Referenz auf den empfangenen Snapshot speichern

Der Nachunternehmer sollte zusätzlich die Identität des erhaltenen Planning Context speichern.

Beispielsweise:

```
Based on:

PlanningContextSnapshot
PCS-2026-10-27-001
```

Die später erzeugte Feinplanung kann auf diesen Snapshot verweisen.

Damit kann nachvollzogen werden:

```
Welche Daten
        ↓
wurden wann bereitgestellt
        ↓
und dienten welcher Feinplanung
als Grundlage?
```

---

## Aufgaben der drei Teilnehmer

## Generalunternehmer

Der Generalunternehmer führt den größten Teil dieses Hauptprozesses aus:

```
Planning Assignment lesen
        ↓
aktuelle Activities abrufen
        ↓
WBS/LBS ermitteln
        ↓
SiteArea semantisch bestimmen
        ↓
benötigtes Equipment bestimmen
        ↓
Equipment-Daten abrufen
        ↓
Nutzungsrechte prüfen
        ↓
Construct-X Graph erzeugen
        ↓
SHACL validieren
        ↓
Snapshot erzeugen
        ↓
Planning Context übertragen
```

---

## Baulogistikdienstleister

Der Baulogistikdienstleister:

```
Equipment-Anfrage erhalten
        ↓
Berechtigung prüfen
        ↓
aktuelle Equipment-Daten lesen
        ↓
auf Construct-X abbilden
        ↓
Daten bereitstellen
```

Er liefert nur die für die Anfrage benötigten Informationen.

---

## Nachunternehmer

Der Nachunternehmer:

```
Planning Context anfordern
        ↓
Planning Context empfangen
        ↓
SHACL prüfen
        ↓
Construct-X interpretieren
        ↓
in eigenes Planungssystem konvertieren
        ↓
Snapshot-ID speichern
```

Anschließend kann Hauptprozess 4 – die eigentliche Detail- bzw. Taktplanung – beginnen.

---

## Rolle der Ontologien in Hauptprozess 3

Die Construct-X-Ontologien übernehmen in diesem Hauptprozess drei zentrale Aufgaben.

### Gemeinsame Bedeutung

Sie sorgen dafür, dass alle Beteiligten beispielsweise unter

```
Activity
LBSNode
SiteArea
SiteEquipment
```

dieselbe fachliche Bedeutung verstehen.

### Verknüpfung unterschiedlicher Datenquellen

Sie ermöglichen Beziehungen über System- und Unternehmensgrenzen hinweg:

```
Activity
   ↓
LBSNode
   ↑
SiteArea
   ↑
SiteEquipment
```

Dadurch kann der benötigte Kontext automatisiert ermittelt werden.

### Fachliche Selektion

Die semantischen Beziehungen können verwendet werden, um nur diejenigen Informationen auszuwählen, die für einen konkreten Planungsauftrag benötigt werden.

Damit wird aus mehreren verteilten Datenquellen ein gezielter, konsistenter Planning Context.

---

## Ergebnis von Hauptprozess 3

Am Ende des Hauptprozesses besitzt der Nachunternehmer einen aktuellen, überprüften und eindeutig referenzierbaren Planning Context.

Beispielsweise:

```
Planning Context
PCS-2026-10-27-001

├── A090 Kontextaktivität
├── A100 zu detaillierende Aktivität
├── A120 Kontextaktivität
│
├── WBS Innenausbau
├── LBS 5. Obergeschoss
├── SiteArea 5. Obergeschoss
└── ConstructionLift-4711
```

Die Informationen stammen aus unterschiedlichen Systemen und teilweise von unterschiedlichen Unternehmen, bilden für den Nachunternehmer jedoch einen **einheitlichen semantischen Zusammenhang**.

Der Kern des Hauptprozesses lässt sich damit wie folgt zusammenfassen:

```
Planungskontext anfordern
        ↓
Berechtigung prüfen
        ↓
aktuelle Daten aus Quellsystemen lesen
        ↓
semantisch relevante Daten ermitteln
        ↓
Daten Dritter bei Bedarf abrufen
        ↓
Construct-X Teilgraph erzeugen
        ↓
Nutzungsrechte berücksichtigen
        ↓
SHACL prüfen
        ↓
Snapshot erzeugen
        ↓
Planning Context übertragen
        ↓
in Fachsystem des Nachunternehmers übernehmen
```

Damit liegen alle erforderlichen Informationen für die anschließende Detail- bzw. Taktplanung vor.

# Hauptprozess 4 – Detailplanung durchführen und bereitstellen

Im vierten Hauptprozess erstellt der Nachunternehmer auf Grundlage des zuvor bereitgestellten Planning Context seine Fein- bzw. Taktplanung.

Der Nachunternehmer arbeitet dabei weiterhin mit seinem eigenen Planungssystem. Die Construct-X-Ontologien ersetzen dieses Fachsystem nicht. Sie stellen vielmehr sicher, dass

- die vom Generalunternehmer erhaltenen Randbedingungen eindeutig interpretiert werden können,
- die neu erzeugten Detailaktivitäten eindeutig beschrieben werden,
- die Beziehung zur ursprünglichen Rahmenplanung erhalten bleibt,
- das Planungsergebnis anschließend systemunabhängig an den Generalunternehmer zurückgegeben werden kann.

Der Hauptprozess beantwortet damit die Frage:

> **Wie wird aus einer übergeordneten Rahmenaktivität eine detaillierte Planung, die anschließend wieder eindeutig mit der ursprünglichen Planung des Generalunternehmers verbunden werden kann?**

---

## Ausgangssituation

Aus Hauptprozess 3 besitzt der Nachunternehmer einen gültigen Planning Context.

Beispielsweise:

```
Planning Context
PCS-001

├── A090 Kontextaktivität
├── A100 zu detaillierende Rahmenaktivität
├── A120 Kontextaktivität
│
├── WBS Innenausbau
├── LBS 5. Obergeschoss
├── SiteArea 5. Obergeschoss
└── ConstructionLift-4711
```

Zusätzlich kennt der Nachunternehmer den Planungsauftrag:

```
zu detaillieren:
A100 Ausbau 5. OG

Planungszeitraum:
02.11.2026 – 27.11.2026

Planungsort:
5. Obergeschoss

verfügbare Ressource:
ConstructionLift-4711
```

Damit liegen die Randbedingungen für die Detailplanung vor.

---

## Planning Context im Fachsystem verwenden

Der Planning Context wurde bereits in Hauptprozess 3 über den Construct-X-Adapter in das interne Planungssystem des Nachunternehmers übernommen.

Vereinfacht:

```
Construct-X Planning Context
          ↓
Construct-X Adapter
          ↓
Planungssystem des Nachunternehmers
```

Im Planungssystem stehen damit beispielsweise zur Verfügung:

```
Rahmenaktivität
Zeitfenster
Vorgänger / Nachfolger
Planungsbereich
Baustellenbereich
verfügbare Ressource
```

Der Nachunternehmer kann diese Informationen nun für seine eigene Planung verwenden.

---

## Rahmenaktivität detaillieren

Die übergeordnete Aktivität des Generalunternehmers wird durch mehrere detaillierte Aktivitäten ersetzt bzw. fachlich untergliedert.

Aus

```
A100
Ausbau 5. Obergeschoss
```

können beispielsweise entstehen:

```
NA-101 Unterkonstruktion herstellen

NA-102 Installationen vorbereiten

NA-103 Trennwände montieren

NA-104 Decke montieren

NA-105 Abschlussarbeiten
```

Diese Detailaktivitäten werden durch den Nachunternehmer geplant.

Die ursprüngliche Aktivität `A100` bleibt jedoch bestehen.

Sie bildet weiterhin den übergeordneten Rahmen des Generalunternehmers.

---

## Eigene Detailaktivitäten eindeutig identifizieren

Die neu erzeugten Aktivitäten gehören zum Datenbestand des Nachunternehmers.

Sie sollten deshalb eigene stabile Identitäten erhalten.

Beispielsweise:

```
https://data.subcontractor.example/
activity/NA-101
```

und

```
https://data.subcontractor.example/
activity/NA-102
```

Damit bleibt eindeutig unterscheidbar:

```
A100
→ Aktivität des Generalunternehmers

NA-101
→ Aktivität des Nachunternehmers
```

Dies ist insbesondere für die spätere Zusammenführung der Planungen wichtig.

Der Generalunternehmer übernimmt nicht die Identität der Aktivitäten des Nachunternehmers und der Nachunternehmer verändert nicht die Identität der Rahmenaktivität des Generalunternehmers.

---

## Detailaktivitäten mit der Rahmenaktivität verbinden

Die neu erzeugten Detailaktivitäten müssen eindeutig mit der Rahmenaktivität verbunden werden, aus der sie entstanden sind.

Semantisch wird eine Hierarchiebeziehung hergestellt:

```
A100 Ausbau 5. OG
        │
        ├── NA-101 Unterkonstruktion
        ├── NA-102 Installationen
        ├── NA-103 Trennwände
        ├── NA-104 Decke
        └── NA-105 Abschlussarbeiten
```

Die Beziehung bedeutet:

> Diese Detailaktivitäten konkretisieren die vom Generalunternehmer freigegebene Rahmenaktivität A100.

Damit kann der Generalunternehmer die Detailplanung später automatisch der richtigen Aktivität seines Rahmenterminplans zuordnen.

Diese Beziehung sollte über die Construction Schedule Ontology bzw. eine darin vorgesehene Aktivitätshierarchie beschrieben werden.

---

## Termine und Abhängigkeiten detaillieren

Der Nachunternehmer plant anschließend die zeitliche Struktur der Detailaktivitäten.

Beispielsweise:

```
NA-101
02.11. – 05.11.

       ↓

NA-102
06.11. – 10.11.

       ↓

NA-103
11.11. – 16.11.

       ↓

NA-104
17.11. – 21.11.

       ↓

NA-105
22.11. – 25.11.
```

Die Detailaktivitäten werden wiederum als `Activity`-Instanzen beschrieben.

Zwischen ihnen können `PrecedenceRelationship`-Beziehungen bestehen.

Damit entsteht beispielsweise:

```
NA-101
   ↓
NA-102
   ↓
NA-103
   ↓
NA-104
```

Die gleiche semantische Struktur kann somit sowohl für den Rahmenterminplan als auch für die Feinplanung verwendet werden.

---

## Rahmenbedingungen des Generalunternehmers berücksichtigen

Die Detailplanung muss die im Planning Context enthaltenen Randbedingungen berücksichtigen.

Beispielsweise:

```
A090
Rohbau abgeschlossen
        ↓

Detailplanung des Nachunternehmers
        ↓

A120
Übergabe 5. OG
```

Die Planung sollte damit innerhalb des vom Generalunternehmer vorgegebenen zeitlichen Korridors liegen.

Beispielsweise:

```
A100:

02.11.2026
───────────────
Rahmen
───────────────
27.11.2026

       ↓

NA-101 ... NA-105

müssen innerhalb dieses
Planungsrahmens liegen
```

Falls der Nachunternehmer feststellt, dass der Rahmen nicht eingehalten werden kann, wäre dies ein eigener Abstimmungs- bzw. Änderungsprozess.

Dieser gehört nicht zum hier betrachteten einfachen Standardablauf.

---

## Räumliche Zuordnung übernehmen und verfeinern

Die Detailaktivitäten können die räumliche Zuordnung der Rahmenaktivität übernehmen.

Aus:

```
A100
    ↓
LBS 5. Obergeschoss
```

wird beispielsweise:

```
NA-101 ──► LBS 5. Obergeschoss
NA-102 ──► LBS 5. Obergeschoss
NA-103 ──► LBS 5. Obergeschoss
```

Falls das Planungssystem des Nachunternehmers eine feinere räumliche Unterteilung verwendet, können zusätzliche Bereiche berücksichtigt werden.

Beispielsweise:

```
5. Obergeschoss

├── Zone A
├── Zone B
└── Zone C
```

Für die organisationsübergreifende Rückgabe muss jedoch weiterhin erkennbar sein, wie diese feineren Bereiche mit der übergeordneten LBS-Struktur des Generalunternehmers zusammenhängen.

---

## Baustellenressourcen in der Planung berücksichtigen

Auch die im Planning Context enthaltenen Baustellenressourcen können in die Detailplanung einfließen.

Beispielsweise:

```
ConstructionLift-4711
        │
        └── relevant für
              ↓
          NA-102
          NA-103
          NA-104
```

Der Nachunternehmer kann damit in seinem eigenen Planungssystem berücksichtigen, dass bestimmte Aktivitäten auf die Nutzung des Bauaufzugs angewiesen sind.

Dabei ist wichtig:

> Der Nachunternehmer erzeugt keine neue Kopie des Bauaufzugs als unabhängige Ressource.

Er referenziert weiterhin die vom Baulogistikdienstleister bereitgestellte Ressource.

Damit bleibt die ursprüngliche Identität erhalten:

```
Baulogistikdienstleister
        ↓
ConstructionLift-4711
        ↑
        │ Referenz
Nachunternehmer
```

---

## Rolle des Baulogistikdienstleisters

Im Standardfall besitzt der Baulogistikdienstleister in Hauptprozess 4 keine aktive Prozessaufgabe.

Seine bereits bereitgestellten Informationen werden lediglich bei der Planung verwendet.

```
Baulogistikdienstleister

Equipment-Daten
      ↓
Planning Context
      ↓
Planung des Nachunternehmers
```

Der Nachunternehmer verändert diese Daten nicht.

Falls während der Planung eine neue Reservierung, Terminabstimmung oder Ressourcenanforderung notwendig wird, wäre dafür ein eigener logistischer Prozess erforderlich.

Dieser wird im vorliegenden Basisszenario zunächst nicht betrachtet.

---

## Planungsergebnis aus dem Fachsystem exportieren

Nach Abschluss der Detailplanung wird das Ergebnis wieder aus dem Planungssystem des Nachunternehmers exportiert.

Dafür wird der in Hauptprozess 1 vorbereitete Converter verwendet:

```
Planungssystem
      ↓
Construct-X Converter
      ↓
Construct-X Detail Schedule
```

Der Nachunternehmer muss damit keinen projektspezifischen Export für das Terminplanungssystem des Generalunternehmers entwickeln.

Er bildet lediglich sein internes Modell auf Construct-X ab.

---

## Construct-X Detail Schedule erzeugen

Das Ergebnis enthält insbesondere:

```
Detail Activities
+
Termine
+
Abhängigkeiten
+
räumliche Zuordnungen
+
Bezug zur Rahmenaktivität
```

Beispielsweise:

```
Detail Schedule

A100
 ├── NA-101
 ├── NA-102
 ├── NA-103
 ├── NA-104
 └── NA-105
```

Die Construction Schedule Ontology bildet dabei die Terminplanstruktur ab.

Die Breakdown Structure Ontology und die entsprechenden Link Ontologies ermöglichen weiterhin die räumliche und organisatorische Zuordnung.

Damit verwendet die Rückgabe dieselben semantischen Grundlagen wie die zuvor empfangenen Daten.

---

## Bezug zum Planning Context erhalten

Ein besonders wichtiger Punkt ist die Verbindung zwischen der neuen Detailplanung und dem Planning Context, auf dessen Grundlage sie erstellt wurde.

Die Detailplanung sollte deshalb den verwendeten Snapshot referenzieren.

Beispielsweise:

```
DetailedSchedule-001

wasDerivedFrom

PlanningContextSnapshot
PCS-001
```

Dadurch ist später nachvollziehbar:

```
Detailplanung
      ↓
basiert auf
      ↓
Planning Context PCS-001
      ↓
Datenstand zum Zeitpunkt
der Planung
```

Wenn sich der Rahmenterminplan oder die Equipment-Daten später verändern, bleibt weiterhin nachvollziehbar, welche Informationen der Nachunternehmer bei seiner Planung tatsächlich verwendet hat.

---

## Herkunft der neuen Daten erhalten

Auch für die neuen Detailaktivitäten muss die Herkunft eindeutig sein.

Beispielsweise:

```
NA-101
        ↓
provided by
Nachunternehmer

NA-102
        ↓
provided by
Nachunternehmer
```

Damit ist im später zusammengeführten Terminplan weiterhin erkennbar:

```
Rahmenaktivität
→ Generalunternehmer

Detailaktivitäten
→ Nachunternehmer

Equipment-Daten
→ Baulogistikdienstleister
```

Die gemeinsame Ontologie bedeutet damit nicht, dass die Eigentümerschaft oder Herkunft der Daten verloren geht.

---

## Detailplanung semantisch prüfen

Bevor die Detailplanung bereitgestellt wird, wird sie gegen das vereinbarte SHACL-Profil geprüft.

Beispielsweise:

```
jede DetailActivity besitzt:

✓ identifier
✓ name
✓ plannedStart
✓ plannedFinish

und

✓ Bezug zur Rahmenaktivität
✓ erforderliche LBS-Zuordnung
```

Zusätzlich können einfache fachliche Konsistenzprüfungen erfolgen.

Beispielsweise:

```
Start < Ende
```

oder:

```
Detailaktivität gehört
zu einer freigegebenen
Rahmenaktivität
```

oder:

```
Detailaktivität liegt
innerhalb des vorgesehenen
Planungsbereichs
```

Damit wird sichergestellt, dass der Generalunternehmer die zurückgegebenen Daten automatisiert weiterverarbeiten kann.

---

## Ergebnis als Datenangebot bereitstellen

Nach erfolgreicher Prüfung stellt der Nachunternehmer seine Detailplanung über den bereits vorbereiteten Datenraumzugang bereit.

Beispielsweise:

```
Detailed Schedule

Project:
Project-X

Planning Assignment:
PA-100

Provider:
Nachunternehmer

Based on:
PCS-001

Semantic Profile:
Construct-X
```

Zu diesem Zeitpunkt muss der Generalunternehmer die Daten noch nicht unmittelbar übernehmen.

Der Nachunternehmer macht zunächst kenntlich:

> Für den Planungsauftrag PA-100 liegt ein neues Planungsergebnis vor.

Der eigentliche Abruf und die Integration erfolgen in Hauptprozess 5.

---

## Datenraumfunktion in diesem Hauptprozess

Die Datenraumfunktionen bleiben auch hier überschaubar.

Benötigt werden im Wesentlichen:

```
Nachunternehmer
      ↓
Detail Schedule registrieren
      ↓
Datenangebot bereitstellen
      ↓
Generalunternehmer erhält
Zugriff auf das Ergebnis
```

Die fachliche Beschreibung der Planung erfolgt nicht durch den Datenraum, sondern durch Construct-X.

Damit bleibt die Trennung:

```
Construct-X
     ↓
beschreibt Inhalt und Beziehungen


Datenraum
     ↓
regelt Bereitstellung und Zugriff
```

---

## Aufgaben der drei Teilnehmer

### Nachunternehmer

Der Nachunternehmer ist der zentrale Akteur dieses Hauptprozesses:

```
Planning Context verwenden
        ↓
Rahmenaktivität detaillieren
        ↓
Detailaktivitäten erzeugen
        ↓
Termine und Abhängigkeiten planen
        ↓
räumliche Zuordnungen übernehmen
        ↓
Ressourcen berücksichtigen
        ↓
Construct-X Export erzeugen
        ↓
Bezug zu Rahmenaktivität
und Planning Context herstellen
        ↓
SHACL prüfen
        ↓
Detail Schedule bereitstellen
```

---

### Generalunternehmer

Der Generalunternehmer führt in diesem Hauptprozess nur wenige aktive Schritte aus.

Seine zuvor bereitgestellten Informationen dienen als verbindlicher Planungskontext.

Er muss insbesondere sicherstellen, dass

```
Rahmenaktivitäten
+
Planungsrandbedingungen
+
Identitäten
```

für den Nachunternehmer weiterhin eindeutig referenzierbar bleiben.

Der eigentliche Abruf der fertigen Detailplanung erfolgt erst in Hauptprozess 5.

---

### Baulogistikdienstleister

Der Baulogistikdienstleister hat im Standardprozess keine aktive Aufgabe.

Seine Equipment-Daten werden innerhalb des bereitgestellten Planning Context verwendet.

Die ursprüngliche Identität und Herkunft dieser Informationen bleiben erhalten.

---

## Rolle der Ontologien in Hauptprozess 4

Die Construct-X-Ontologien erfüllen in diesem Hauptprozess insbesondere vier Aufgaben.

### Rahmen- und Detailplanung verbinden

Die neu erzeugten Aktivitäten können eindeutig mit der übergeordneten Aktivität des Generalunternehmers verbunden werden.

```
Framework Activity
        ↓
Detail Activities
```

### Gleiche Terminplansemantik verwenden

Rahmen- und Detailaktivitäten werden mit denselben grundlegenden Konzepten beschrieben:

```
Activity
PrecedenceRelationship
plannedStart
plannedFinish
```

Dadurch können beide Planungen später zusammengeführt werden.

### Räumliche Beziehungen erhalten

Die Detailaktivitäten können weiterhin auf die gemeinsam vereinbarte LBS-Struktur verweisen.

```
Detail Activity
      ↓
LBSNode
```

### Ressourcen eindeutig referenzieren

Bereits vorhandene Ressourcen wie ein Bauaufzug können referenziert werden, ohne sie erneut oder widersprüchlich zu beschreiben.

```
Detail Activity
      ↓
bestehendes SiteEquipment
```

Damit bildet Construct-X die semantische Verbindung zwischen dem vom Generalunternehmer vorgegebenen Planungskontext und der vom Nachunternehmer erzeugten Detailplanung.

---

## Ergebnis von Hauptprozess 4

Am Ende des Hauptprozesses liegt eine semantisch beschriebene und geprüfte Detailplanung vor.

Beispielsweise:

```
Detailed Schedule DS-001

Based on:
Planning Context PCS-001

Framework Activity:
A100

        │
        ├── NA-101
        ├── NA-102
        ├── NA-103
        ├── NA-104
        └── NA-105

LBS:
5. Obergeschoss

relevante Ressource:
ConstructionLift-4711

Provider:
Nachunternehmer
```

Damit bleibt die gesamte fachliche Kette nachvollziehbar:

```
Rahmenplanung
Generalunternehmer
        ↓
Planning Context
        ↓
Detailplanung
Nachunternehmer
```

Der Kern von Hauptprozess 4 lässt sich damit zusammenfassen:

```
Planning Context übernehmen
        ↓
im eigenen Fachsystem planen
        ↓
Rahmenaktivität detaillieren
        ↓
Detailaktivitäten eindeutig identifizieren
        ↓
Beziehungen zur Rahmenplanung erhalten
        ↓
Construct-X Detail Schedule erzeugen
        ↓
SHACL prüfen
        ↓
Planungsergebnis bereitstellen
```

Damit steht die Detailplanung für Hauptprozess 5 zur Verfügung, in dem der Generalunternehmer das Ergebnis abruft, prüft und in seinen Rahmenterminplan integriert.

# Hauptprozess 5 – Detailplanung übernehmen und integrieren

Im fünften Hauptprozess übernimmt der Generalunternehmer die vom Nachunternehmer erstellte Detailplanung.

Dabei wird nicht einfach eine Datei importiert. Zunächst wird geprüft,

- ob die Detailplanung zum richtigen Planungsauftrag gehört,
- ob sie auf dem vorgesehenen Planning Context basiert,
- ob die semantischen Beziehungen vollständig sind,
- ob die zeitlichen und räumlichen Randbedingungen eingehalten wurden,
- ob die Detailaktivitäten eindeutig der ursprünglichen Rahmenaktivität zugeordnet werden können.

Anschließend werden die Detailaktivitäten in das Terminplanungssystem des Generalunternehmers übernommen.

Der Hauptprozess beantwortet damit die Frage:

> **Wie wird die vom Nachunternehmer erzeugte Detailplanung kontrolliert in die Rahmenplanung des Generalunternehmers zurückgeführt?**

---

## Ausgangssituation

Aus Hauptprozess 4 liegt eine vom Nachunternehmer bereitgestellte Detailplanung vor.

Beispielsweise:

```
Detailed Schedule DS-001

Planning Assignment:
PA-100

Based on:
Planning Context PCS-001

Framework Activity:
A100 Ausbau 5. OG

Detail Activities:
NA-101
NA-102
NA-103
NA-104
NA-105
```

Der Generalunternehmer besitzt weiterhin seine ursprüngliche Rahmenplanung.

Damit bestehen zunächst zwei Planungsstände:

```
Generalunternehmer

Rahmenterminplan
      │
      └── A100 Ausbau 5. OG


Nachunternehmer

Detailplanung
      │
      ├── NA-101
      ├── NA-102
      ├── NA-103
      ├── NA-104
      └── NA-105
```

Diese beiden Planungsstände müssen nun kontrolliert miteinander verbunden werden.

---

## Generalunternehmer erkennt neues Planungsergebnis

Der Nachunternehmer hat seine Detailplanung als Datenangebot bereitgestellt.

Der Generalunternehmer erkennt, dass für den Planungsauftrag

```
PA-100
```

ein neues Ergebnis vorhanden ist.

Über den Datenraum wird zunächst geprüft:

```
Wer stellt die Daten bereit?
        ↓
Gehört das Ergebnis zum Projekt?
        ↓
Ist der Generalunternehmer berechtigt?
        ↓
Welcher Planungsauftrag ist betroffen?
```

Anschließend kann der Generalunternehmer die Detailplanung abrufen.

---

## Detailplanung übertragen

Die Detailplanung wird über den Datenraum übertragen.

Beispielsweise:

```
Nachunternehmer
      │
      │ Construct-X Detail Schedule
      ▼
Datenraum
      │
      ▼
Generalunternehmer
```

Der Datenraum übernimmt dabei wiederum nur den kontrollierten Austausch.

Die fachliche Bedeutung des Planungsergebnisses wird durch Construct-X beschrieben.

---

## Construct-X-Daten zunächst semantisch prüfen

Nach dem Empfang sollte der Generalunternehmer die Daten zunächst gegen das vereinbarte SHACL-Profil prüfen.

Beispielsweise:

```
DetailActivity vorhanden?
✓

identifier vorhanden?
✓

plannedStart vorhanden?
✓

plannedFinish vorhanden?
✓

Beziehung zur Rahmenaktivität vorhanden?
✓

LBS-Zuordnung vorhanden?
✓
```

Damit wird überprüft, ob die empfangenen Daten formal dem vereinbarten Austauschmodell entsprechen.

Eine technisch fehlerhafte oder unvollständige Detailplanung wird nicht unmittelbar in das interne Terminplanungssystem übernommen.

---

## Bezug zum Planungsauftrag prüfen

Als nächstes wird geprüft, ob die Detailplanung zum richtigen Planungsauftrag gehört.

Beispielsweise:

```
Detailed Schedule DS-001
        │
        └── Planning Assignment
                 ↓
              PA-100
```

Der Generalunternehmer kennt aus Hauptprozess 2 die Inhalte dieses Planungsauftrags.

Zum Beispiel:

```
PA-100

Nachunternehmer:
Subcontractor-A

zu detaillierende Activity:
A100

LBS:
5. Obergeschoss
```

Damit kann automatisch überprüft werden, ob der Nachunternehmer nur die vorgesehenen Planungsbereiche bearbeitet hat.

---

## Verwendeten Planning Context prüfen

Die Detailplanung sollte zusätzlich auf den Planning Context verweisen, auf dessen Grundlage sie erstellt wurde.

Beispielsweise:

```
Detailed Schedule DS-001
        │
        │ wasDerivedFrom
        ▼
Planning Context PCS-001
```

Dadurch weiß der Generalunternehmer genau, auf welchem Datenstand die Planung beruht.

Dies ist wichtig, weil sich zwischenzeitlich beispielsweise

- der Rahmenterminplan,
- die Baustelleneinrichtung,
- Equipment-Verfügbarkeiten

geändert haben können.

Der Generalunternehmer kann somit feststellen:

```
Ist PCS-001 noch aktuell?
```

oder:

```
Gab es seit PCS-001
relevante Änderungen?
```

---

## Beziehung zur Rahmenaktivität prüfen

Die wichtigste semantische Verbindung besteht zwischen den Detailaktivitäten des Nachunternehmers und der Rahmenaktivität des Generalunternehmers.

Beispielsweise:

```
A100 Ausbau 5. OG
        │
        ├── NA-101
        ├── NA-102
        ├── NA-103
        ├── NA-104
        └── NA-105
```

Damit kann der Generalunternehmer automatisch erkennen:

> Diese fünf Aktivitäten stellen die Detailplanung für A100 dar.

Ohne diese semantische Beziehung müsste die Zuordnung beispielsweise anhand von Namen, Codes oder manuellen Listen erfolgen.

Gerade hier entsteht ein wesentlicher Vorteil der gemeinsamen Ontologie.

---

## Zeitliche Konsistenz prüfen

Anschließend werden die zeitlichen Randbedingungen geprüft.

Die Rahmenaktivität besitzt beispielsweise:

```
A100

Start:
02.11.2026

Ende:
27.11.2026
```

Die Detailaktivitäten müssen dazu passen:

```
NA-101   02.11. – 05.11.
NA-102   06.11. – 10.11.
NA-103   11.11. – 16.11.
NA-104   17.11. – 21.11.
NA-105   22.11. – 25.11.
```

Automatisch kann geprüft werden:

```
frühester Start Detailplanung
        >=
Start Rahmenaktivität

und

spätestes Ende Detailplanung
        <=
Ende Rahmenaktivität
```

Zusätzlich können Vorgänger- und Nachfolgerbeziehungen geprüft werden.

Beispielsweise:

```
A090
   ↓
Detailplanung A100
   ↓
A120
```

Damit wird geprüft, ob die Detailplanung in den übergeordneten Terminplan passt.

---

## Räumliche Konsistenz prüfen

Auch die räumliche Zuordnung kann überprüft werden.

Aus dem Planungsauftrag ist bekannt:

```
A100
    ↓
LBS 5. Obergeschoss
```

Die Detailaktivitäten sollten deshalb ebenfalls diesem Bereich oder einem zulässigen Unterbereich zugeordnet sein.

Beispielsweise:

```
NA-101 → LBS 5. OG
NA-102 → LBS 5. OG
NA-103 → LBS 5. OG
```

Damit kann automatisch erkannt werden, wenn beispielsweise versehentlich eine Aktivität einem falschen Gebäudebereich zugeordnet wurde.

---

## Verwendung von Ressourcen prüfen

Wenn die Detailplanung auf bestimmte Baustellenressourcen verweist, können auch diese Beziehungen geprüft werden.

Beispielsweise:

```
NA-103
   │
   └── nutzt
        ConstructionLift-4711
```

Der Generalunternehmer kann prüfen, ob diese Ressource Bestandteil des ursprünglichen Planning Context war.

Dadurch ist sichergestellt, dass der Nachunternehmer nicht versehentlich auf eine unbekannte oder nicht freigegebene Ressource verweist.

Wichtig bleibt:

```
ConstructionLift-4711
```

behält weiterhin die ursprüngliche Identität des Baulogistikdienstleisters.

---

## Änderungen seit Erstellung des Planning Context erkennen

Zwischen der Bereitstellung des Planning Context und der Rückgabe der Detailplanung können sich Daten geändert haben.

Beispielsweise:

```
PCS-001 erzeugt
01.11.

Detailplanung zurückgegeben
10.11.

zwischenzeitliche Änderung:
A120 wurde vorgezogen
```

Da die Detailplanung auf `PCS-001` verweist, kann der Generalunternehmer gezielt prüfen, ob seitdem relevante Änderungen erfolgt sind.

Vereinfacht:

```
Planning Context PCS-001
        ↓
mit aktuellem Datenstand vergleichen
        ↓
relevante Änderung?
```

Falls keine relevante Änderung vorliegt:

```
→ Integration möglich
```

Falls relevante Änderungen vorliegen:

```
→ erneute Abstimmung erforderlich
```

Ein solcher Änderungs- oder Konfliktprozess kann später separat modelliert werden.

---

## Freigabe zur Integration

Erst wenn die Prüfungen erfolgreich abgeschlossen sind, wird die Detailplanung für die Integration freigegeben.

Beispielsweise:

```
Semantik gültig
      +
Planungsauftrag korrekt
      +
Planning Context bekannt
      +
Terminrahmen eingehalten
      +
räumliche Zuordnung korrekt
        ↓
Integration freigegeben
```

Diese Freigabe kann automatisiert, teilautomatisiert oder durch einen verantwortlichen Planer erfolgen.

---

## Construct-X auf internes Terminplanmodell abbilden

Die Detailplanung liegt weiterhin als Construct-X-Daten vor.

Für die Übernahme in das Terminplanungssystem des Generalunternehmers wird der bereits in Hauptprozess 1 vorbereitete Converter verwendet:

```
Construct-X
      ↓
Construct-X → Terminplanung Converter
      ↓
Terminplanungssystem
```

Dieser Converter kennt die Abbildung zwischen:

```
Construct-X Activity
        ↓
interne Terminplanaktivität
```

sowie beispielsweise:

```
plannedStart
plannedFinish
PrecedenceRelationship
```

und den entsprechenden Strukturen des Terminplanungssystems.

---

## Detailaktivitäten in den Rahmenterminplan integrieren

Die Detailaktivitäten werden der bestehenden Rahmenaktivität zugeordnet.

Aus:

```
A100 Ausbau 5. OG
```

wird im Terminplan beispielsweise:

```
A100 Ausbau 5. OG
 │
 ├── NA-101 Unterkonstruktion
 ├── NA-102 Installationen
 ├── NA-103 Trennwände
 ├── NA-104 Decke
 └── NA-105 Abschlussarbeiten
```

Die Rahmenaktivität bleibt erhalten.

Sie bildet weiterhin die übergeordnete Steuerungsebene des Generalunternehmers.

Die Detailaktivitäten ergänzen diese lediglich.

---

## Ursprüngliche Identitäten erhalten

Auch nach dem Import sollten die ursprünglichen Construct-X-Identitäten gespeichert bleiben.

Das interne Terminplanungssystem kann beispielsweise eine eigene technische ID vergeben:

```
MS Project ID:
4711
```

zusätzlich wird jedoch die externe Identität gespeichert:

```
Construct-X IRI:
https://data.subcontractor.example/activity/NA-101
```

Damit bleibt auch nach dem Import nachvollziehbar:

> Diese Aktivität wurde ursprünglich vom Nachunternehmer erzeugt.

Das ist wichtig für spätere Aktualisierungen.

---

## Herkunft und Verantwortlichkeit erhalten

Der integrierte Terminplan enthält nun Informationen verschiedener Beteiligter.

Beispielsweise:

```
A100
Provider:
Generalunternehmer


NA-101
Provider:
Nachunternehmer


ConstructionLift-4711
Provider:
Baulogistikdienstleister
```

Die Integration bedeutet also nicht, dass sämtliche Informationen anschließend dem Generalunternehmer zugerechnet werden.

Die Herkunft der jeweiligen Informationen bleibt erhalten.

---

## Aktualisierung statt Duplizierung ermöglichen

Die stabilen Identitäten ermöglichen auch spätere Aktualisierungen.

Wenn der Nachunternehmer beispielsweise eine neue Version seiner Detailplanung bereitstellt:

```
NA-103
plannedFinish:

alt:
16.11.

neu:
18.11.
```

kann der Generalunternehmer anhand der Identität erkennen:

```
Es handelt sich nicht um
eine neue Aktivität,

sondern um eine Aktualisierung
von NA-103.
```

Dadurch können Dubletten vermieden werden.

---

## Integrierten Planungsstand dokumentieren

Nach erfolgreicher Integration sollte der neue Planungsstand eindeutig dokumentiert werden.

Beispielsweise:

```
Integrated Schedule Version:
IS-2026-11-10-01
```

mit Bezug auf:

```
Framework Schedule
+
Detailed Schedule DS-001
+
Planning Context PCS-001
```

Damit entsteht eine nachvollziehbare Kette:

```
Rahmenterminplan
       ↓
Planning Assignment
       ↓
Planning Context
       ↓
Detailed Schedule
       ↓
Integrated Schedule
```

---

## Rolle des Nachunternehmers

Der Nachunternehmer besitzt in diesem Hauptprozess zunächst keine aktive Aufgabe mehr.

Er hat seine Detailplanung bereits bereitgestellt.

Falls der Generalunternehmer jedoch Fehler oder Konflikte feststellt, kann eine Rückmeldung an den Nachunternehmer erfolgen.

Beispielsweise:

```
Detailplanung abgelehnt

Grund:
Terminrahmen überschritten
```

Ein solcher Korrekturprozess würde anschließend erneut in die Detailplanung führen.

Für den Standardprozess wird zunächst davon ausgegangen, dass die Planung erfolgreich geprüft und integriert werden kann.

---

## Rolle des Baulogistikdienstleisters

Auch der Baulogistikdienstleister besitzt im Standardfall keine aktive Aufgabe.

Seine Daten werden weiterhin lediglich referenziert.

Sollte bei der Prüfung festgestellt werden, dass sich beispielsweise die Verfügbarkeit eines Bauaufzugs geändert hat, kann daraus ein separater Abstimmungsprozess entstehen.

Dies gehört jedoch nicht zum einfachen Standardablauf.

---

## Rolle der Ontologien in Hauptprozess 5

Die Construct-X-Ontologien übernehmen erneut mehrere zentrale Funktionen.

### Automatische Zuordnung ermöglichen

Die Detailaktivitäten können eindeutig der Rahmenaktivität zugeordnet werden.

```
DetailActivity
      ↓
FrameworkActivity
```

Damit entfällt eine manuelle Zuordnung anhand von Bezeichnungen.

### Konsistenz prüfen

Terminliche, räumliche und organisatorische Beziehungen können automatisch ausgewertet werden.

Beispielsweise:

```
Activity
   ↓
LBSNode
```

oder:

```
Activity
   ↓
PrecedenceRelationship
   ↓
Activity
```

### Unterschiedliche Fachsysteme verbinden

Der Nachunternehmer muss das Terminplanungssystem des Generalunternehmers nicht kennen.

Beide Systeme bilden lediglich auf Construct-X ab:

```
Planungssystem Nachunternehmer
        ↓
Construct-X
        ↓
Terminplanungssystem Generalunternehmer
```

Dadurch wird eine direkte proprietäre Schnittstelle zwischen beiden Systemen vermieden.

### Herkunft erhalten

Die gemeinsamen Ontologien ermöglichen, Ressourcen verschiedener Organisationen miteinander zu verknüpfen, ohne deren Identität zu verlieren.

---

## Aufgaben der drei Teilnehmer

### Generalunternehmer

Der Generalunternehmer ist der zentrale Akteur:

```
Detailplanung abrufen
        ↓
SHACL prüfen
        ↓
Planning Assignment prüfen
        ↓
Planning Context prüfen
        ↓
Bezug zur Rahmenaktivität prüfen
        ↓
zeitliche Konsistenz prüfen
        ↓
räumliche Konsistenz prüfen
        ↓
Integration freigeben
        ↓
Construct-X konvertieren
        ↓
in Rahmenterminplan integrieren
        ↓
neuen Planungsstand speichern
```

---

### Nachunternehmer

Der Nachunternehmer:

```
stellt Detailplanung bereit

und

reagiert nur bei
Rückfragen oder Konflikten
```

---

### Baulogistikdienstleister

Der Baulogistikdienstleister:

```
bleibt Quelle der
referenzierten Equipment-Daten
```

und besitzt im normalen Integrationsprozess keine zusätzliche aktive Aufgabe.

---

## Ergebnis von Hauptprozess 5

Am Ende des fünften Hauptprozesses besitzt der Generalunternehmer einen integrierten Terminplan.

Beispielsweise:

```
Rahmenterminplan

A090 Rohbau 5. OG
   ↓

A100 Ausbau 5. OG
 │
 ├── NA-101 Unterkonstruktion
 ├── NA-102 Installationen
 ├── NA-103 Trennwände
 ├── NA-104 Decke
 └── NA-105 Abschlussarbeiten

   ↓
A120 Übergabe 5. OG
```

Dabei bleiben weiterhin nachvollziehbar:

```
wer
welche Information

wann

auf Basis welchen
Datenstands

bereitgestellt hat.
```

Der vollständige Informationsfluss ist damit geschlossen:

```
Generalunternehmer
Rahmenplanung
       ↓
Planning Assignment
       ↓
Planning Context
       ↓
Nachunternehmer
Detailplanung
       ↓
Detailed Schedule
       ↓
Generalunternehmer
integrierte Planung
```

Der Kern von Hauptprozess 5 lässt sich somit zusammenfassen:

```
Detailplanung abrufen
        ↓
semantisch prüfen
        ↓
Planungsauftrag und Datenstand prüfen
        ↓
fachliche Konsistenz prüfen
        ↓
freigeben
        ↓
in internes Terminplanmodell konvertieren
        ↓
Detailaktivitäten integrieren
        ↓
integrierten Planungsstand dokumentieren
```

Damit ist der organisationsübergreifende Planungszyklus abgeschlossen.
