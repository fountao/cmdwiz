#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


gcipcs=subprocess.Popen([r'''pythonw''',r'''..\..\GCI_ctor.py''',r'''demo_GCI.json'''],stdin=None,stdout=None,stderr=None,shell=False,close_fds=True)


