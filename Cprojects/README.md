C Mini Projects: File Opener & Text-to-Speech


This repository contains two mini C programs showcasing:

System commands in C

User input handling

Integration with external tools

📂 Project 1: File Opener (Windows)
✨ Overview

A command-line utility that opens files with their default Windows application.

Features:

Open files instantly using:

start filename.txt


Detects:

Invalid commands

Missing file names

Non-existent files

Loops until exit is entered

Friendly greetings and goodbye messages

🛠 Implementation Details

Used system() to run the Windows start command

Parsed user commands with fgets() and strncmp()

Checked file existence using GetFileAttributes()

Continuous loop for an interactive CLI

▶️ How to Run
# Compile
gcc file_opener.c -o file_opener

# Run
file_opener.exe

🗣 Project 2: Text-to-Speech (TTS) with eSpeak
✨ Overview

A simple command-line program that speaks the user’s input using eSpeak.

Features:

Immediately converts typed text to speech

Prevents speech if no text is entered

Exits gracefully with exit

🛠 Implementation Details

Called espeak via system()

Removed unwanted newline characters with strcspn()

Continuous read–execute loop

Error handling for empty input

▶️ Install eSpeak

Windows:

choco install espeak


Linux:

sudo apt install espeak


Mac:

brew install espeak

▶️ How to Run
# Compile
gcc tts.c -o tts

# Run
./tts

🏆 Skills Gained

C Programming: loops, conditionals, strings, system calls

Error Handling: validating file paths and user input

System Integration: using OS commands & third-party tools

User Experience: building interactive CLI apps

TTS Concepts: basic voice synthesis using external libraries

🔮 Future Improvements

Add Linux & Mac support for the File Opener project

Implement voice selection & speed control for TTS

Add file history log to track opened files

Build a GUI version using GTK or WinAPI

Include unit tests for input parsing functions

📜 Summary

These projects demonstrate the ability to:

Solve real-world problems using C

Integrate external tools like eSpeak

Build reliable and user-friendly CLI programs