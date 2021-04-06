#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 100; truncate-lines: t -*-
#
# This file is part of Active-Learning-of-PES python package
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# If you use this programm for scientific work, you must correctly reference it; see LICENSE file
# for details.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

"""An example on how to use a query strategy to construct potential energy surf-
-aces with as few data as possible."""

import numpy as np
from libact.base.dataset import Dataset
from AL_PESs.query_strategies.stochastic_query_by_forest import SQBF
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import h5py as hp
from AL_PESs.nnutils import *

def LoadData(filename: str, No_iterations: int, initial_size: int):
    """Returns precalculated electronic structure calculations for pyrrole-water.

    Args:
    filename: the name of the file where data are stored.
    No_iterations: number of AL iterations required.
    initial_size: number of elements in the initialy-labeled-dataset.

    Output:
    D: Labeled and unlabeled dataset.
    Labeler: A function that returns the energy for an unlabeled geometry.
    D_oop: out of the pool (OOP) dataset. It's used for test purposed.
    D_v: a validation dataset, used to train a neural network.
    """
    items = {}
    def print_attrs(name, obj):
        for index, elem in enumerate(name):
            if elem == '/' in name:
                key = name[0:index]
                x = f.get(name)
                x = np.asarray(x)
                items[key] = x
    f = hp.File(filename, 'r')
    f.visititems(print_attrs)
    X = (items['ExpDistance'])
    Y = (items['Energies'])
    Y += np.abs(np.amin(Y))
    # Create an Out-Of-Pool dataset
    X, X_oop, Y, Y_oop = train_test_split(X, Y, test_size=0.1, random_state=3)
    # create a validation set for training the NN
    X, Xv, Y, Yv = train_test_split(X, Y, test_size=0.05, random_state=3)
    # create a labeler object
    Labeler = Y
    BatchSize = int(np.shape(Y)[0]/No_iterations)
    Indices = np.random.choice(np.arange(np.shape(Y)[0]), size=initial_size, replace=False) # to determine initial data
    Y = Y.tolist()
    for i in range(np.shape(Y)[0]):
        if i not in Indices:
            Y[i] = None
    Y = np.array(Y)
    D, D_oop, D_v = (X,Y), (X_oop, Y_oop), (Xv, Yv)
    return D, D_oop, D_v, Labeler, BatchSize

def main(No_iterations=20, initial_size=2458):
    filename_dat = 'data/dataset.h5'
    # Read data
    D, D_oop, D_v, Labeler, BatchSize = LoadData(filename_dat, No_iterations, initial_size)
    X, Y = D
    X_oop, Y_oop = D_oop
    Xv, Yv = D_v
    #create a dataset object
    dataset = Dataset(X=X, y=Y)
    #create a random forest model
    Trees = RFR(n_estimators=100, max_features=12, max_depth=None,
                min_samples_leaf=1, min_samples_split=2, bootstrap=False,
                max_samples=0.9, ccp_alpha=0.01, n_jobs=-1)
    iter = 0
    while dataset.len_unlabeled()>0: # While Pool isn't emtpy
        # get labeled entries in the pool
        X_L, y_L = dataset.get_labeled_entries()
        # train a random forest regressor on the labeled data
        Trees.fit(X_L, y_L)
        # Initialize SQBF object
        query_strategy = SQBF(Trees=Trees, BatchSize=BatchSize, dataset=dataset)
        # Compute the root mean squared error of the RFR model on the OOP data
        Error_RFR = np.sqrt(mean_squared_error(Y_oop, Trees.predict(X_oop)))
        print(f"Iteration: {str(iter)}, Model: RFR, OOP Error: {Error_RFR}")

        # Initialize a neural network and train it
        NN = MLPmodel()
        NN = MLPtrain(NN, X_L, y_L, Xv, Yv)
        # Compute the root mean squared error of the NN model on the OOP data
        Error_NN = np.sqrt(mean_squared_error(Y_oop, NN(X_oop)))
        print(f"Iteration: {str(iter)}, Model: NN, OOP Error: {Error_NN}")

        #Query new datapoints
        ids = query_strategy.make_query()
        # Label these datapoints and update the dataset
        dataset.update(ids, Labeler[ids])
        iter += 1

if __name__ == '__main__':
    main(20) #Running for 20 AL-iterations