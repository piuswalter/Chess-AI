# Chess-AI

## Schnellstart

1. Download der Endspiel-Tabellen mithilfe der Links aus [`README.md`](lib/ending/3-4-5/README.md).
2. Extrahieren der Dateien nach `lib/ending/3-4-5/` (z.B. `lib/ending/3-4-5/KBBBvK.rtbz`).
3. Validieren der heruntergeladenen Dateien mithilfe der Prüfsummen.
4. Anlegen eines `virtual environments` mit `conda create -n chess python=3.10.4 -c conda-forge`.
5. Installation von `jupyter notebook` in diesem `environment` mit `conda install jupyter -c conda-forge`.
6. Installation der benötigten Pakete mit `pip install -r src/requirements.txt`.
7. Ausführen des [`src\Main.ipynb`](src/Main.ipynb) Notebooks.

### Optional

Optional kann auch die Stockfish-Engine als Spielgegner angesteuert werden. Die Anleitung zur Installation ist [hier](lib/stockfish/README.md) zu finden.

## Ordnerstruktur

| Name | Beschreibung |
|---|---|
| `docs` | Interne Meeting-Notizen |
| `games` | Ordner für die Speicherung gespielter Partien im `.pgn`-Format |
| `lib` | Die verwendeten Bibliotheken bzw. Engines und Tabellen im Eröffnungs- und Endspiel (müssen vor der Ausführung separat heruntergeladen werden, siehe entsprechende `README.md`) |
| `scripts` | Eine Sammlung von Scripts für die Automatisierung. |
| `src` | Der gesamte Quellcode des Projekts. Hauptdatei und **Einstiegspunkt** ist die Datei `Main.ipynb`. |

## Aufgabenstellung

### Entwicklung einer KI für das Schach-Spiel

Das Schach-Spiel ist in der westlichen Welt das am weitesten verbreitete Brett-Spiel. Ziel der Studienarbeit ist die Entwicklung einer KI für das Schach-Spiel. Bei dieser Studienarbeit geht es darum, die auf der Seite

[https://www.chessprogramming.org/Simplified_Evaluation_Function](https://www.chessprogramming.org/Simplified_Evaluation_Function)

dargestellte Evaluierungsfunktion zusammen mit Alpha-Beta-Suche und Transpositions-Tabellen zu implementieren. Diese beiden Themen werden in meinem Skript über "Introduction to Artificial Intelligence" diskutiert. Um eine akzeptable Performanz der KI zu erreichen, ist es wichtig, dass bei der Suche auch eine sogenannte Ruhesuche (Englisch: Quiescence Search)

[https://www.chessprogramming.org/Quiescence_Search](https://www.chessprogramming.org/Quiescence_Search)

durchgeführt wird.

Die KI soll mit Hilfe der Bibliothek

[https://pypi.org/project/python-chess/](https://pypi.org/project/python-chess/)

entwickelt werden. Diese Bibliothek soll auch als GUI verwendet werden. Das Programm soll als Jupyter Notebook entwickelt werden.

Dieses Thema kann von 2 oder 3 Studierenden bearbeitet werden.

Erforderliche Vorkenntnisse: Gute Kenntnisse in Python und Jupyter Notebook.

## Hilfreiche Links

- [Simplified Evaluation Function](https://www.chessprogramming.org/Simplified_Evaluation_Function)
- [An Introduction to Artificial Intelligence](https://github.com/karlstroetmann/Artificial-Intelligence/raw/master/Lecture-Notes/artificial-intelligence.pdf)
- [Quiescence Search](https://www.chessprogramming.org/Quiescence_Search)
