#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:11:40 2017

@author: yisubai
"""

def sample_region(indir,location,interval):
    allMat = np.loadtxt(os.path.join(indir, '.pkl'), dtype=str, allow_pickle =True)