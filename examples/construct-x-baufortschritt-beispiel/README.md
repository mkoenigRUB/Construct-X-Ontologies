# Construct-X Baufortschritt – verständliches Beispiel

Das Beispiel zeigt eine durchgängige Kette von der Lieferung eines Packstücks bis zum Einbau der darin enthaltenen Produkte in ein BIM-Konstruktionselement.

Ablauf:
1. PACK-001 wird in Anlieferzone A angenommen.
2. PACK-001 wird in das 4. Obergeschoss transportiert.
3. GK-001, GK-002 und MP-001 werden in WALL-4711 eingebaut.
4. WALL-4711 ist über eine IFC-GlobalId und den Raum 4.12 lokalisierbar.

Die Notifications sind bewusst schlank. Sie melden nur das Ereignis und verweisen mit `dataResourceId` und `dataRevision` auf den jeweiligen Datenstand.

Die Header-Struktur orientiert sich am Tractus-X Industry Core Notification Pattern. Der `content` ist Construct-X-spezifisch.
