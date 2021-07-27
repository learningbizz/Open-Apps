#!/usr/bin/env python3
#To enable the shebang, you have to give the file permission of execution: chmod +x name_of_the_file.py

import sys
import subprocess
import shlex

def value(item):
    return item[1]


#  OJO! If your working with bash, you will have to change all the "zsh" in the terminal item to "bash". Why? Because zsh is a substitute to it so yeah. 


def python():
    dictionary = {}
    #Programs I want to open in their respective enviornments 
    dictionary["firefox"] = r"firefox"
    dictionary["terminal"] = r'gnome-terminal -- zsh -c "cd /home/manuel/Desktop/python/; ls; exec zsh"'
    dictionary["vscode"] = r'code /home/manuel/Desktop/Python'
    dictionary["spotify"] = r'/usr/bin/spotify &'

    for item in dictionary:
        arguments = shlex.split(dictionary[item])
        subprocess.Popen(arguments)


def front():
    dictionary = {}
    #Programs I want to open in their respective enviornments 
    dictionary["firefox"] = r"firefox"
    dictionary["terminal"] = r'gnome-terminal -- zsh -c "cd /home/manuel/Desktop/front; ls; exec zsh"'
    dictionary["vscode"] = r'code /home/manuel/Desktop/front'
    dictionary["spotify"] = r'/usr/bin/spotify &'

    for item in dictionary:
        arguments = shlex.split(dictionary[item])
        subprocess.Popen(arguments)

    

    

