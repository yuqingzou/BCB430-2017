import os
import numpy as np

def loaddata(indir):
	markMat = np.loadtxt(os.path.join(indir, '.mat'), dtype=str)
	Mat = np.loadtxt(os.path.join(indir, '.mat'), dtype=str)
	return methyMat, transMat

def mat2dict(mat):
	result = dict()
	for i in range(len(mat[0, :])):
		result[mat[0, i]] = mat[1:, i]
	return result