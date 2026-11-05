# Construction Schedule Ontologie (Draft)

**Namespace:** `https://www.construct-x.org/ontology/construction-schedule#`  
**Version:** `0.5.0`  
**Link:** `construction-schedule.ttl`

Die Ontologie beschreibt einen konkreten Bauablauf- bzw. Terminplan, dessen Vorgänge, Meilensteine, Termine und logische Anordnungsbeziehungen.

## Klassen

| Klasse | Deutsch | Fachliche Beschreibung |
|---|---|---|
| `ConstructionSchedule` | Bauablaufplan / Terminplan | Konkreter Terminplan eines Projekts. |
| `Activity` | Vorgang | Konkreter Vorgang innerhalb eines Terminplans. |
| `Milestone` | Meilenstein / Schlüsselereignis | Zeitlich punktuelles Ereignis; Unterklasse von `Activity`. |
| `PrecedenceRelationship` | Anordnungsbeziehung | Logische Beziehung zwischen Vorgänger- und Nachfolgervorgang. |

## Eigenschaften von ConstructionSchedule

| Property | Wertebereich | Beschreibung |
|---|---|---|
| `identifier` | `xsd:string` | Fachliche Kennung des Terminplans. |
| `name` | `xsd:string` | Bezeichnung des Terminplans. |
| `scheduleType` | `skos:Concept` | Typ bzw. Einordnung des Terminplans; mehrere Typen möglich. |
| `hasActivity` | `Activity` | Ordnet dem Terminplan einen Vorgang zu. |
| `hasMilestone` | `Milestone` | Ordnet dem Terminplan einen expliziten Meilenstein zu; Subproperty von `hasActivity`. |

## Eigenschaften von Activity

| Property | Wertebereich | Beschreibung |
|---|---|---|
| `identifier` | `xsd:string` | Fachliche Kennung des Vorgangs. |
| `hierarchyCode` | `xsd:string` | Strukturierte Kennung der Position innerhalb der hierarchischen Gliederung des Terminplans. |
| `name` | `xsd:string` | Bezeichnung des Vorgangs. |
| `description` | `xsd:string` | Kurzbeschreibung der Aktivität. |
| `hasStatus` | `skos:Concept` | Aktueller Ausführungsstatus. |
| `isSubActivityOf` | `Activity` | Direkter übergeordneter Vorgang. |
| `hasSubActivity` | `Activity` | Direkter untergeordneter Vorgang. |
| `plannedStart` | `xsd:dateTime` | Geplanter Anfangstermin. |
| `plannedFinish` | `xsd:dateTime` | Geplanter Endtermin. |
| `earliestStart` | `xsd:dateTime` | Frühester Anfangstermin. |
| `earliestFinish` | `xsd:dateTime` | Frühester Endtermin. |
| `latestStart` | `xsd:dateTime` | Spätester Anfangstermin. |
| `latestFinish` | `xsd:dateTime` | Spätester Endtermin. |

## Milestone

`Milestone` ist Unterklasse von `Activity`. Für einen Meilenstein gilt:

```text
plannedStart = plannedFinish
```

## Eigenschaften von PrecedenceRelationship

| Property | Wertebereich | Beschreibung |
|---|---|---|
| `identifier` | `xsd:string` | Optionale Kennung. |
| `name` | `xsd:string` | Optionale Bezeichnung. |
| `hasPredecessor` | `Activity` | Vorgänger. |
| `hasSuccessor` | `Activity` | Nachfolger. |
| `relationshipType` | `skos:Concept` | Typ der Anordnungsbeziehung. |
| `lag` | `xsd:duration` | Zeitabstand zwischen Vorgänger und Nachfolger. |

## Externe Verknüpfungen

Domänenübergreifende Beziehungen werden ausschließlich in separaten Link-Ontologien definiert.

## Vokabulare

- Schedule Type: `https://www.construct-x.org/vocab/construction-schedule/schedule-type#`
- Activity Status: `https://www.construct-x.org/vocab/construction-schedule/activity-status#`
- Precedence Relationship Type: `https://www.construct-x.org/vocab/construction-schedule/precedence-relationship-type#`

Die konkreten Werte sind `skos:Concept`-Instanzen in separaten `skos:ConceptScheme`s.
