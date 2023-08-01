#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:29:53 2021

@author: alina
"""

import os
from multiprocess import Pool
from tqdm import tqdm

import numpy as np
import random
import umap
import hdbscan
from sklearn.metrics import adjusted_rand_score


number_of_cores = 10
pool = Pool(number_of_cores)


PATH = 'robustness_check/'
ITERATIONS = 1000


if not os.path.exists(PATH + f'data'):
    os.makedirs(PATH + f'data')


# initialize empty lists to collect results
label_collection = []
no_cluster_collection = []
random_seeds = []


def eval_loop(dummy):
    """computes UMAP & HDBSCAN with fixed parameters, but different random seedss"""
    strategy_embeddings = np.load('data/strategy_embeddings_masked.npy')
    
    random_seed = random.randint(0, 10**5)
        
    umap_test = umap.UMAP(n_neighbors=30,
                          min_dist=0.01,
                          n_components=30,
                          metric='cosine',
                          random_state=random_seed).fit_transform(strategy_embeddings)

    hdbscan_test = hdbscan.HDBSCAN(min_cluster_size=10,
                                   min_samples=30,
                                   metric='euclidean').fit(umap_test)
    
    return (hdbscan_test.labels_, max(hdbscan_test.labels_) + 1, random_seed)


# compute number of clusters and labels per random seed iteration
for batch in tqdm(pool.imap_unordered(func=eval_loop, iterable=range(ITERATIONS)),
                  total=ITERATIONS):
    label_collection.append(batch[0])
    no_cluster_collection.append(batch[1])
    random_seeds.append(batch[2])


# compute rand indices per pair of cluster solutions
rand_indices = []


for i in range(len(label_collection)):
    rand_scores = []
    for label_set in label_collection:
        rand_scores.append(adjusted_rand_score(label_collection[i], label_set))
    rand_indices.append(rand_scores)


# save results to files
np.save(PATH + f'data/random_seeds', random_seeds)
np.save(PATH + f'data/labels', label_collection)
np.save(PATH + f'data/no_clusters', no_cluster_collection)
np.save(PATH + f'data/ARI', rand_indices)
