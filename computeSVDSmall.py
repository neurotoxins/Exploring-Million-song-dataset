import numpy as np
import scipy.sparse.linalg
from scipy import linalg

def getSVD():
	train_data = open('../data/mxm_dataset_train.txt', 'r')

	input_matrix = []

	for line in train_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			term_counts = line.strip().split(',')

			feature_vector = [0]*5000

			for i in range(2, len(term_counts)):
				term = term_counts[i].strip().split(':')[0]
				freq = term_counts[i].strip().split(':')[1]

				feature_vector[int(term)-1] = float(freq)

			input_matrix.append(feature_vector)

	train_data.close()

	test_data = open('../data/mxm_dataset_test.txt', 'r')

	for line in test_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			term_counts = line.strip().split(',')

			feature_vector = [0]*5000

			for i in range(2, len(term_counts)):
				term = term_counts[i].strip().split(':')[0]
				freq = term_counts[i].strip().split(':')[1]

				feature_vector[int(term)-1] = float(freq)

			input_matrix.append(feature_vector)

	test_data.close()

	print 'Computing SVD ...'
	#U, s, Vh = linalg.svd(input_matrix)
	U, s, Vh = scipy.sparse.linalg.svds(input_matrix, k=1000, which='LM')
	print 'Process complete .. '
	#U.shape, Vh.shape, s.shape

	print 'Singular Values -', s, len(s)


getSVD()