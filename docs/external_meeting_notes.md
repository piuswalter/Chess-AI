# External meeting notes

## Meeting 10.12.21

Anmerkungen:

- [x] Alle: In jedes Notebook HTML-Code für width = 100% einfügen.
- [x] Anton: MyPy Type checker implementieren um die Typen zu überprüfen (nicht rekursiv möglich).
- [ ] Alle: Jede Funktion kurz im Text beschreiben (welche Argumente bekommt sie, was ist die Idee dahinter).
- [ ] Anton: **Alles** als Funktion implementieren.
- [ ] Pius: Das initiale Board einmal ausgeben vor Spielstart (sonst sieht der menschliche Spieler nichts vor dem ersten Zug).
- [ ] Pius: Den Wechsel der Spielzustände besser anzeigen (Human vs. KI berücksichtigen!)
- [ ] Pius: Bug: Bei Remis wird aktuell noch ausgegeben, das der Spieler verloren hätte.
- [ ] Pius: Bug: Key Error mit falscher Tabelle (s. Discord). Zum Reproduzieren Seed auf 3 setzen, einmal alles ausführen und dann **nur** die Spielzelle erneut ausführen.
- [ ] Pius: Bug: Anfangsbib funktioniert nicht. Zum Reproduzieren: Player 1 als Human, Player 2 als Exercise01 KI. Dann ersten Zug e2e4 ausführen. ⇒ Spiel wechselt direkt ins Mittelspiel.
- [ ] Philipp: Zeilenumbruch bei gespeicherten Spielen hinzufügen.
- [ ] Philipp: Testfunktionen und actions (GitHub Action?) implementieren welche die KI mit vielen random seeds ausprobieren.
- [ ] Philipp: Metriken für den Vergleich entwickeln: z.B. Stockfish Engine einbauen und mit verminderter Qualität spielen lassen. Mögliche Metriken: Anzahl Züge bis Schachmatt; Spieldauer.
- [ ] Weiteres Vorgehen: MiniMax mit einfachem Materialwert implementieren → MiniMax mit simple evaluation function implementieren → Memoisierung (Speicherung bereits gesuchter/ausgewerteter Pfade) implementieren.
