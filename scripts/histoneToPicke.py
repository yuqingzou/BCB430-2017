import numpy as np
import pandas as pd
import pickle


def read_input(inputdata = 0, reference = 0, datatype = "histon-mark", cellline = "H3K27me3"):
    """
    Return: pickle cantains list with design chr order
    convert the bed file to binary formate for each chr and output as a pickle for whole chr
    """
    df = pd.read_csv('/mnt/raisin/yuqing/E001-H3K27me3.narrowPeak',sep="\t" , error_bad_lines=False, header = None)
    chrom_list = {}
    print(list(df.columns.values))

    
    #mostly wrong here?
    chrom_list['chr1'] = [0]*249250621
    chrom_list['chr2'] = [0]*243199373
    chrom_list['chr3'] = [0]*198022430
    chrom_list['chr4'] = [0]*191154276
    chrom_list['chr5'] = [0]*180915260
    chrom_list['chr6'] = [0]*171115067
    chrom_list['chr7'] = [0]*159138663
    chrom_list['chr8'] = [0]*146364022
    chrom_list['chr9'] = [0]*141213431
    chrom_list['chr10'] = [0]*135534747
    chrom_list['chr11'] = [0]*135006516
    chrom_list['chr12'] = [0]*133851895
    chrom_list['chr13'] = [0]*115169878
    chrom_list['chr14'] = [0]*107349540
    chrom_list['chr15'] = [0]*102531392
    chrom_list['chr16'] = [0]*90354753
    chrom_list['chr17'] = [0]*81195210
    chrom_list['chr18'] = [0]*78077248
    chrom_list['chr19'] = [0]*59128983
    chrom_list['chr20'] = [0]*63025520
    chrom_list['chr21'] = [0]*48129895
    chrom_list['chr22'] = [0]*51304566
    

    for i, row in enumerate(df.itertuples(), 1):
        if row[0] in chrom_list:
            chrom_list[row[0]][int(row[1]):int(row[2])] = [1]*(int(row[2])-int(row[1]))

    for lists in chrom_list:  
        with open('/mnt/raisin/yuqing/pkl/'+lists+'/'+datatype+'-'+cellline+'-'+lists+'.pkl', 'wb') as f:
            pickle.dump(chrom_list[lists], f)
            
def main():
    read_input()


if __name__ == "__main__":
    main()
