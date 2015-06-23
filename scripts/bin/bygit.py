import sys
import os
import subprocess

script_directory_path = os.path.dirname(os.path.realpath(sys.argv[0])
sys.path.append(script_directory_path)

repo_list = "" # get from json

def fetch(repo_id):
    cmd = []
    subprocess.popen(cmd, cwd=repoDir, stdout = subprocess.PIPE,stderr = subprocess.PIPE )
