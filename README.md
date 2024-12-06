# BookBot: Text Analysis Command-Line Application
## Overview
This project is a Python-based command-line application designed to perform static analysis on text files, specifially novels like *Frankenstein*. It was developed as part of the **Boot.dev** course title *"Build a Bookbot"*.

## Purpose
The purpose of this project is to introduce Python programming fundamentals while working with a real-world use case. It involves setting up a professional development environment using VS Code, Git and GitHub.

## Features 
Bookbot processes text files and provides a detailed analysis, including:
- The total number of words in the document.
- The frequency of each alphabetic character in the text, sorted by usage.

## How It Works
1. The program reads the text file (*Frankenstein* in this case) from a specified path.
2. It calculates
    - The total word count
    - The frequency of each alphabetic character in the text
3. A summary report is displayed in the console with these insights.

## Usage
Download the full content of Frankenstein book [here](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt)

Ensure the text file is located in the `books/` directory and named `frankenstein.txt`

Run the application from the command line using the following command:
```bash
python3 main.py
```
