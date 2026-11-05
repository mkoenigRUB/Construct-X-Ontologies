# Breakdown Structure Ontologie (Draft)

**Namespace:** `https://www.construct-x.org/ontology/breakdown-structure#`  
**Version:** `0.6.0`

Die Ontologie beschreibt generische hierarchische Gliederungsstrukturen. Sie unterscheidet Work, Location, System und Cost Breakdown Structures. Die fachliche Bedeutung eines Knotens wird über `nodeType` mit einem kontrollierten SKOS-Vokabular beschrieben.

## Klassen

| Klasse | Deutsch | Fachliche Bedeutung |
|---|---|---|
| `BreakdownStructure` | Gliederungsstruktur | Allgemeine hierarchische Struktur. |
| `WorkBreakdownStructure` | Work Breakdown Structure / Projektstrukturplan | Gliederung des Arbeits- bzw. Leistungsumfangs. |
| `LocationBreakdownStructure` | räumliche Gliederungsstruktur | Gliederung nach physischen oder logischen Orten. |
| `SystemBreakdownStructure` | Systemgliederungsstruktur | Gliederung nach Systemen, Baugruppen, Elementen oder Komponenten. |
| `CostBreakdownStructure` | Kostengliederungsstruktur | Gliederung nach Kostenbereichen bzw. Kostenklassifikationen. |
| `BreakdownNode` | Gliederungsknoten | Allgemeiner Knoten einer Gliederungsstruktur. |
| `WBSNode` | WBS-/PSP-Knoten | Knoten einer WBS. |
| `LBSNode` | LBS-Knoten | Knoten einer LBS. |
| `SBSNode` | SBS-Knoten | Knoten einer SBS. |
| `CBSNode` | CBS-Knoten | Knoten einer CBS. |

## Eigenschaften von BreakdownStructure

| Property | Wertebereich | Kardinalität | Beschreibung |
|---|---|---:|---|
| `identifier` | `xsd:string` | **1..1** | Verpflichtende fachliche Kennung. |
| `name` | `xsd:string` | **0..1** | Optionale menschenlesbare Bezeichnung. |
| `hasNode` | `BreakdownNode` | 1..n | Zugehörige Knoten. |
| `hasRootNode` | `BreakdownNode` | 1..n | Wurzelknoten; Subproperty von `hasNode`. |

Die vier Struktur-Unterklassen erben diese Eigenschaften. Das Core-SHACL-Profil beschränkt `hasNode` und `hasRootNode` jeweils auf `WBSNode`, `LBSNode`, `SBSNode` bzw. `CBSNode`.

## Eigenschaften von BreakdownNode

| Property | Wertebereich | Kardinalität | Beschreibung |
|---|---|---:|---|
| `identifier` | `xsd:string` | **1..1** | Verpflichtende fachliche Kennung des Knotens. |
| `name` | `xsd:string` | **0..1** | Optionale menschenlesbare Bezeichnung. |
| `code` | `xsd:string` | 0..1 | Optionaler Fach-/Klassifikationscode. |
| `level` | `xsd:nonNegativeInteger` | 0..1 | Optionale numerische Hierarchieebene. |
| `nodeType` | `skos:Concept` | 0..1 im Core | Fachlicher Knotentyp; in DE-Profilen genau ein Wert aus dem jeweiligen Vokabular. |
| `isSubNodeOf` | `BreakdownNode` | 0..1 | Direkter Elternknoten. |
| `hasSubNode` | `BreakdownNode` | 0..n | Direkte Unterknoten; invers zu `isSubNodeOf`. |

`WBSNode`, `LBSNode`, `SBSNode` und `CBSNode` erben diese Eigenschaften. Der direkte Elternknoten muss jeweils vom gleichen Knotentyp sein.

## Vokabulare

| Node | Prefix | Term Namespace |
|---|---|---|
| `WBSNode` | `conx-de-wbs` | `https://www.construct-x.org/vocab/breakdown-structure/de-wbs-node-type#` |
| `LBSNode` | `conx-de-lbs` | `https://www.construct-x.org/vocab/breakdown-structure/de-lbs-node-type#` |
| `SBSNode` | `conx-de-sbs` | `https://www.construct-x.org/vocab/breakdown-structure/de-sbs-node-type#` |
| `CBSNode` | `conx-de-cbs` | `https://www.construct-x.org/vocab/breakdown-structure/de-cbs-node-type#` |

Die Einträge der Vokabulare sind technisch `skos:Concept`; in der Dokumentation können sie als `Vocabulary Term` bezeichnet werden.

## Versionierung

WBS, LBS, SBS und CBS werden als versionierbare Hauptartefakte behandelt. Stabile Identität und unveränderliche Snapshots werden getrennt. Knoten behalten grundsätzlich stabile IRIs; historische Zustände können in Snapshot-Named-Graphs gespeichert werden.
