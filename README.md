# Expand selections in Sublime Text

These are two commands to help you work with Sublime Text. The first command is *select_left* and the second is *select_right*.

In Sublime Text, there are views, windows, cursors and selected regions. Each window has many views. In a view there may be several cursors. Every cursor has a selected region. Now we want to expand each selected region up until some text either before or after that region in the view.

When you run one of the two commands, it asks for a string. Then every single selected region in the current view will be expanded to the left or right respectively until the specified string. Now, your selected regions are bigger!

# Add a custom command to the command palette

Create a file at
```sh
subl ~/.config/sublime-text-3/Packages/User/Default.sublime-commands
```
with the content

```json
[
  { "caption": "Move selectors to the left", "command": "select_left"},
  { "caption": "Move selectors to the right", "command": "select_right"}
]
```

# Add a key combination for a custom command

Create a file at
```sh
subl "~/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap"
```

with the content
```json
[
  { "keys": ["ctrl+shift+;"], "command": "select_left" },
  { "keys": ["ctrl+shift+'"], "command": "select_right" },
]
```

# Done
* Get the cursor position
* Select everything from the cursor up to some character
* Check if a character is equal to a given character
* Iterate until a given character in the text buffer
* Add the select_left command to the command palette
* Add the select_right command to the command palette
* Bind the select_left command to a combination of keys
* Bind the select_right command to a combination of keys
* Pop up some dialog to receive an input
* Select until a sequence of characters
* Select backwards until a character
* Remove the shortcut shift ctrl l as it breaks a functionality if several lines are selected
* Check if the shortcut shift ctrl ; breaks an existing funtionality
* If selected to the left, put the cursor to the left of the selected region, so that one can manually modify the selection there

# To do
* Go to the first character that is not a space
* Check if a character matches a regexp
* Sublime market https://packagecontrol.io/ uploadable?
* Check out the application command "expand_selection"
* Check out the pre-made plugin Packages/Default/goto_line.py in the **Default** package


# Beispiel 1. Ersetze die Bindestriche mit Leerzeichen in jeder Zeile zwischen < und >
1. <Modul-FlexRay-Protokoll>%#Modul-FlexRay-Protokoll%
1. <Modul-VHDL>%#Modul-VHDL%
1. <Modul-FPGA-Simulation-1>%#Modul-FPGA-Simulation-1%
1. <Modul-FPGA-Simulation-2>%#Modul-FPGA-Simulation-2%
1. <Modul-LTSpice>%#Modul-LTSpice%
1. <Modul-C++-Basics>%#Modul-C++-Basics%
1. <Modul-C++-Advanced>%#Modul-C++-Advanced%
1. <Modul-C++-Expert>%#Modul-C++-Expert%
1. <Modul-Command-Line-Suchen>%#Modul-Command-Line-Suchen%
1. <Modul-Command-Line-Simple>%#Modul-Command-Line-Simple%
1. <Modul-Git-I>%#Modul-Git-I%
1. <Modul-Git-II>%#Modul-Git-II%
1. <Modul-ARM-Assembly>%#Modul-ARM-Assembly%
1. <Modul-x86-Assembly>%#Modul-x86-Assembly%
1. <Modul-C++-Cross-Build>%#Modul-C++-Cross-Build%
1. <Modul-QEMU>%#Modul-QEMU%
1. <Modul-Sensor-and-Actuator-AUTOSAR-Pattern>%#Modul-Sensor-and-Actuator-AUTOSAR-Pattern%

# Beispiel 2. Unterteile den folgenden Text in Bereiche, die von # eingeschlossen sind, und wähle diejenigen Bereiche aus, wo "Level 2" vorkommt

# Übersicht

