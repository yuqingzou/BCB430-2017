#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:58:29 2017

@author: yisubai
"""
import os
import numpy as np
import pickle
import random

def annotation(time,size):
    """"
    make a matrix of DNA annotation for a region: gather the binary arrays from all the marks\
    Return: matrix of DNA annotation
    """
    

    result = np.array([])
    for i in range(time):
        rad_chrom_num = random.randint(1,22)
        print("this is %s time" % i)
        for root, dirs, files in os.walk("/mnt/raisin/yuqing/pkl/chr"+str(rad_chrom_num)):
            print('Found directory: %s' % root)
            allflattenRow = np.array([])
            for fname in files:
                print('\t%s' % fname)
                if fname.endswith(".pkl"):
                    opencontacts = pickle.load(open("/mnt/raisin/yuqing/pkl/chr" +str(rad_chrom_num)+'/'+ fname, 'rb'))
                    startNum = random.randint(0,len(opencontacts)-size+1)  
                    print('star :%d, and max :%d' % (startNum,len(opencontacts)))                  
                    flattenRow = np.asarray(opencontacts[startNum:startNum+size]).flatten()
                allflattenRow = np.append(allflattenRow, flattenRow)
                print("now allflattenRow size is %s" % allflattenRow.size)
            result = np.concatenate((result, allflattenRow), axis=0)
    result.shape = (time,3*size)
    #save the result into pickle
    with open('/mnt/raisin/yuqing/pkl/annotate/'+str(time)+'_'+str(size)+'.pkl', 'wb') as f:
        pickle.dump(result,f)




def main():
    annotation(1000,1000)


if __name__ == "__main__":
    main()
