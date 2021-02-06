#!/usr/bin/env python3
#To enable the shebang, you have to give the file permission of execution: chmod +x name_of_the_file.py

import sys
import subprocess
import shlex

def value(item):
    return item[1]

def programming_preset():
    dictionary = {}
    #Programs I want to open in their respective enviornments 
    dictionary["firefox"] = r"firefox"
    dictionary["terminal"] = r'gnome-terminal -- bash -c "cd /home/manuel/Desktop/Python/; ls; exec bash"'
    dictionary["vscode"] = r'code /home/manuel/Desktop/Python'
    dictionary["spotify"] = r'Spotify'

    for item in dictionary:
        arguments = shlex.split(dictionary[item])
        subprocess.Popen(arguments)

    #sys.exit(1)

    

