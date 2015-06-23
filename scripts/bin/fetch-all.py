import sys
import os
import subprocess
import bygit

script_directory_path = os.path.dirname(os.path.realpath(sys.argv[0])
sys.path.append(script_directory_path)

if __name__ == "__main__":
    bygit.fetch('dotenv')