1. [Modul FlexRay Protokoll](#Modul-FlexRay-Protokoll)
1. [Modul CAN Protokoll](#Modul-CAN-Protokoll)
1. [Modul FlexCAN Protokoll](#Modul-FlexCAN-Protokoll)
1. [Modul TTCAN Protokoll](#Modul-TTCAN-Protokoll)
1. [Modul VHDL](#Modul-VHDL)
1. [Modul FPGA Simulation 1](#Modul-FPGA-Simulation-1)
1. [Modul FPGA Simulation 2](#Modul-FPGA-Simulation-2)
1. [Modul LTSpice](#https://de.wikipedia.org/wiki/LTspice)
1. [Modul C++ Level 0](#Modul-C++-Level-0)
1. [Modul C++ Level 1](#Modul-C++-Level-1)
1. [Modul C++ Level 2](#Modul-C++-Level-2)

  // Replace p
1. [Modul Command Line Suchen](#Modul-Command-Line-Suchen)
1. [Modul Command Line Simple](#Modul-Command-Line-Simple)
1. [Modul Git I](#Modul-Git-I)
1. [Modul Git II](#Modul-Git-II)
1. [Modul ARM Assembly](#Modul-ARM-Assembly)
1. [Modul x86 Assembly](#Modul-x86-Assembly)
1. [Modul C++ Cross Build](#Modul-C++-Cross-Build)
1. Modul QEMU
1. Modul Sensor and Actuator AUTOSAR Pattern
1. [Modul AUTOSAR Blockset](#Modul-AUTOSAR-Blockset)
1. [Modul Vehicle Network Toolbox](#Modul-Vehicle-Network-Toolbox)
1. [Modul 64 bit Mikroprozessor Programmierung](#Modul-64-bit-Mikroprozessor-Programmierung)
1. [Modul 32 bit Mikroprozessor Programmierung](#Modul-32-bit-Mikroprozessor-Programmierung)
1. [Modul Microcontroller Basics](#Modul-Microcontroller-Basics)
1. [Modul Protokoll Basics](#Modul-Protokoll-Basics)
1. [Modul C++ If Abfragen](#Modul-C++-If-Abfragen)
1. [Modul C++ Schleifen](#Modul-C++-Schleifen)
1. [Modul C++ Signal Handling](#Modul-C++-Signal-Handling)
1. Modul Micro Python pyboard
1. [Modul Basics about FPGAs](#Modul-Basics-about-FPGAs)
1. [Modul Basics about Ethernet](#Modul-Basics-about-Ethernet)
1. [Modul LIN Protokoll](#Modul-LIN-Protokoll)
1. [Modul OSEK](#Modul-OSEK)
1. [Modul 8 bit PICmicro](#Modul-8-bit-PICmicro)
1. [Modul 16 bit PICmicro](#Modul-16-bit-PICmicro)
1. [Modul Basics über Netzwerkbusse](#Modul-Basics-über-Netzwerkbusse)


Der Aufwand für jedes Modul ist etwa 3 Stunden.

# Modul FlexRay Protokoll

## Niveau

* Level 0

## Voraussetzungen

* Schon mal ein Auto gesehen und drinnen gesessen
* hat eine Muttersprache

## Lernziele

* Kommunikationsprotokolle
* FlexRay Protokoll

## Inhalt

* Was sind Kommunikationsprotokolle?
* Wie funktioniert genau das FlexRay Kommunikationsprotokoll: ![](flexray-frame.png)
* Welche Programmiersprachen haben eine Schnittstelle zum FlexRay Protokoll?
* Auf welchen Kabeln und physischen Netzwerken werden FlexRay Pakete übertragen?

## Prüfung

* Multiple Choice Fragen

# Modul CAN Protokoll

## Niveau

* Level 0

## Voraussetzungen

* Modul Microcontrollers Basics

## Lernziele

* Wie werden die Sensorinformationen im Auto verarbeitet?
* Wie wird einem Aktuator wie dem Scheibenwischer ein Befehl geschickt? In welcher Sprache wird der Befehl geschickt?

## Inhalt

* CAN Protokoll
* Wie sehen die CAN Frames aus?
* Aus welchen Schichten besteht das CAN Protokoll?
* Wie funktioniert genau das CAN Kommunikationsprotokoll
* Welche Programmiersprachen haben eine Schnittstelle zum CAN Protokoll?
* Auf welchen Kabeln und physischen Netzwerken werden CAN Pakete übertragen?

## Prüfung

* Multiple Choice Fragen

# Modul FlexCAN Protokoll

## Niveau

* Level 0

## Voraussetzungen

* Modul CAN Protokoll
* Modul Microcontrollers Basics

## Lernziele

* Wie kann man das CAN Protokoll verlässlicher machen?
* Wie kann man das CAN Protokoll fehlerrobuster machen?

## Inhalt

* Duplikation von Maschinenteilen.
* Kommunikation, die anhand von Zeitabständen prioritisiert.

## Prüfung

* Multiple Choice Fragen

# Modul TTCAN Protokoll

## Niveau

* Level 0

## Voraussetzungen

* Modul CAN Protokoll
* Modul Microcontrollers Basics

## Lernziele

* Wie kann man das CAN Protokoll echtzeitfähig machen?

## Inhalt

* Hingabe von Zeitslots an Masterknoten.

## Prüfung

* Multiple Choice Fragen

# Modul VHDL

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Elektrische Schaltungen entwerfen
* Einführung in VHDL Sprache

## Inhalte

* Was ist eine Hardware Beschreibungssprache?
* Was ist VHDL?
* Was sind die wichtigsten Konzepte von VHDL?
* Drei Beispielmodelle in VHDL

* Multiple Choice

# Modul FPGA Simulation 1

## Niveau

* Level 2

## Voraussetzungen

* Modul VHDL

## Lernziele

* Selbst VHDL Modelle simulieren
* Simulationen richtig betrachten und analysieren

## Inhalte

* Erstelle TCL Dateien für eine Simulation mit `ModelSim\*-Intel® FPGA Edition Software`.
* Schreibe `.do` Skripte für eine Simulation mit `ModelSim\*-Intel® FPGA Edition Software`.

# Modul FPGA Simulation 2

## Niveau

* Level 2

## Voraussetzungen

* Modul VHDL
* Modul FPGA Simulation 1

## Lernziele

* Selbst VHDL Modelle simulieren
* Simulationen richtig betrachten und analysieren

## Inhalte

* Erstelle TCL Dateien für eine Simulation mit `ModelSim\*-Intel® FPGA Edition Software`.
* Schreibe `.do` Skripte für eine Simulation mit `ModelSim\*-Intel® FPGA Edition Software`.
* Kompiliere VHDL Modelle.
* Simuliere elektrische Schaltungen mit `ModelSim\*-Intel® FPGA Edition Software`.
* Simuliere elektrische Schaltungen mit `Quartus Prime Pro Edition`.
* Schau Dir simulierte Signale an:
  * CLOCK
  * WE
  * OFFSET
  * RESET_N
  * RD_DATA

# Modul [LTSpice](https://de.wikipedia.org/wiki/LTspice)

## Niveau

* Level 2

## Voraussetzungen

## Lernziele

* Simuliere elektrische Schaltungen
* Entwerfe die Peripherie eines Microcontrollers
* Entferne ein Microcontroller Board

## Inhalte

* Einfache elektrische Schaltungen wie z.B. ein Halbaddierer oder Volladdierer
* Was sind Schemata von elektrischen Schaltungen?
* Schemata editieren
* Wellenform von Signalen beobachten und analysieren
* Beobachte die Spannungswerte, während die Simulation läuft
* .ASC Dateien erstellen

# Modul C++ Level 0

## Niveau

* Level 0

## Lernziele

* Wie liest man C++ Programme?
* Welche [Konzepte und Schlüsselwörter](https://www.tutorialspoint.com/cplusplus/cpp_basic_syntax.htm) gibt es in C++?

## Inhalte

* C++ Kontrollflussdiagramme
* C++ Schleifen
* C++ Bedingungen
* C++ Funktionen
* C++ Arrays
* C++ Zahlen
* C++ Klassen
* C++ auto keyword

# Modul C++ Level 1

## Niveau

* Level 1

## Lernziele

* Die String Klasse und ihre verschiedenen Methoden

## Inhalte

* C++ Strings: Finde eine fortlaufende Untersequenz vom String, wie `Hallo` von `Hallo Welt!`.
* C++ Strings: Finde eine nicht-fortlaufende Untersequenz vom String, wie `loelt` von `Hallo Welt!`.
* C++ Strings: Erstelle einen immer länger werdenden String.
* Analysiere den String:
  * Wo ist die Adresse des String Objekts? Wo ist seine reale Adresse?
  * Wie groß ist das String Objekt? Wie lang ist der String? Wie viel Speicher ist für den String reserviert?

# Modul C++ Level 2

## Niveau

* Level 2

## Lernziele

* Reguläre Ausdrücke mit C++

## Inhalte

* C++ [reguläre Ausdrücke](https://en.cppreference.com/w/cpp/regex) mit der `regex` Bibliothek
* Schreibe einen regulären Ausdruck für IBANs
* Schreib einen regulären Ausdruck für das Datum
* Schreib einen regulären Ausdruck für die Email.


# Modul Command Line Suchen

## Niveau

* Level 1

## Lernziele

* Dateioperationen mittels Linux Konsole

## Inhalte

Linux command line:
* `grep`:
  * Finde das Vorkommnis einer bestimmten Variable in einer C++ Quelldatei.
  * Finde das Vorkommnis einer bestimmten Variable in einem Ordner voll von C++ Quelldateien.
  * Gib pro Datei aus, wie oft dort `{` vorkommt.
* `find`:
  * Finde eine Datei, deren Namen einen bestimmte regulären Ausdruck macht und deren Größe größer 0 ist.
* `wc`: Zähle Anzahl der Zeilen von allen C++ Quelldateien in einem Ordner zusammen genommen.

# Modul Command Line Simple

## Niveau

* Level 0

## Lernziele

* Ordner anschauen

## Inhalte

Linux command line:
* `ls`:
  * Zeige den Inhalt eines Ordners an.
* `cat`:
  * Zeige den Inhalt einer Textdatei an.
* `cd`:
  * Wechsle den aktuellen Ordner.

# Modul Git I

## Niveau

* Level 0

## Lernziele

* Was ist git?

## Inhalte

* Wozu wird Git benutzt?
* Befehl `git init`
* Befehl `git checkout`
* Befehl `git add`
* Befehl `git commit`
* Befehl `git log`
* Befehl `git pull`
* Befehl `git push`
* Befehl `git remote`

# Modul Git II

## Niveau

* Level 1

## Lernziele

* Einen Git Merge Konflikt manuell auflösen

## Inhalte

* Befehl `git merge`
* Befehl `git tag`
* Löse Merge Konflikt mit Sublime Merge

# Modul ARM Assembly

## Niveau

* Level 2

## Lernziele

* Programmiere einen Mikroprozessor mit der ARM Instruction Set Architektur

## Inhalte

* Was ist der Befehlssatz in der ARM Architektur?
* Schreibe ein Programm in der ARM Architektur, welches einen algebraischen Ausdruck in Infixnotation in einen algebraischen Ausdruck in Postfix Notation umschreibt.

# Modul x86 Assembly

## Niveau

* Level 2

## Lernziele

* Programmiere einen Mikroprozessor mit der x86 Instruction Set Architektur

## Inhalte

* Was ist der Befehlssatz in der x86 Architektur?
* Schreibe ein Programm in der x86 Architektur, welches einen algebraischen Ausdruck in Infixnotation in einen algebraischen Ausdruck in Postfix Notation umschreibt.

# Modul C++ Cross Build

## Niveau

* Level 1

## Voraussetzungen

* C++ Level 0

## Lernziele

* Wie man einen Buildserver baut, welcher Kompilate, z. B. Nightly Builds, für verschiedene Zielplattformen erzeugt.
* Kompiliere C++ Code für eine fremde CPU Architektur.
* Kompiliere C++ Code für ein fremdes Betriebssystem.

## Inhalte

* Cross build with `gcc`.

# Modul [QEMU](https://www.qemu.org/)

## Niveau

* Level 2

## Voraussetzungen

* C++ 3
* Modul C++ Cross compilation

## Lernziele

* Faster feedback cycle compared to hardware.
* Emuliere einen anderen Computer von anderer Befehlssatzarchitektur.
* Emuliere die CPU Architektur ARMv8 von einem Raspberry Pi 3 Model A+.
* Emuliere die CPU Architektur ARMv7 von einem Raspberry Pi 2 Model B.
* Spare Kosten, die durch Missverhalten von Computern auftreten können.
* Verifiziere, dass Dein Code auf der eingeplanten Maschine richtig läuft, um auch die spezifischen Probleme der eingeplanten Maschine zu lösen.

## Inhalte

* Simuliere einen ARMv7 Computer auf einem x86 Computer.
* Führe eine ARMv7 Binärdatei innerhalb der Simulation eines ARMv7 Computers auf einem x86 Computer aus.

# Modul [Sensor and Actuator AUTOSAR Pattern](https://www.autosar.org/fileadmin/user_upload/standards/classic/4-2/AUTOSAR_TR_AIDesignPatternsCatalogue.pdf)

## Niveau

* Level 2

## Voraussetzungen


## Lernziele

* Wie strukturiere ich meine Software für Sensoren und Aktuatoren von verschiedenen Herstellern für dieselbe Automobilfunktion?
* Wie schreibe ich Code, der wiederverwendbar für mehrere Sensoren und Aktuatoren von verschiedenen Herstellern ist?

## Inhalte
Sensor and Actuator AUTOSAR Pattern
* Sensor and Actuator AUTOSAR Pattern
* Ein Beispiel für die Verbesserung eines Systems bestehend aus einer Lampe und einem Geschwindigkeitssensor durch dieses Muster.

# Modul AUTOSAR Blockset

## Niveau

* Level 2

## Voraussetzungen

* Modul Sensor and Actuator AUTOSAR Pattern

## Lernziele

* Was ist die `AUTOSAR Blockset` Software?
* Wie installiert man die `AUTOSAR Blockset` Software?
* Wie benutzt man die `AUTOSAR Blockset` Software?

## Inhalte

* Wie erstelle ich AUTOSAR XML Dateien mit Simulink Modellen?
* Wie kann ich atomare Softwarekomponenten in Simulink Modellen zu einer größeren Softwarekomponente zusammensetzen?
* Wie emuliere ich meine größere Softwarekomponente auf der richtigen Maschine?
* Wie generiere ich C/C++ Code mit `AUTOSAR Blockset`?

# Modul Vehicle Network Toolbox

## Niveau

* Level 2

## Voraussetzungen

* Modul CAN Protokoll

## Lernziele

* Wie simuliert man CAN Netzwerke?

## Inhalte

* Wie können wir ein CAN Netzwerk simulieren?
* Was sind CAN Datenbanken?
* Wie definiert man CAN Nachrichten für die Simulation eines CAN Netzwerks?
* Was sind Kalibrationsprotokolle wie CCP und XCP?
* Wie verbindet man MATLAB zu einer Simulation eines CAN Netzwerks?
* Wie verbindet man Simulink zu einer Simulation eines CAN Netzwerks?

# Modul 64 bit Mikroprozessor Programmierung

## Niveau

* Level 2

## Voraussetzungen

* Modul ARM Assembly
* Modul C++ Level 0
* Modul QEMU

## Lernziele

* Programmierung eines ARMv8 Prozessors

## Inhalte

* Programmiere den ARMv8 Mikroprozessor von Raspberry Pi 3 Model A+.
* Schreib ein ARMv8 Assembly Programm für den Raspberry Pi 3 Model A+.

# Modul 32 bit Mikroprozessor Programmierung

## Niveau

* Level 2

## Voraussetzungen

* Modul ARM Assembly
* Modul C++ Level 0
* Modul QEMU

## Lernziele

* Programmierung eines ARMv7 Prozessors

## Inhalte

* Programmiere den ARMv7 Mikroprozessor von Raspberry Pi 2 Model B.
* Schreib ein ARMv7 Assembly Programm für den Raspberry Pi 2 Model B.

# Modul Microcontroller Basics

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was ist ein Microcontroller?
* Wofür ist ein Microcontroller gut?

## Inhalte

* System on a chip
* Was ist die Peripherie?
* CAN-Schnittstelle
* LIN-Schnittstelle
* LCD-Controller
* Betriebssysteme für Microcontroller

# Modul Protokoll Basics

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was ist ein Kommunikationsprotokoll?

## Inhalte

* Was ist ein Kommunikationsprotokoll?
* Wozu ist ein Kommunikationsprotokoll gut?
* Was ist der einfachste Kommunikationsprotokoll?
* Wie geht uART?

# Modul C++ If Abfragen

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Wie verzweigt man den Code?
* Wie vergabelt man den Kontrollfluss im Code?

## Inhalte

* Boolesche Verknüpfungen
* If Konstrukt
* If else Konstrukt
* switch/case Konstrukt

# Modul C++ Schleifen

## Niveau

* Level 0

## Voraussetzungen

* Modul C++ If Abfragen

## Lernziele

* Was sind Schleifen im Computerprogramm?

## Inhalte

* Wo kommt die Komplexität von Code her?
* Wie kann man an denselben Punkt im Code zurückkehren, an dem man schon mal war?
* Was ist eine "Schleife" im Code?
* Wie sieht das Kontrollflussdiagramm einer Schleife aus?

# Modul C++ Signal Handling

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Wie können zwei verschiedene Prozesse miteinander kommunizieren?

## Inhalte

* Funktion `signal()`
* Funktion `sigaction()`
* Was sind Linux Signale?

# Modul [Micro Python pyboard](https://micropython.org/unicorn/)

## Niveau

* Level 2

## Voraussetzungen

* Modul Microcontrollers Basics

## Lernziele

* Kann Python auf einem Microcontroller benutzt werden?

## Inhalte

* List
* Dictionaries
* komplexe Zahlen
* große Zahlen
* Kontrolliere die LEDs
* Lies die Zustände der Schalter des Microcontrollers ab.

# Modul Basics about FPGAs

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was sind Field Programmable Gate Arrays?

## Inhalte

* Was sind Field Programmable Gate Arrays?
* Wie kann man sie programmieren?
* Wie unterscheiden sie sich von Prozessoren?

# Modul Basics about Ethernet

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was ist Ethernet?

## Inhalte

* Was ist Ethernet?
* Wofür ist Ethernet da?
* Welche Versionen gibt es?
* Welche Übertragungsgeschwindigkeiten sind möglich?

# Modul LIN Protokoll

## Niveau

* Level 0

## Voraussetzungen

* Modul Protokolle

## Lernziele

* Was ist das LIN Protokoll?

## Inhalte

* Welche seriellen Netzwerkprotokolle zur Kommunikation von Mikrocontrollern im Fahrzeug gibt es?
* Was ist LIN?
* Was ist das LIN Protokoll?

# Modul OSEK

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was sind die verschiedenen OSEK Standards?

## Inhalte

* Welche OSEK Standards gibt es?
* Was standardisiert OSEK-TIME?
* Was standardisiert OSEK-NM?
* Was standardisiert OSEK-COM?
* Was standardisiert OSEK-ORTI?
* Was standardisiert OSEK-OIL?

# Modul 8 bit PICmicro

## Niveau

* Level 2

## Voraussetzungen

## Lernziele

* Wie programmiert man einen 8 bit Microcontroller?

## Inhalte

* Programmiere einen 8 bit Microcontroller der Familie PICmicro

# Modul 16 bit PICmicro

## Niveau

* Level 2

## Voraussetzungen

## Lernziele

* Wie programmiert man einen 16 bit Microcontroller?

## Inhalte

* Programmiere einen 16 bit Microcontroller der Familie PICmicro

# Modul Basics über Netzwerkbusse

## Niveau

* Level 0

## Voraussetzungen

## Lernziele

* Was sind Busse?

## Inhalte

* Was sind Busse?
* Wie werden Busse zur Datenverarbeitung benutzt?
