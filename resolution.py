# -*- coding: utf-8 -*-
"""
@author: Anna Galsanova
"""
filename = 'figure6.txt'
 
file = open(filename)
width = float(file.readline())
lines = file.readlines()
file.close()
lines = lines[1:]
 
line = lines[0]
line = line.split()
ilen = len(line)
 
r = width/ilen
print('Resolution is',r)