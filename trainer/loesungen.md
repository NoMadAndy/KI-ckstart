# Spickzettel: Was bei den Experimenten rauskommt

Zum Einsammeln der Beobachtungen in Minute 35 („Was habt ihr gesehen?"). Die Zahlen gelten für `torch.manual_seed(0)` und können auf anderen Maschinen leicht abweichen – die Muster nicht.

## Notebook 01

| Experiment | Beobachtung | Der Satz für die Tafel |
|---|---|---|
| Lernrate 0.001 | Loss sinkt nur auf ~0.46, Grenze fast gerade, ~83 % | *Zu kleine Schritte: Es lernt, aber es wird nicht fertig.* |
| Lernrate 30 | Loss explodiert in die Tausender, Grenze unsinnig, Genauigkeit ~50 % (bei 100: `nan`) | *Zu große Schritte: Es schießt über das Ziel hinaus.* |
| 2 Neuronen | Zwei gerade Knicke, ~86 %, Monde bleiben halb vermischt | *Das Modell ist zu klein für die Aufgabe (Underfitting).* |
| 256 Neuronen | ~98 %, praktisch gleiche Grenze wie mit 16, nur etwas langsamer | *Mehr Gewichte helfen erst, wenn die Aufgabe schwerer ist.* |
| 30 Epochen | Grenze grob, ~85 % | *Zu früh aufgehört.* |
| 2000 Epochen | Kaum besser als 300 (~96–97 %) | *Irgendwann ist gelernt, was zu lernen ist.* |
| Overfitting-Zelle | 8 Neuronen: Training 81 %, Test 85 %. 512 Neuronen: Training 99 %, Test 75 %, Grenze zappelt um jeden Ausreißer | *Auswendig lernen ist nicht verstehen.* |

Wichtige Rückfrage an die Gruppe: **Woran erkennt man Overfitting, wenn man die Grenze nicht sehen kann?** → Trainings- und Testgenauigkeit vergleichen. Das ist die Antwort, die sie in jedem echten Projekt brauchen.

## Spiralen-Challenge

Die Ausgangskonfiguration (eine Schicht, 16 Neuronen, 500 Epochen) landet bei ~60 % – kaum besser als raten. Eine Schicht mit 64 Neuronen und 3000 Epochen kommt auf ~94 %, knapp unter dem Ziel. Ein Netz mit **zwei** versteckten Schichten schafft 100 % auf den Testdaten:

```python
torch.manual_seed(0)
model = nn.Sequential(
    nn.Linear(2, 64), nn.ReLU(),
    nn.Linear(64, 64), nn.ReLU(),
    nn.Linear(64, 1),
)
verlauf = trainiere(model, X_train, y_train, lernrate=0.05, epochen=3000, ausgabe=False)
```

Mit einer Schicht und 16 Neuronen bleibt es bei ~60 %: nicht genug Knicke. Das ist der Moment für den Satz *„Deep Learning heißt einfach: mehrere Schichten hintereinander."*

## Notebook 02 (Bonus)

- Nach 3000 Schritten (4–10 Sekunden) liegt der Loss bei ~0.2: Das Modell hat den 6-KB-Text weitgehend auswendig gelernt (Overfitting) und gibt ganze Sätze wörtlich wieder, neu zusammengemischt an den Nahtstellen. Genau das ansprechen – es ist der Text-Zwilling der Overfitting-Zelle aus Notebook 01.
- Temperatur 0.2 → wiederholt sich („Der Server brummt. Der Server brummt.") – das ist der Modus, in dem Sprachmodelle *langweilig, aber sicher* sind.
- Temperatur 1.5 → Buchstabensalat – *kreativ bis wirr*.
- `zeige_kandidaten("Die ")` → mehrere Kandidaten (A, K, J, T …), `zeige_kandidaten("Der Kaff")` → `e` mit ~100 %. Das ist die Folie „Autovervollständigung auf Steroiden" in echt – manchmal unsicher, manchmal felsenfest.

## Typische Fragen und kurze Antworten

- **„Warum ReLU?"** – Ohne die Knick-Funktion wäre das ganze Netz nur eine gerade Linie, egal wie viele Schichten. Die Knicke machen krumme Grenzen möglich.
- **„Warum Momentum / Adam?"** – Beschleunigung fürs Bergabrollen: Der Schritt merkt sich die Richtung der letzten Schritte. Prinzip bleibt Gradient Descent.
- **„Wie wählt man die Lernrate in echt?"** – Ausprobieren, genau wie heute. Plus Tricks wie sinkende Lernrate im Laufe des Trainings.
- **„Kann man das auf der GPU laufen lassen?"** – Ja, mit `model.to("cuda")` und den Daten ebenso. Für 400 Punkte lohnt es nicht, für Milliarden Gewichte ist es zwingend.
- **„Ist ChatGPT wirklich nur das?"** – Der Kern ja. Dazu kommen Transformer-Architektur, riesige Datenmengen und Feinschliff mit menschlichem Feedback. Aber die Schleife ist dieselbe.
