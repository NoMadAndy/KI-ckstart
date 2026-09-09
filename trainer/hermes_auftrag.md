# Hermes-Live-Demo: Auftrag, Feature-Optionen, Regie

## Idee

Hermes baut vor den Augen der Teilnehmer eine **Live-Umfrage-App**, die die Teilnehmer sofort selbst mit dem Handy benutzen. Damit ist die Demo nicht nur Zuschauen: Das Publikum stimmt in der App ab, die der Agent gerade gebaut hat – und das Ergebnis der Umfrage („Wie oft nutzt ihr KI in der Ausbildung?") ist gleichzeitig der Einstieg in den JAV-Teil.

Die Basis-App ist fix. Das Publikum wählt **ein** Extra-Feature aus drei Optionen, die vorher alle einzeln getestet wurden.

## Vorbereitung (einmalig, vor dem 16.09.)

1. Reverse Proxy vorab einrichten: `umfrage.<deine-domain>` → `sbs02:8090` in NPM anlegen (inkl. Zertifikat). Dann ist die App in dem Moment erreichbar, in dem der Container hochkommt – und der Agent muss live nichts am Proxy anfassen.
2. Zielverzeichnis festlegen und leer anlegen, z. B. `~/apps/jav-umfrage`. Hermes bekommt dieses Verzeichnis und darf nur dort schreiben.
3. Den Auftrag unten mit jeder der drei Optionen einmal trocken laufen lassen. Zeit stoppen. Erwartung: 5–10 Minuten mit laguna-s-2.1 über OpenRouter.
4. Die beste fertige Version als Fallback sichern (`~/apps/jav-umfrage-fallback`), inkl. `docker compose up -d` getestet.
5. Einen Trockenlauf als Screencast aufnehmen (OBS oder `asciinema`) – falls am Tag Netz, Proxy oder Modell zicken.

## Der Auftrag (so 1:1 an Hermes geben)

```
Baue eine kleine Web-App "JAV-Live-Umfrage" und bringe sie auf diesem Server zum Laufen.

Rahmen:
- Arbeitsverzeichnis: ~/apps/jav-umfrage – lege alle Dateien nur dort an.
- Stack: Python 3.12, FastAPI + Uvicorn, eine einzige app.py, statische index.html
  (Vanilla JS, Chart.js vom CDN). Daten in einer SQLite-Datei im Verzeichnis ./data.
- Deployment: Dockerfile + docker-compose.yml, Container-Name jav-umfrage,
  Port 8090 auf dem Host, restart: unless-stopped, Healthcheck auf /health.
- Keine Änderungen außerhalb des Arbeitsverzeichnisses, kein sudo, kein Zugriff
  auf andere Container.

Funktion:
- Startseite zeigt die Frage "Wie oft nutzt du KI-Tools in deiner Ausbildung?"
  mit vier großen Buttons: "Täglich", "Mehrmals pro Woche", "Selten", "Nie".
  Die Seite muss auf dem Handy gut bedienbar sein (große Buttons, kein Zoomen nötig).
- Ein Klick sendet die Stimme per POST an /vote. Pro Browser nur eine Stimme
  (Cookie oder localStorage-Token), danach sieht man direkt das Ergebnis.
- /ergebnis zeigt ein Balkendiagramm (Chart.js) mit Stimmen pro Antwort und die
  Gesamtzahl. Diese Seite wird auf dem Beamer stehen.
- GET /health liefert {"status": "ok"}.
- POST /admin/reset mit Header X-Token: <RESET_TOKEN> setzt alle Stimmen zurück.
  RESET_TOKEN kommt aus einer .env-Datei; lege sie mit einem zufälligen Wert an.

Extra-Feature (genau eines, siehe unten): {{FEATURE}}

Vorgehen:
- Erst kurz planen, dann bauen, dann `docker compose up -d --build`.
- Prüfe mit curl, dass /health, / und /ergebnis antworten, und gib eine Test-Stimme
  ab, um den kompletten Ablauf zu verifizieren. Setze danach zurück.
- Zum Schluss: Aufruf-URL, Reset-Befehl und in drei Sätzen, was du gebaut hast.
```

### Die drei Feature-Optionen (Publikum wählt per Handzeichen)

**A – „Live"**
```
Live-Aktualisierung: /ergebnis aktualisiert sich ohne Neuladen über Server-Sent
Events (GET /events). Jede neue Stimme erscheint innerhalb einer Sekunde auf allen
geöffneten Ergebnis-Seiten.
```

**B – „Wortwolke"**
```
Nach der Abstimmung wird eine zweite Frage gestellt: "Ein Wort, das du mit KI
verbindest" (Freitext, max. 30 Zeichen). /ergebnis zeigt zusätzlich eine Wortwolke
aller Antworten (Schriftgröße nach Häufigkeit; wordcloud2.js vom CDN oder eigene
einfache Skalierung). Unanständige Wörter musst du nicht filtern, aber HTML muss
escaped werden.
```

**C – „Konfetti"**
```
Dark-Mode-Umschalter (Icon oben rechts, Einstellung merken) und eine
Konfetti-Animation über den ganzen Bildschirm, sobald jemand abgestimmt hat
(canvas-confetti vom CDN). Die Buttons bekommen beim Antippen eine kleine
Animation.
```

## Regie während der Demo (Minute 35–50)

| Minute | Was passiert | Was du sagst |
|---|---|---|
| 35 | Feature-Abstimmung per Handzeichen, `{{FEATURE}}` einsetzen, Auftrag absenden | „Das ist derselbe Typ Modell wie euer 65-Gewichte-Netz – nur mit Werkzeugen und einer Schleife drumherum." |
| 35–43 | Hermes plant und arbeitet. Terminal auf Beamer, Schrift groß | Live kommentieren, was er tut: Plan, Datei schreiben, Befehl ausführen, Ergebnis lesen, nächster Schritt. Das *ist* die Agenten-Erklärung – besser als jede Folie. |
| ~43 | Container läuft, URL steht | QR-Code der Umfrage-URL zeigen (vorher erzeugt, da Domain feststeht). Alle stimmen ab. |
| 45 | /ergebnis auf dem Beamer | Ergebnis kommentieren – direkte Überleitung zum JAV-Teil: „So viele von euch nutzen das täglich. Und was heißt das für Ausbildung und Mitbestimmung?" |
| 48 | Ein Blick in den erzeugten Code | „Würdet ihr das so übernehmen? Was fehlt?" (Tests, Validierung, Rate-Limit …) – Botschaft: Der Agent liefert einen Entwurf, die Verantwortung bleibt beim Menschen. |

## Wenn es schiefgeht

- **Hermes hängt oder das Modell antwortet nicht:** Screencast starten, parallel Fallback-App hochfahren (`cd ~/apps/jav-umfrage-fallback && docker compose up -d`). Die Umfrage findet trotzdem statt.
- **Homelab nicht erreichbar (Firmennetz):** Handy-Hotspot für den Präsentationslaptop. Die Teilnehmer-Handys erreichen die öffentliche URL ohnehin über Mobilfunk.
- **Nur die Umfrage-URL nicht erreichbar:** Ergebnis-Seite per Beamer, Abstimmung per Handzeichen. Die Demo hat ihren Zweck trotzdem erfüllt.

## Hygiene

- Nichts Firmeninternes in den Auftrag – die Demo läuft komplett mit fiktiven Inhalten.
- Nach der Veranstaltung: Container stoppen, Proxy-Host deaktivieren, Umfragedaten löschen (`data/`), OpenRouter-Kosten kurz prüfen.
