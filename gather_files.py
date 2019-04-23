"""
Preston Sergent
Practicing using subprocess to process system variables

"""
import subprocess
import cmd

Class fileshell(cmd.Cmd):
    





name = subprocess.check_output(["ls","-l"])
print(name.decode('utf8'))
