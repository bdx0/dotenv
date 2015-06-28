#!/usr/bin/env python
"""" ovis.py --- ovis supporter
@Author: dbd
@Version: 0.0.1
"""
""" Commentary:
"""

""" Code: """
import sys
import os


local_path = os.path.dirname(os.path.realpath(__file__))

exec(open(os.path.join(local_path, 'ovis'), 'rb').read())

if __name__ == "__main__":
  main(sys.argv)
