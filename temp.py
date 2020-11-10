# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
infile = open ('input.txt')

outfile = open ('output.txt', 'w')
               
line = infile.readline()

outfile.write(str(int(line.split () [0] + int(line.split () [1]))
                   
infile.close()

outfile.close()