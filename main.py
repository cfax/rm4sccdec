#!/usr/bin/env python

import sys
from cv2 import imread
# import cv2

import processing, statistics
from rm4scc import RM4SCC


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: {} image_filename.ext'.format(sys.argv[0])

    img = imread(sys.argv[1])
    processed = processing.prepareImage(img)
    contours = processing.findContours(processed)

    features, initial_centroids = statistics.getFeatures(contours)

    symbols = statistics.classifySymbols(features, initial_centroids)

    codeword = RM4SCC.decodeSymbols(symbols)
    print codeword

    # cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    # cv2.imwrite('code_cv.jpg', img)
