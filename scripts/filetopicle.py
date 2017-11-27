import numpy as np
import pandas as pd
import pickle


def read_input(inputdata = 0, reference = 0, datatype = "DNase-seq", cellline = "human"):
    """
    Return: pickle cantains list with design chr order
    convert the bed file to binary formate for each chr and output as a pickle for whole chr
    """
    df = pd.read_csv('/mnt/raisin/yuqing/GM12878_DNase.dms',sep="\t" , error_bad_lines=False, header = None)
    chrom_list = {}
    
    #mostly wrong here?
    chrom_list['chr1'] = [0]*248956422
    chrom_list['chr2'] = [0]*242193529
    

    for index, row in df.iterrows():
        if row[1] in chrom_list:
            print(row[1])
    	    chrom_list[row[1]][row[2]:row[3]] = [1]*(row[3]-row[2])
    print(chrom_list['chr1'])
    for lists in chrom_list:   
        with open(datatype+'-'+cellline+'-'+lists+'.pkl', 'wb') as f:
            pickle.dump(chrom_list[lists], f)
        
def main():
    read_input()


if __name__ == "__main__":
    main()
