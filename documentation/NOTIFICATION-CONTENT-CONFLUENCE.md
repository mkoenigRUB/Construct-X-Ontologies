# Notification Content Ontologie (Draft)

**Namespace:** `https://www.construct-x.org/ontology/notification-content#`  
**Version:** `0.1.1`  
**Prefix:** `conx-nc`

Die Ontologie modelliert den **fachsemantischen Inhalt** einer Benachrichtigung im
Construct-X-Austausch. Transport- und Routing-Metadaten (messageId, Sender, Empfänger,
Zeitstempel, relatedMessageId) werden bewusst **nicht** modelliert – sie verbleiben im
externen Notification-Header (z. B. Industry Core / Tractus-X). Damit bleibt der
fachliche Inhalt transportneutral und wiederverwendbar.

Eine `NotificationContent` trägt einen `notificationType` (SKOS-Konzept) und je nach
Typ optionale `taskType`, `taskStatus` sowie eine oder mehrere `SubjectAssignment`, die
die referenzierten Objekte mit ihrer Rolle (`Target` / `ContextOnly`) kennzeichnen.

## Klassen

| Klasse | Deutsch | Fachliche Bedeutung |
|---|---|---|
| `NotificationContent` | Benachrichtigungsinhalt | Fachsemantischer Inhalt innerhalb eines technischen Notification-Umschlags. |
| `SubjectAssignment` | Objektzuordnung | Ordnet einem referenzierten Objekt seine Rolle innerhalb der Benachrichtigung zu. |

## Eigenschaften von NotificationContent

| Property | Wertebereich | Kardinalität | Fachliche Bedeutung |
|---|---|---:|---|
| `notificationType` | `skos:Concept` | **1..1** | Klassifiziert die fachliche Bedeutung der Benachrichtigung. |
| `taskType` | `skos:Concept` | 0..1 | Angeforderter Aufgabentyp (bei `TaskRequested` und auftragsbezogenen Folgemeldungen). |
| `taskStatus` | `skos:Concept` | 0..1 | In einer Statusbenachrichtigung mitgeteilter Bearbeitungsstatus. |
| `contextResource` | `owl:Thing` | 0..1 | Verweist auf einen eigenständigen fachlichen Dateninhalt, der den Kontext bereitstellt. |
| `hasResult` | `owl:Thing` | 0..n | Durch die Benachrichtigung bereitgestelltes Ergebnisobjekt. |
| `hasSubjectAssignment` | `SubjectAssignment` | 0..n | Verknüpft die Benachrichtigung mit einem oder mehreren Ziel-/Kontextobjekten. |

## Eigenschaften von SubjectAssignment

| Property | Wertebereich | Kardinalität | Fachliche Bedeutung |
|---|---|---:|---|
| `assignedResource` | `owl:Thing` | **1..1** | Von der Benachrichtigung referenziertes Objekt. |
| `subjectRole` | `skos:Concept` | **1..1** | Rolle des Objekts: `Target` (Adressat einer Anforderung) oder `ContextOnly` (nur Kontext). |

## SKOS-Vokabulare

Die Core-Eigenschaften haben im Core den Wertebereich `skos:Concept`. Über das
Core-SHACL-Profil werden sie auf die folgenden Construct-X-Vokabulare gebunden
(`sh:in`, geschlossene Mengen):

- **notification-type** (`conx-nt`): `DataAvailable`, `DataUpdated`, `DataDeleted`,
  `TaskRequested`, `TaskStatusChanged`, `ResultAvailable`
- **task-type** (`conx-tt`): `DetailedScheduling`, `ProgressReporting`, `PriceCalculation`
- **task-status** (`conx-ts`): `Accepted`, `InProgress`, `Completed`, `Rejected`, `Cancelled`
- **subject-role** (`conx-sr`): `Target`, `ContextOnly`

## Core-SHACL-Regeln

- `notificationType` ist verpflichtend und muss exakt ein Vokabular-Konzept sein.
- `taskStatus` muss, falls vorhanden, exakt ein Vokabular-Konzept sein.
- `taskType` muss, falls vorhanden, exakt ein Vokabular-Konzept sein.
- `SubjectAssignment`: `assignedResource` und `subjectRole` sind verpflichtend;
  `subjectRole` muss `Target` oder `ContextOnly` sein.

**Fachliche SPARQL-Regeln (abhängig vom notificationType):**

| notificationType | Regel |
|---|---|
| `TaskRequested` | Exakt ein `taskType` **und** mindestens ein `SubjectAssignment` mit Rolle `Target`. |
| `TaskRequested` + `taskType = DetailedScheduling` | Exakt eine `contextResource`. |
| `TaskStatusChanged` | Exakt ein `taskStatus`. |
| `DataAvailable` / `DataUpdated` / `DataDeleted` | Mindestens ein `SubjectAssignment` mit Rolle `Target`. |
| `ResultAvailable` | Mindestens ein `hasResult`. |

Die Regeln sind als `sh:SPARQLConstraint` formuliert und wirken nur auf die jeweiligen
`notificationType`-Werte – eine `ResultAvailable`-Benachrichtigung beispielsweise muss
kein `taskStatus` tragen.

## Beispiel

```turtle
@prefix conx-nc:  <https://www.construct-x.org/ontology/notification-content#> .
@prefix conx-nt:  <https://www.construct-x.org/vocab/notification-content/notification-type#> .
@prefix conx-tt:  <https://www.construct-x.org/vocab/notification-content/task-type#> .
@prefix conx-ts:  <https://www.construct-x.org/vocab/notification-content/task-status#> .
@prefix conx-sr:  <https://www.construct-x.org/vocab/notification-content/subject-role#> .

# Angeforderte Feinterminplanung (TaskRequested)
ex:nc-detail-001
    a conx-nc:NotificationContent ;
    conx-nc:notificationType conx-nt:TaskRequested ;
    conx-nc:taskType conx-tt:DetailedScheduling ;
    conx-nc:contextResource ex:pcs-001 ;
    conx-nc:hasSubjectAssignment ex:sa-a100 .

ex:sa-a100
    a conx-nc:SubjectAssignment ;
    conx-nc:assignedResource ex:a100 ;
    conx-nc:subjectRole conx-sr:Target .

# Statusänderung derselben Aufgabe (TaskStatusChanged)
ex:nc-detail-002
    a conx-nc:NotificationContent ;
    conx-nc:notificationType conx-nt:TaskStatusChanged ;
    conx-nc:taskStatus conx-ts:InProgress ;
    conx-nc:contextResource ex:pcs-001 ;
    conx-nc:hasSubjectAssignment ex:sa-a100 .

# Ergebnis verfügbar (ResultAvailable)
ex:nc-detail-003
    a conx-nc:NotificationContent ;
    conx-nc:notificationType conx-nt:ResultAvailable ;
    conx-nc:contextResource ex:pcs-001 ;
    conx-nc:hasResult ex:detail-schedule-001 ;
    conx-nc:hasSubjectAssignment ex:sa-a100 .
```

Das Beispiel spiegelt die Referenzbenachrichtigung
`examples/construct-x-doppelboden-beispieldaten/notification/doppelboden-task-request.json`.

## Umgang mit Änderungen

Eine `NotificationContent` ist ein **zeitpunktbezogener, unveränderlicher Datensatz**:
jeder Statuswechsel oder jede neue Anforderung erzeugt eine neue Benachrichtigung.
Historische Benachrichtigungen werden nicht überschrieben – der Verlauf ergibt sich aus
der Abfolge der `TaskStatusChanged`-/`ResultAvailable`-Meldungen desselben
`contextResource`.
