# KI-ckstart – Gesamtpaket (13.09.2026)

```
Konzept_KI-ckstart_v2.md                  Konzept für JAV-Workshop, VHS-Kurs und Buch
Folien_KI-ckstart_v2.pptx / .pdf          22 Folien: 17 im JAV-Ablauf + R1–R5 Reserve/VHS, Sprechernotizen mit Minutenangaben
Praxisbeispiele_und_Uebungen.md           alle Übungen: Rätsel, Halluzinations-Bogen, 14 Handy-Übungen, 6 Papierübungen, Demo, Zeitbudgets, Anhänge
handy/index.html                          Handy-Seite (GitHub Pages): 11 Übungskarten, Eliza-Miniatur, optionaler Turing-Test
vorlagen/Papier-Vorlagen_KI-ckstart.pdf   8 Seiten Papierübungen zum Drucken
qr_handy.png                              QR-Code auf die Handy-Seite (ist bereits auf Folie 13 und 17)
```

## Was gegenüber der Fassung vom 08.09. neu ist

- **Folie 13** (neu): „Jetzt ihr: zwei Fragen an die KI“ – QR-Code, Zufallszahl, Buch. Danach die Auflösung.
- **Folie 17**: zweiter QR-Code auf die Handy-Seite.
- **Reservefolien R1–R5**: Sätze vervollständigen, Eliza, Turing-Test, Münchhausen, Training von Hand. Im JAV-Ablauf nicht eingeplant, für den VHS-Kurs Kernfolien.
- **Sprechernotizen** auf Folie 1, 2, 3, 4, 6, 8, 9, 12, 13, 15, 16, 17 überarbeitet (Buch-Satz, Rätsel, CAPTCHA, Eliza, Zählen lassen, Papier-Training, Kuh-Trick, Münchhausen, Auflösung, Weizenbaum).
- Alle anderen Folien und das Repo (Notebooks, Devcontainer, Hermes-Auftrag, Lösungen) sind unverändert.

## Handy-Seite veröffentlichen

1. Ordner `handy/` in die Wurzel des Repos `NoMadAndy/KI-ckstart` kopieren, committen, pushen.
2. Settings → Pages → „Deploy from a branch“, Branch `main`, Ordner `/ (root)`.
3. Nach ein bis zwei Minuten: `https://nomadandy.github.io/KI-ckstart/handy/`. Nur dann stimmt der QR-Code. Bei anderem Pfad `qr_handy.png` neu erzeugen (`python3 trainer/make_qr.py <URL> qr_handy.png`) und auf Folie 13 und 17 tauschen.

Keine Abhängigkeiten, keine Cookies, keine Datenübertragung. Eliza läuft im Browser.

## Vor dem Termin testen (am eigenen Handy, im Raum)

- QR-Code scannen → Seite lädt.
- „Kopieren“ auf Übung 1 → in Copilot einfügen → Antwort.
- „Copilot öffnen“ → Copilot geht auf, Toast „Prompt kopiert“ → im Feld einfügen, absenden. (Copilot hat die Prompt-Übergabe per Link 2025 abgeschaltet; sollte der Prompt doch schon im Feld stehen, umso besser.)
- „In ChatGPT öffnen“ → ChatGPT geht mit dem Prompt im Feld auf. Wenn nicht: Kopieren und einfügen.
- Übung 2 (Buch) einmal in beiden Plattformen laufen lassen – beide Ausgänge kennen.
- Eliza: „Ich bin müde“, dann etwas ohne Schlüsselwort.

## Turing-Test freischalten (VHS Abend 4)

In `handy/index.html` das Array `PAIRS` füllen (Frage, echte Antwort eines Menschen mit Einverständnis, Antwort eines Modells). Solange es leer ist, bleibt der Abschnitt unsichtbar.

## Drucken

- JAV: Seiten 1–3 (Teilnehmer ÷ 3 + 2, reihum Rot/Blau/Grün), Seite 4 (eine pro zwei Gruppen). Karten ausschneiden, mittig falten, bedruckte Seite außen.
- VHS: siehe Anhang B der Praxisbeispiele.
