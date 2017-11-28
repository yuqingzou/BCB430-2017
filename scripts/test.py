#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:11:27 2017

@author: yisubai
"""

import pickle

with open('DNase-seq-human-chr1.pkl', 'rb') as f:
        mynewlist = pickle.load(f)
        print(mynewlist)
        print(len(mynewlist))
x