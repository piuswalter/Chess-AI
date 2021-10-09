# Chess-AI

## Entwicklung einer KI für das Schach-Spiel

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

## .vscode settings.json file

```json
{
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "biber",
            "command": "biber",
            "args": [
                "-outdir=%OUTDIR%",
                "%DOCFILE%"
            ]
        },
        {
            "name": "lualatexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-lualatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "latexmk_rconly",
            "command": "latexmk",
            "args": [
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "rnw2tex",
            "command": "Rscript",
            "args": [
                "-e",
                "knitr::opts_knit$set(concordance = TRUE); knitr::knit('%DOCFILE_EXT%')"
            ],
            "env": {}
        },
        {
            "name": "jnw2tex",
            "command": "julia",
            "args": [
                "-e",
                "using Weave; weave(\"%DOC_EXT%\", doctype=\"tex\")"
            ],
            "env": {}
        },
        {
            "name": "jnw2texmintex",
            "command": "julia",
            "args": [
                "-e",
                "using Weave; weave(\"%DOC_EXT%\", doctype=\"texminted\")"
            ],
            "env": {}
        },
        {
            "name": "tectonic",
            "command": "tectonic",
            "args": [
                "--synctex",
                "--keep-logs",
                "%DOC%.tex"
            ],
            "env": {}
        },
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-output-directory=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk 🔃",
            "tools": [
                "latexmk"
            ]
        },
        {
            "name": "bibtex",
            "tools": [
                "bibtex"
            ]
        },
        {
            "name": "latexmk -> biber -> latexmk*2",
            "tools": [
                "latexmk",
                "biber",
                "latexmk",
                "latexmk"
            ]
        },
        {
            "name": "xelatex -> biber -> xelatex*2",
            "tools": [
                "xelatex",
                "biber",
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "latexmk (latexmkrc)",
            "tools": [
                "latexmk_rconly"
            ]
        },
        {
            "name": "latexmk (lualatex)",
            "tools": [
                "lualatexmk"
            ]
        },
        {
            "name": "pdflatex ➞ bibtex ➞ pdflatex × 2",
            "tools": [
                "pdflatex",
                "bibtex",
                "pdflatex",
                "pdflatex"
            ]
        },
        {
            "name": "Compile Rnw files",
            "tools": [
                "rnw2tex",
                "latexmk"
            ]
        },
        {
            "name": "Compile Jnw files",
            "tools": [
                "jnw2tex",
                "latexmk"
            ]
        },
        {
            "name": "tectonic",
            "tools": [
                "tectonic"
            ]
        }
    ],
    "ltex.latex.environments": {
        "lstlisting": "ignore",
        "verbatim": "ignore",
        "minted": "ignore",
        "code": "ignore"
    },
    "latex-workshop.latex.outDir": "%DIR%/Build"
}
```
