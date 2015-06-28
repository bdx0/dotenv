#!/usr/bin/env python
""" git.py --- the wrapper of git command
@Author: duongbaoduy
@Version: 0.0.1
"""
""" Commentary:
"""
""" Code: """
import os
import sys
import subprocess as sp

local_path = os.path.dirname(os.path.realpath(__file__))
exec(open(os.path.join(local_path, 'git'), 'rb').read())


def main1(argv):
  print 'git wrapper'

if __name__ == "__main__":
  main(sys.argv)
