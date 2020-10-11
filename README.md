[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wwi20ama-programmierung/python-intro/main?urlpath=lab)

# Programmier-Grundlagen

Dieses Repository enthält Informationen bzw. Erklärungen zu grundlegenden Programmier-Konzepten in [Python](https://www.python.org).

Diese Einführung wird größtenteils in Form von [Jupyter-Notebooks](https://jupyter.org) zur Verfügung gestellt.
Ein Jupyter-Notebook ist eine interaktive Programmier-Umgebung, in der Code geschrieben und direkt ausgeführt werden kann.
Die Programmiersprache Python enthält eine ähnliche Umgebung, das sog.
*[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)* ("**R**ead-**E**valuate-**P**rint-**L**oop").
Jupyter-Notebooks sind allerdings komfortabler zu benutzen und erlauben es, auch noch Erklärungstexte in Form von [Markdown](https://de.wikipedia.org/wiki/Markdown)-Zellen hinzuzufügen.

Einige Beispiele und Aufgaben werden auch in Form von Python-Quelldateien zur Verfügung gestellt.
Dies sind Textdateien mit der Endung `.py`.
Um Python-Quelldateien auf dem eigenen Computer auszuführen wird eine Python-Installation
benötigt.
Alternativ kann auch ein Online-Editor wie z.B. [Repl.It](https://repl.it) verwendet werden,
oder die Dateien werden mittels des in Jupyter/Anaconda ([s.u.](#Nutzungshinweise)) enthaltenen Python ausgeführt.


## Nutzungshinweise

- **Online-Dienst Binder:**
  Die hier verwendeten Notebooks können mittels des Online-Services
  [Binder](https://mybinder.org/v2/gh/wwi20ama-programmierung/python-intro/main?urlpath=lab)
  verwendet werden.
  Dies ist eine webbasierte Jupyter-Umgebung, die gut zum Lesen und für schnelles Experimentieren
  geeignet ist.
  
  Wenn Sie dem
  [Binder-Link](https://mybinder.org/v2/gh/wwi20ama-programmierung/python-intro/main?urlpath=lab)
  oder dem Badge ganz oben in dieser Beschreibung
  ([![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wwi20ama-programmierung/python-intro/main?urlpath=lab))
  folgen, gelangen Sie in eine Jupyter-Umgebung, die exklusiv für Sie erzeugt wurde.
  D.h. Sie können dort Änderungen vornehmen, ohne dass das andere Nutzer betrifft
  bzw. für andere sichtbar ist.
  Der Nachteil dabei ist allerdings, dass Ihre Änderungen nur bedingt gespeichert werden.
  Man kann Änderungen an Notebooks im eigenen Browser-Speicher ablegen oder Notebooks herunterladen,
  die Umgebung ist aber nicht persistent in dem Sinne, dass Änderungen ohne weiteres Zutun
  beim nächsten Start wieder verfügbar sind.

- **Online-Editor Repl.It:**
  Unter https://repl.it findet sich ein kollaborativer Online-Editor, in dem man Python-Dateien
  (auch zu mehreren) im Browser bearbeiten und ausführen kann.
  Ein [Python-REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
  gibt es dort auch, Jupyter-Notebooks sind allerdings nur sehr umständlich verwendbar.
  Wir werden Repl.It in den Vorlesungen für die meisten Beispiele und Übungen verwenden.
  
- **Jupyter lokal installieren:**
  Jupyter kann auf dem eigenen Rechner als [Python](https://www.python.org)-Paket oder als Teil
  der Data-Science-Plattform [Anaconda](https://www.anaconda.com) installiert werden.
  Python ist auch Teil von Anaconda, d.h. wer letzteres installiert, benötigt nicht
  mehr unbedingt noch eine separate Python-Installation.
  Genauere Infos gibt es auf der offiziellen Website des Projekts: https://jupyter.org.

- **Python lokal installieren:**
  Python kann über die offizielle Python-Website heruntergeladen und installiert werden:
  https://www.python.org.
  Alternativ ist es Teil von [Anaconda](https://www.anaconda.com).
  Sobald ein Python installiert ist, können Python-Dateien (`*.py`) unter Windows einfach
  per Doppelklick augeführt werden.
  Praktischer ist es allerdings für die Übungen, Python auf einer Konsole auszuführen,
  weil sich dann das Fenster nicht sofort nach dem Ende des Programms schließt.

- **Benutzung von Python auf der Konsole:**
  Unter Windows startet man die Konsole mittels Rechtsklick im Explorer, dort ist es der
  Punkt "Eingabeaufforderung" oder "Powershell".
  Nach diesen Stichworten kann man auch im Startmenü suchen.
  Unter Linux oder MacOS sollte man ein "Terminal" starten.
  In Jupyter-Umgebungen kann man ebenfalls ein Terminal starten.
  Ggf. muss man sich noch mit Shell-Befehlen in das richtige Verzeichnis vorarbeiten.
  
  Die wichtigsten Kommanozeilen-Befehle für unsere Zwecke im Überblick:
  - `dir`: Inhalt des aktuellen Verzeichnisses auflisten (unter Windows).
  - `ls`: Inhalt des aktuellen Verzeichnisses auflisten (unter Linux/MacOS).
  - `cd <NAME>`: Ins Unterverzeichnis `<NAME>` wechseln.
  - `cd ..`: Aus dem aktuellen Unterverzeichnis wieder eine Ebene nach oben wechseln.
  - `python <DATEINAME>`: Die Python-Datei `<DATEINAME>` ausführen.