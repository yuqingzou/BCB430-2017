import argparse
import os
import scipy
import numpy as np
from scripts import *

parser = argparse.ArgumentParser(description="Run commands")
parser.add_argument('--reference', type=str, default="./data/",
                    help="database for annotation")
parser.add_argument('--indir', type=str, default="./data/test/",
                    help="input dir")
parser.add_argument('--outdir', type=str, default="./data/test/",
                    help="output dir")
parser.add_argument('--cpus', type=int, default="1",
                    help="number of CPUs")


def main():
    # args = parser.parse_args()
    # dataMat = utils.loaddata(args.indir)
    filetopicle.read_input()


if __name__ == "__main__":
    main()
    #yes?
