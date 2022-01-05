# Anforderungen aus dem ersten Meeting

1. Einarbeitung in Python-Chess
    - Eröffnungsbibliothek
    - Endspiel-Bibliothek: Syzygy
    - Version 0: zufällige Züge auswählen im Mittelspiel

2. Minimax-Algorithmus
    1. Evaluierungs-Funktion **inkrementell** implementieren.
    2. Memoisierung

3. Alpha-Beta-Pruning mit iterative Deepening
    - wichtig: Memoisierung beibehalten
    - iterative Deepening: Russell & Norvig

4. Ruhesuche: Eine Stellung ist ruhig falls:
    1. keine Figur geschlagen werden kann
    2. kein Bauer umgewandelt werden kann
    3. der König nicht im Schach steht

**WICHTIG**: Alles soll als Jupyter-Notebook implementiert werden.
Jede Funktion muss ausführlich dokumentiert werden (mittles Markdown + LaTeX),  d.h.

1. Welche Argumente erhält die Funktion
2. Welches Ergebnis wird berechnet
3. Welche Seiteneffekte treten auf (falls Seiteneffekte auftreten)
4. Bei komplizierter Logik soll auch Algorithmus beschrieben werden.

Schriftliche Abgabe als PDF erzeugt auf Jupyter-Notebook

Abgabe-Datum vor Beginn Ihrer Bachelorarbeit

GitHub-Repo anlegen

Testen:
Abspeichern einer Partie als Datei auf Festplatte in algebraischer Notation
Verschiedene Versionen Ihrer KIs sollen gegeneinander antreten können
Nur Bibliotheken verwenden, die unter Windows lauffähig sind

Bei Verwendung von Random immer Seed setzen.

Zielorientiertes Arbeiten:
Entwicklung einer Schach-KI mit etwa ELO 1500
