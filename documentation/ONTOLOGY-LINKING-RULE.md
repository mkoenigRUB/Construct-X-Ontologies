# Construct-X Ontology Linking Rule

## Principle

Relations between classes that belong to different domain ontologies are **never defined in either source ontology**.

They are defined in a separate **link ontology**.

```text
Ontology A                Ontology B
    │                         │
    └──────── Link Ontology ──┘
```

The link ontology:

- imports the exact released versions of both source ontologies;
- defines only the cross-domain ObjectProperties and, where needed, their SHACL constraints;
- must not redefine classes or properties from the source ontologies;
- keeps both source ontologies independently reusable;
- avoids circular imports.

## Example: Schedule ↔ Breakdown

Source ontologies:

```text
construction-schedule
    ConstructionSchedule
    Activity
    Milestone
    PrecedenceRelationship

breakdown-structure
    WorkBreakdownStructure
    LocationBreakdownStructure
    WBSNode
    LBSNode
```

External link ontology:

```text
schedule-breakdown-link
    usesWorkBreakdownStructure
    usesLocationBreakdownStructure
    isClassifiedByWBSNode
    isPerformedIn
```

Example:

```text
Activity
    ├─ isClassifiedByWBSNode ──► WBSNode
    └─ isPerformedIn ──────────► LBSNode
```

Neither `construction-schedule` nor `breakdown-structure` contains these cross-domain relations.

## Naming

Recommended module pattern:

```text
{ontology-a}-{ontology-b}-link
```

For example:

```text
schedule-breakdown-link
schedule-boq-link
boq-product-link
schedule-spatial-link
```

## Vocabularies

Controlled vocabularies are not domain ontologies and do not require a link ontology merely because a domain property has range `skos:Concept`.

Examples:

```text
Activity --hasStatus---------> Activity Status vocabulary
ConstructionSchedule --scheduleType--> Schedule Type vocabulary
PrecedenceRelationship --relationshipType--> Relationship Type vocabulary
```

The concrete allowed vocabulary is selected through optional SHACL profiles.

## Validation

A package-level architecture check should verify that:

1. no source ontology imports another source domain ontology;
2. no ObjectProperty in a source ontology has its domain in that ontology and its range in another Construct-X domain ontology;
3. cross-domain ObjectProperties occur only in dedicated link ontologies;
4. link ontologies import the exact released versions of all source ontologies they connect.
