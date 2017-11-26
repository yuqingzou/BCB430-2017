import os
import numpy as np
from utils import mat2dict
from collections import defaultdict

def collapse(methyMat, reference, distance, collapse):
	start, end = [int(d) for d in distance.split(',')]
	methyDict = mat2dict(methyMat)
	probesInfo = np.loadtxt(os.path.join(reference, '450k.txt'), dtype=str)
	genesDict = defaultdict(list)
	for probe in probesInfo:
		if probe[1] > (int(probe[5]) - start) and probe[1] < (int(probe[5]) + end):
			try:
				genesDict[probe[-1]].append([methyDict[probe[3]], (int(probe[5])-int(probe[1]))])
			except KeyError:
				continue

	collapseDict = dict()
	for gene in genesDict:
		if collapse == 'mean':
			values = np.array([t[0] for t in genesDict[gene]])
			collapseDict[gene] = np.mean(values, axis=1)

	return collapseDict


