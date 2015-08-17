#!/usr/bin/env python

import sys
from cv2 import imread

import processing, statistics
from rm4scc import RM4SCC


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: {} image_filename.ext'.format(sys.argv[0])

    img = imread(sys.argv[1])
    processed = processing.prepareImage(img)
    contours = processing.findContours(processed)

    features = statistics.getFeatures(contours)
    initial_centroids = statistics.computeClusteringInitialPoints(features)

    symbols, centroids = statistics.classifySymbols(features, initial_centroids)

    codeword = RM4SCC.decodeSymbols(symbols)
    print codeword
