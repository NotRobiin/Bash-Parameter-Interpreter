# Bash-Parameter-Interpreter
Simple script that essentially does three things:
- Moves to directory from which the script was called (cd ..)
- Adds unstaged files (git add .)
- Commits files (git commit -m)
- Sends files (git push)

The script is called by the git bash alias (.bash_profile):
```
alias gsend="python -u \"c:\Users\%USERNAME%\Desktop\.hidden\bash_parameter_interpreter\main.py\" '$1'"
```

The script's path is hardcoded, just because it is not a commercial thing, probably only for me.


This was made due to git bash not cooperating with aliases using parameters.
