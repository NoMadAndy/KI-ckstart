# KI-ckstart – Wie lernt eine Maschine?

KI zum Anfassen: in 60 Minuten vom Neuron zum Agenten. Material zum Workshop bei der JAV-Versammlung am 16.09.2026.

[![In GitHub Codespaces öffnen](https://github.com/codespaces/badge.svg)](https://codespaces.new/NoMadAndy/KI-ckstart?quickstart=1)

## Das brauchst du

- Einen **kostenlosen GitHub-Account** (private Adresse reicht – bitte **vor** dem Workshop anlegen und einmal einloggen, die E-Mail-Bestätigung dauert sonst wertvolle Minuten).
- Einen Browser. Sonst nichts – Python, PyTorch und alles Weitere laufen in der Cloud.

Der KI-ckstart-Codespace verbraucht etwa 2 von 120 kostenlosen Core-Stunden, die jeder GitHub-Account monatlich hat. Es entstehen keine Kosten.

## So startest du (dauert 2–3 Minuten – bitte gleich zu Beginn machen)

1. Auf den Button **„Open in GitHub Codespaces"** oben klicken (oder QR-Code auf der Folie scannen).
2. Bei GitHub einloggen, dann **„Create new codespace"** bestätigen. Die Voreinstellung (2 Kerne) ist richtig.
3. Warten, bis VS Code im Browser erscheint und unten rechts keine Setup-Meldung mehr läuft.
4. Links im Explorer `01_wie_lernt_eine_maschine.ipynb` öffnen – es sollte schon offen sein.
5. Die erste Zelle mit **Shift + Enter** ausführen. Falls gefragt wird, welcher Kernel: **„Python 3 (Workshop)"** bzw. `/usr/local/bin/python` wählen.

Wenn `PyTorch … läuft. Los geht's.` erscheint, bist du startklar.

## Die Notebooks

| Datei | Was drin ist | Dauer |
|---|---|---|
| `01_wie_lernt_eine_maschine.ipynb` | Ein neuronales Netz bauen, trainieren, beim Lernen zuschauen, an drei Drehknöpfen drehen, Overfitting erleben | 20 min |
| `02_bonus_mini_sprachmodell.ipynb` | Dasselbe Prinzip auf Text: ein winziges Sprachmodell, das Deutsch zu schreiben versucht | 10 min, für Schnelle oder für zu Hause |

`workshop_utils.py` enthält nur Plot-Hilfen und Datensätze – reinschauen erlaubt und erwünscht.

## Wenn etwas klemmt

- **Zelle hängt / Fehler „Kernel not found":** oben rechts *Select Kernel* → „Python 3 (Workshop)". Notfalls *Restart* und wieder von oben ausführen.
- **`ModuleNotFoundError: torch`:** Das Setup ist noch nicht durch. Unten rechts auf die Meldung klicken und warten, oder im Terminal `bash .devcontainer/setup.sh` ausführen.
- **Codespace startet nicht:** Browser-Tab schließen, auf https://github.com/codespaces gehen und den bestehenden Codespace dort öffnen.
- **Copilot fragen ist erlaubt.** Wenn du wissen willst, was eine Zeile tut: markieren, in Copilot einfügen, fragen. Prüfen, ob die Antwort zum Verhalten passt – das ist Teil der Übung.

## Danach

Der Codespace läuft nach 30 Minuten Inaktivität von allein aus und wird nach 30 Tagen gelöscht. Wer sein Kontingent sauber halten will: auf https://github.com/codespaces → *Delete*.

Das Material darf gern zu Hause weiterverwendet werden. Ideen zum Weitermachen stehen am Ende von Notebook 02.
