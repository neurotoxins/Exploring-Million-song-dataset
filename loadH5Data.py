from __future__ import print_function
import numpy as np
import h5py

with h5py.File('../data/sample.h5','r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    data = hf.get('analysis')
    metaData = hf.get('metadata')
    music = hf.get('musicbrainz')
    #np_data = np.array(data)
    print('Shape of the array analysis: \n', music.get('songs'))