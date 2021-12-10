# External meeting notes

# Meeting 10.12.21

Anmerkungen:

- In jedes Notebook HTML-Code für width = 100% einfügen.
- MyPy Type checker implementieren um die Typen zu überprüfen (nicht rekursiv möglich).
- Jede Funktion kurz im Text beschreiben (welche Argumente bekommt sie, was ist die Idee dahinter).
- **Alles** als Funktion implementieren.
- Das initiale Board einmal ausgeben vor Spielstart (sonst sieht der menschliche Spieler nichts vor dem ersten Zug).
- Den Wechsel der Spielzustände besser anzeigen (Human vs. KI berücksichtigen!)
- Bug: Bei Remis wird aktuell noch ausgegeben, das der Spieler verloren hätte.
- Bug: Key Error mit falscher Tabelle (s. Discord). Zum Reproduzieren Seed auf 3 setzen, einmal alles ausführen und dann **nur** die Spielzelle erneut ausführen.
- Testfunktionen und actions (GitHub Action?) implementieren welche die KI mit vielen random seeds ausprobieren.
- Metriken für den Vergleich entwickeln: z.B. Stockfish Engine einbauen und mit verminderter Qualität spielen lassen. Mögliche Metriken: Anzahl Züge bis Schachmatt; Spieldauer.
- Bug: Anfangsbib funktioniert nicht. Zum Reproduzieren: Player 1 als Human, Player 2 als Exercise01 KI. Dann ersten Zug e2e4 ausführen. ⇒ Spiel wechselt direkt ins Mittelspiel.
- Zeilenumbruch bei gespeicherten Spielen hinzufügen.
- Weiteres Vorgehen: MinMax mit einfachem Materialwert implementieren → MinMax mit simple evaluation function implementieren → Memoisierung (Speicherung bereits gesuchter/ausgewerteter Pfade) implementieren.
