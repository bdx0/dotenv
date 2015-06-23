import sys
import os
import subprocess
import bygit
import list_repo as lp

script_directory_path = os.path.dirname(os.path.realpath(sys.argv[0])
sys.path.append(script_directory_path)

def main():
    glog = ''
    for item in lp.list_repo:
        cmd = ['git', 'push','-u origin', '--all']
        pfetch=subprocess.popen(
            cmd, cwd=item, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        plog = pfetch.communication()[0]

    print glog

if __name__ == "__main__":
    main()
