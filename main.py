#!/usr/bin/env python3
#To enable the shebang, you have to give the file permission of execution: chmod +x name_of_the_file.py

import sys
import subprocess
from program_preset import programming_preset

def main():
  args = sys.argv[1:]
  
  if not args:
    print('Add an existing preset, like "programming"')
    sys.exit(1)
  
  if args[0] == "programming":
    programming_preset()

if __name__ == '__main__':
  main()
