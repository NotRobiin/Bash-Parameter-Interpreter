import sys
import os

# To move into the directory of bash
path = os.getcwd()

# Commit message is the last argument
msg = sys.argv[-1]

# Actual command send to the windows terminal
cmd = f'cd "{path}" && git add . && git commit -m "{msg}" && git push'

os.system(cmd)
