import os
import subprocess

project_dir = os.getcwd()

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[94m"
RESET_ALL = "\x1b[0m"

def environ():
    # Create the environment according to the user selection


    print(f"{MESSAGE_COLOR}Creating conda env (./env)...{RESET_ALL}")
    subprocess.call(["mamba", "env", "create", "--prefix", "./env", "--file", "environment.yml"])



def nb():
    # Set up Git diff for notebooks and lab
    nbdime = 'env/bin/nbdime'
    subprocess.call([f"{nbdime}", "config-git", "--enable"]) #configure it to this git project


environ()
nb()
