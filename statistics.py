import numpy as np
from scipy.cluster.vq import kmeans2

import processing
from rm4scc import RM4SCC


def getFeatures(contours):
    """Extract the relevant features from the list of contours given and return them"""
    features = map(processing.getAreaAndCentroid, contours)
    # Use x-position to sort, and then get rid of it
    features.sort(key=lambda t: t[1])
    features = [(area, y) for (area, x, y) in features]
    features = np.array(features)

    return features

def computeClusteringInitialPoints(features):
    """Return the initial centroids to use when clustering"""
    # To ease decoding, we define the initial centroid in the same order the symbols are defined in RM4SCC
    initial_centroids = np.array([
        [features[:,0].min(), features[:,1].mean()],  # 'S'
        [features[:,0].mean(), features[:,1].max()],  # 'D'
        [features[:,0].mean(), features[:,1].min()],  # 'A'
        [features[:,0].max(), features[:,1].mean()],  # 'L'
    ])

    return initial_centroids

def classifySymbols(features, initial_centroids):
    """Run the k-means algorithm against the features using initial_centroids as the starting points for clustering.
    Try and remove any outlier, i.e. any point more than avg+3sigma away from its centroid."""
    centroids, labels = kmeans2(features, initial_centroids)

    # Compute all distances from the relative centroid
    distances = []
    from math import sqrt
    for idx, label in enumerate(labels):
        centroid = centroids[label]
        point = features[idx]
        d = sqrt((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)
        distances.append(d)

    # Remove outliers
    distances = np.array(distances)
    d_mean = distances.mean()
    d_std = distances.std()
    for idx, d in enumerate(distances):
        if d > d_mean + 3*d_std:
            labels = np.delete(labels, idx)

    symbols = map(lambda i: RM4SCC.symbols[i], labels)

    return symbols, centroids
