import numpy as np
import pandas as pd
import pickle
import glob


def collapse():
    """
    collapse all pickle into an big pickle, with all numpy array object
    """
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

    for i in range(22):
        chr_table = np.array(chrom_list['chr'+i])
        chr_order = []
        os.chdir("/mnt/raisin/yuqing/pkl/")
        for f in (glob.glob("*chr"+i+".pkl")):
            data = np.load(f)
            np.concatenate((chr_table, data), axis=0)
            chr_order.append(f)

        chr_table.dump('/mnt/raisin/yuqing/collapse/'+'chr'+i+'.dat')

        order_file = open("chr"+i+".txt", "w")
        order_file.write(chr_order)
        order_file.close()
        
    

            
def main():
    collapse()


if __name__ == "__main__":
    main()
