import org.apache.jena.rdf.model.Literal;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;

/**
 * Verifiziert den Construct-X JSON-LD-Kontext:
 * 1. Test-Dokument (Bare Terms + Praefix-Terms inkl. aller 17 Kollisionsfaelle)
 *    wird mit dem lokalen Kontext expandiert
 * 2. Alle erwarteten Ontologie-IRIs muessen exakt auftauchen
 * 3. Roundtrip: expanded Model -> JSON-LD -> expanded -> gleiche Triple-Angabe
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Path doc = Path.of(args[0]);

        // 1) expandieren (Kontext wird aus dem Dokument per relativem Pfad geladen)
        Model data = ModelFactory.createDefaultModel();
        RDFDataMgr.read(data, doc.toUri().toString(), Lang.JSONLD);
        Set<String> iris = new HashSet<>();
        data.listStatements().toList().forEach(s -> {
            iris.add(s.getSubject().toString());
            iris.add(s.getPredicate().toString());
            if (s.getObject().isResource()) {
                iris.add(s.getObject().asResource().toString());
            } else if (s.getObject().isLiteral()) {
                var dt = ((Literal) s.getObject()).getDatatype();
                if (dt != null) iris.add(dt.getURI());
            }
        });
        System.out.println("Expandiert: " + data.size() + " Triples, " + iris.size() + " IRIs");

        String[][] expected = {
            // N1 ConstructionSchedule
            {"https://data.construct-x.org/project/X/schedule/SCH-01", "N1 Subjekt SCH-01"},
            {"https://www.construct-x.org/ontology/construction-schedule#ConstructionSchedule", "N1 @type conx-cs:ConstructionSchedule"},
            {"https://www.construct-x.org/ontology/construction-schedule#scheduleType", "N1 bare scheduleType (@id-Coercion)"},
            {"https://www.construct-x.org/vocab/construction-schedule/schedule-type#RoughNetwork", "N1 scheduleType-Wert (conx-st:RoughNetwork)"},
            {"https://www.construct-x.org/ontology/construction-schedule#hasActivity", "N1 bare hasActivity (@id-Coercion)"},
            {"https://data.construct-x.org/project/X/schedule/ACT-01", "N1 hasActivity-Wert ACT-01"},
            {"https://www.construct-x.org/ontology/construction-schedule#plannedStart", "N1 conx-cs:plannedStart (Kollision)"},
            {"http://www.w3.org/2001/XMLSchema#dateTime", "N1-N5 Datatype xsd:dateTime"},
            {"https://www.construct-x.org/ontology/construction-schedule#plannedFinish", "N1 conx-cs:plannedFinish (Kollision)"},
            {"https://www.construct-x.org/ontology/construction-schedule#description", "N1 conx-cs:description (Kollision)"},
            {"https://www.construct-x.org/ontology/construction-schedule#hierarchyCode", "N1 conx-cs:hierarchyCode (Kollision)"},
            // N2 Activity
            {"https://www.construct-x.org/ontology/construction-schedule#Activity", "N2 @type conx-cs:Activity"},
            {"https://www.construct-x.org/ontology/construction-schedule#hasStatus", "N2 conx-cs:hasStatus (Kollision)"},
            {"https://www.construct-x.org/vocab/construction-schedule/activity-status#InProgress", "N2 hasStatus-Wert (conx-status:InProgress)"},
            {"https://www.construct-x.org/ontology/construction-schedule#earliestStart", "N2 bare earliestStart (String-Mapping)"},
            {"https://www.construct-x.org/ontology/schedule-breakdown-link#isClassifiedByWBSNode", "N2 bare isClassifiedByWBSNode (@id-Coercion)"},
            {"https://data.construct-x.org/project/X/wbs/WBS-001", "N2 isClassifiedByWBSNode-Wert WBS-001"},
            // N3 LogisticsLoad
            {"https://data.construct-x.org/project/X/delivery/LOAD-001", "N3 Subjekt LOAD-001"},
            {"https://www.construct-x.org/ontology/construction-delivery#LogisticsLoad", "N3 @type conx-del:LogisticsLoad"},
            {"https://www.construct-x.org/ontology/construction-delivery#hasStatus", "N3 conx-del:hasStatus (Kollision)"},
            {"https://www.construct-x.org/vocab/construction-delivery/requirement-status#InProgress", "N3 hasStatus-Wert (conx-drs:InProgress)"},
            {"https://www.construct-x.org/ontology/construction-delivery#plannedStart", "N3 conx-del:plannedStart (Kollision)"},
            {"https://www.construct-x.org/ontology/construction-delivery#quantity", "N3 conx-del:quantity (Kollision)"},
            {"http://www.w3.org/2001/XMLSchema#decimal", "N3/N4 Datatype xsd:decimal"},
            {"https://www.construct-x.org/ontology/construction-delivery#unitCode", "N3 conx-del:unitCode (Kollision)"},
            {"https://qudt.org/vocab/unit/m3", "N3/N4 unitCode-Wert (unit:m3)"},
            // N4 BoQItem
            {"https://data.construct-x.org/project/X/gaeb/POS-001", "N4 Subjekt POS-001"},
            {"https://www.construct-x.org/ontology/gaeb-boq#BoQItem", "N4 @type conx-gaeb:BoQItem"},
            {"https://www.construct-x.org/ontology/gaeb-boq#quantity", "N4 conx-gaeb:quantity (Kollision)"},
            {"https://www.construct-x.org/ontology/gaeb-boq#unitCode", "N4 conx-gaeb:unitCode (Kollision)"},
            {"https://www.construct-x.org/ontology/gaeb-boq#identifier", "N4 conx-gaeb:identifier"},
            // N5 ConstructionProgressReport
            {"https://data.construct-x.org/project/X/progress/CPR-001", "N5 Subjekt CPR-001"},
            {"https://www.construct-x.org/ontology/construction-progress-report#ConstructionProgressReport", "N5 @type conx-cpr:ConstructionProgressReport"},
            {"https://www.construct-x.org/ontology/construction-progress-report#activityStatus", "N5 bare activityStatus (@id-Coercion)"},
            {"https://www.construct-x.org/vocab/construction-schedule/activity-status#Completed", "N5 activityStatus-Wert (conx-status:Completed)"},
            {"https://www.construct-x.org/ontology/construction-progress-report#actualStart", "N5 conx-cpr:actualStart (Kollision)"},
            {"https://www.construct-x.org/ontology/construction-progress-report#actualFinish", "N5 conx-cpr:actualFinish (Kollision)"},
            // N6 BuiltAsset
            {"https://data.construct-x.org/project/X/asset/BA-001", "N6 Subjekt BA-001"},
            {"https://www.construct-x.org/ontology/built-asset#BuiltAsset", "N6 @type conx-ba:BuiltAsset"},
            {"https://www.construct-x.org/ontology/built-asset#hierarchyCode", "N6 conx-ba:hierarchyCode (Kollision)"},
            {"https://www.construct-x.org/ontology/built-asset#hasSpatialStructureType", "N6 conx-ba:hasSpatialStructureType (Kollision)"},
            {"https://www.construct-x.org/vocab/built-asset/spatial-structure-type#Storey", "N6 hasSpatialStructureType-Wert (conx-bst:Storey)"},
            // N7 ConstructionSite
            {"https://data.construct-x.org/project/X/site/SITE-001", "N7 Subjekt SITE-001"},
            {"https://www.construct-x.org/ontology/construction-site#ConstructionSite", "N7 @type conx-site:ConstructionSite"},
            {"https://www.construct-x.org/ontology/construction-site#name", "N7 conx-site:name"},
            {"https://www.construct-x.org/ontology/construction-site#description", "N7 conx-site:description (Kollision)"},
            // N8 GEOM (GeoSPARQL, kein @type)
            {"https://data.construct-x.org/project/X/site/GEOM-001", "N8 Subjekt GEOM-001"},
            {"http://www.opengis.net/ont/geosparql#hasGeometry", "N8 geo:hasGeometry (kein Kontext-Term)"},
            {"https://example.org/geom/1", "N8 hasGeometry-Wert (unregistrierte IRI)"},
            // N9 NotificationContent
            {"https://data.construct-x.org/project/X/notification/NC-001", "N9 Subjekt NC-001"},
            {"https://www.construct-x.org/ontology/notification-content#NotificationContent", "N9 @type conx-nc:NotificationContent"},
            {"https://www.construct-x.org/ontology/notification-content#taskStatus", "N9 bare taskStatus (@id-Coercion)"},
            {"https://www.construct-x.org/vocab/notification-content/task-status#Cancelled", "N9 taskStatus-Wert (conx-ts:Cancelled)"},
            {"https://www.construct-x.org/ontology/notification-content#taskType", "N9 bare taskType (@id-Coercion)"},
            {"https://www.construct-x.org/vocab/notification-content/task-type#DetailedScheduling", "N9 taskType-Wert (conx-tt:DetailedScheduling)"},
            {"https://www.construct-x.org/ontology/notification-content#notificationType", "N9 bare notificationType (@id-Coercion)"},
            {"https://www.construct-x.org/vocab/notification-content/notification-type#TaskRequested", "N9 notificationType-Wert (conx-nt:TaskRequested)"},
            {"http://www.w3.org/2000/01/rdf-schema#seeAlso", "N9 bare seeAlso (@id-Coercion)"},
            // N10 WBS-Node mit Link-Properties
            {"https://www.construct-x.org/ontology/schedule-breakdown-link#isClassifiedByCBSNode", "N10 conx-sbl:isClassifiedByCBSNode (Kollision)"},
            {"https://data.construct-x.org/project/X/cbs/CBS-001", "N10 isClassifiedByCBSNode-Wert CBS-001"},
            {"https://www.construct-x.org/ontology/site-breakdown-link#isRepresentedByLBSNode", "N10 conx-sbdl:isRepresentedByLBSNode (Kollision)"},
            {"https://www.construct-x.org/vocab/breakdown-structure/de-lbs-node-type#Storey", "N10 isRepresentedByLBSNode-Wert (conx-de-lbs:Storey)"},
            {"https://www.construct-x.org/ontology/built-asset-breakdown-link#isRepresentedByLBSNode", "N10 conx-babl:isRepresentedByLBSNode (Kollision)"},
            {"https://www.construct-x.org/ontology/built-asset-breakdown-link#isClassifiedByCBSNode", "N10 conx-babl:isClassifiedByCBSNode (Kollision)"}
        };
        int failures = 0;
        for (String[] e : expected) {
            boolean ok = iris.contains(e[0]);
            System.out.println((ok ? "  OK    " : "  FEHLT ") + e[1] + " -> " + e[0]);
            if (!ok) failures++;
        }

        // 2) Roundtrip: expanded -> JSON-LD -> expanded
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        RDFDataMgr.write(baos, data, Lang.JSONLD);
        String jsonld = baos.toString(StandardCharsets.UTF_8);
        Model re = ModelFactory.createDefaultModel();
        RDFDataMgr.read(re, new ByteArrayInputStream(jsonld.getBytes(StandardCharsets.UTF_8)), Lang.JSONLD);
        boolean same = re.size() == data.size();
        System.out.println("Roundtrip: " + data.size() + " -> " + re.size() + " Triples" + (same ? " (gleich)" : " (ABWEICHUNG)"));
        if (!same) failures++;

        System.out.println(failures == 0 ? "ERGEBNIS: PASS" : "ERGEBNIS: FAIL (" + failures + ")");
        if (failures > 0) System.exit(1);
    }
}
