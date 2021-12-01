#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Demo CUI-APP for VisualCMD
This APP counts the number of input arguments and prints them one by one.
'''

import sys


print('APP path: %s'%(sys.argv[0]))



allags=sys.argv[1:]
agsnu=len(allags)
print('%s arguments received!'%agsnu)


cn=1
for ea in allags:
    print('Argument %s: %s'%(cn,ea))
    cn+=1

print('\n>>>Number counting: ')

for ea in range(20000):
    print(ea,' ...')

print('The end!')


