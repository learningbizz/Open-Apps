#!/usr/bin/env python3
#To enable the shebang, you have to give the file permission of execution: chmod +x name_of_the_file.py

import sys
import subprocess
from programming_preset import python, front

def main():
  args = sys.argv[1:]
  
  if not args:
    print('Add an existing preset, like "programming"')
    sys.exit(1)

  #Remember when adding a preset, add it in the bashrc or the zshrc depends what you use
  if args[0] == "python":
    python()
  elif args[0] == "front":
    front()

if __name__ == '__main__':
  main()
