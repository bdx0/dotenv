#!/usr/bin/env python

# services.py ---
# Author: dbd
# Version: 0.0.1
###

# Commentary
##
###

# Code:

import os
import sys
import subprocess as sp
import time
import re

local_path = os.path.dirname(os.path.realpath(__file__))
services_file_path = os.path.join(local_path, '.services')


def main():
  if os.path.exists(services_file_path):
    with open(services_file_path, 'r') as f:
      for line in f.readlines():
        if not line.startswith('#'):
          cmd = re.findall(r'([a-zA-z-/_0-9&]+|".+")', line.rstrip())
          print 'start service:  %s' % cmd
          ps = sp.Popen(cmd, stdout=None, stderr=None, stdin=None,
                        close_fds=True, creationflags=0)
          # sp.DETA DETACHED_PROCESS)
          # print ps.communicate()[0]
          time.sleep(1)

      f.close()

if __name__ == "__main__":
  main()
