import sys
import os
import subprocess as sps

script_directory_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_directory_path)
execfile(os.path.join(script_directory_path,'list_repo'))

def main():
  glog = ''
  for item in list_repo:
    print item
    cmd = ['git', 'push', '-u', 'origin', '--all']
    pfetch = sps.Popen(
        cmd, cwd=item, stdout=sps.PIPE, stderr=sps.PIPE)
    for line in pfetch.stdout:
      glog = glog + line
      print line

    for line in pfetch.stderr:
      glog = glog + line
      print line
    
    pfetch.wait()

if __name__ == "__main__":
  main()
