#!/usr/bin/env python

import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go


def plotWordCounts():
	full_words = open('../data/full_word_list.txt', 'r')
	frequencies = []
	filterCount = 0

	for line in full_words:
		if not line.strip().startswith("#"):
			word_arr = line.split('<SEP>')

			if int(word_arr[1]) > 5:
				filterCount += 1
			
			frequencies.append(int(word_arr[1]))

	full_words.close()

	indexes = range(len(frequencies))

	plt.plot(indexes, frequencies)
	plt.xlabel('Terms')
	plt.ylabel('Term Counts')
	plt.title('Total terms and their Counts')
	plt.yscale('log')
	plt.xscale('log')
	plt.show()

	print 'Total number of terms and filtered terms', len(indexes), filterCount


def plotTermFrequencies():
	train_data = open('../data/mxm_dataset_train.txt', 'r')

	term_frequencies = {}

	for line in train_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			term_counts = line.strip().split(',')

			for i in range(2, len(term_counts)):
				freq = term_counts[i].strip().split(':')[1]

				if freq in term_frequencies:
					term_frequencies[freq] += 1
				else:
					term_frequencies[freq] = 1

	train_data.close()

	test_data = open('../data/mxm_dataset_test.txt', 'r')

	for line in test_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			term_counts = line.strip().split(',')

			for i in range(2, len(term_counts)):
				freq = term_counts[i].strip().split(':')[1]

				if freq in term_frequencies:
					term_frequencies[freq] += 1
				else:
					term_frequencies[freq] = 1

	test_data.close()

	max_term_freq = int(max(term_frequencies.keys(), key=int))

	freq_counts = [0] * max_term_freq

	for key, val in term_frequencies.iteritems():
		freq_counts[int(key)-1] = int(val)

	indexes = range(max_term_freq)

	plt.plot(indexes, freq_counts)
	plt.xlabel('Term Frequencies')
	plt.ylabel('Counts')
	plt.title('Term Frequency Distribution')
	plt.yscale('log')
	plt.xscale('log')
	plt.show()

	print 'Total term frequencies -', max_term_freq


def plotDocumentFrequencies():
	track_count = 0

	train_data = open('../data/mxm_dataset_train.txt', 'r')

	document_frequencies = {}

	for line in train_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			track_count += 1
			term_counts = line.strip().split(',')

			for i in range(2, len(term_counts)):
				term = term_counts[i].strip().split(':')[0]

				if term in document_frequencies:
					document_frequencies[term] += 1
				else:
					document_frequencies[term] = 1

	train_data.close()

	test_data = open('../data/mxm_dataset_test.txt', 'r')

	for line in test_data:
		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			track_count += 1
			term_counts = line.strip().split(',')

			for i in range(2, len(term_counts)):
				term = term_counts[i].strip().split(':')[0]

				if term in document_frequencies:
					document_frequencies[term] += 1
				else:
					document_frequencies[term] = 1

	test_data.close()

	max_doc_freq = int(max(document_frequencies.keys(), key=int))

	doc_counts = [0] * max_doc_freq

	for key, val in document_frequencies.iteritems():
		doc_counts[int(key)-1] = int(val)

	indexes = range(max_doc_freq)

	plt.plot(indexes, doc_counts)
	plt.xlabel('Document Frequencies')
	plt.ylabel('Counts')
	plt.title('Document Frequency Distribution')
	plt.yscale('log')
	plt.xscale('log')
	plt.show()

	print 'Total document frequencies -', max_doc_freq, track_count



plotDocumentFrequencies()
#plotTermFrequencies()
#plotWordCounts()