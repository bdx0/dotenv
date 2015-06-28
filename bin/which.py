#!/usr/bin/env python
""" which.py --- the which command implement in python
@Author: duongbaoduy
@Version: 0.0.1
"""
""" Commentary:
"""
""" Code: """
import os
import sys

local_path = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(local_path, 'ovis'), 'rb').read())

def main(argv):
    pass

if __name__ == "__main__":
    main(sys.argv)
