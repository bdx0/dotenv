from distutils.core import setup
import py2exe

setup(windows=['gui.py'],
    console=['console.py']
)
