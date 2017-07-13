import plotly.plotly as py
py.sign_in('Sateesh.tata', '6gunkyylym')
import plotly.graph_objs as go

import matplotlib.pyplot as plt

genre_mapping = {}

def plotGenres():
	genre_data = open('../data/msd_genre_dataset.txt', 'r')

	genre_frequencies = {}
	track_count = 0

	for line in genre_data:
		track_count += 1

		if not line.strip().startswith("#") and not line.strip().startswith("%"):
			term_counts = line.strip().split(',')

			genre = term_counts[0].strip()
			track_id = term_counts[1].strip()

			if genre in genre_frequencies:
				genre_frequencies[genre] += 1
			else:
				genre_frequencies[genre] = 1

			if genre in genre_mapping:
				genre_mapping[genre].append(track_id)
			else:
				genre_mapping[genre] = [track_id]

	genre_data.close()

	genres = []
	counts = []

	for key, val in genre_frequencies.iteritems():
		genres.append(key)
		counts.append(int(val))

	data = [
	    go.Bar(
	        x = genres,
	        y = counts
	    )
	]
	plot_url = py.plot(data, filename='basic-bar')

	print 'Genre Frequencies -', genre_frequencies, track_count


plotGenres()