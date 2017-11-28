from random import randint
import numpy as np
from random import randint


def sample_region(indir,location,interval = 1000):
	random_chr_num = randint(1, 22)
	random_chr = np.load('/mnt/raisin/yuqing/collapse/' + 'chr' + random_chr_num + '.dat')

	chr_size = random_chr.shape[1]
	half = interval/2
	random_mid_point = randint(half,(chr_size-half))

	sample_array = random_chr[random_mid_point-half:random_mid_point+half]

	return sample_array

def main():
    sample_region()


if __name__ == "__main__":
    main()
