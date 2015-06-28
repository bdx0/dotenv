""" targets.py ---
@Author duongbaoduy
@Version 0.0.1
"""
""" Commentary:
"""
""" Code: """
import os
import sys

print 'load ', __file__

function_list = []
def method_singleton(function):
    global function_list
    def decorated_method(*args, **kwargs):
        if function.__name__ not in function_list:
            function_list.append(function.__name__)
            return function(*args, **kwargs)
        else:
            print "Method %s already called"%function.__name__
    return decorated_method

@method_singleton
def example():
    print 'Hello ', function_list
    # print "Helllo ", sys._getframe(1).f_code.co_name

def someother():
    print 'Hello', someother.__name__
