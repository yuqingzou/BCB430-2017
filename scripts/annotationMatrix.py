#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:58:29 2017

@author: yisubai
"""

def annotation(indir,location,interval):
    """"
    make a matrix of DNA annotation for a region: gather the binary arrays from all the marks\
    Return: matrix of DNA annotation
    """"
    
    #do we need dna sequence?
    allMat = np.loadtxt(os.path.join(indir, '.pkl'), dtype=str, allow_pickle =True)
    
    