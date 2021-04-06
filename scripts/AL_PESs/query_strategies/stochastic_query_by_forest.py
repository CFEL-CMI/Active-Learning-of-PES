#!/usr/bin/env python3
# -*- coding: utf-8; fill-column: 100; truncate-lines: t -*-
#
# This file is part of Active-Learning-of-PES python package
#
# Copyright (C) 2018,2020 CFEL Controlled Molecule Imaging group
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# If you use this program for scientific work, you should correctly reference it; see the LICENSE.md file for details.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

"""
An implementation of stochastic query by committee (QBC) algorithm for regression problems in a batch setting. The members of the
committee are regression trees. The disagreement criterion between the trees is the standard deviation from their mean prediction.
Data to query are chosen by a random samplin procedure that gives higher weights for data points corresponding to uncertainties in their
predictions.
See:
[1] Borisov, Active batch learning with stochastic query-by-forest (SQBF), Active Learning and Experimental Design workshop In conjunction with AISTATS 2010,
  pages={59--69}, 2011.
"""

import numpy as np
from libact.base.dataset import Dataset
from libact.base.interfaces import QueryStrategy

class SQBF(QueryStrategy):
    """SQBF query strategy object
    Args:
    BatchSize: int. The number of elements to query in a single AL iteration.
    Trees: an ensemble of trees sklearn instance composed of n trees.
    dataset: an object containing the labeled and unlabeled data.

    Attribs:
    make_query: choose n=BatchSize data points to query from the pool.
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.BatchSize = kwargs.pop('BatchSize', 1)
        self.Trees = kwargs.pop('Trees', None)
        if self.Trees is None:
            raise TypeError(
                "__init__() missing required keyword-only argument: 'Trees'"
            )

    def _stochastic_standard_deviation(self, predictions):
        def Utility(Q):
            L = np.zeros((np.shape(Q)))
            q0 = np.amin(Q)
            qm = np.amax(Q)
            L = (Q-q0)/(qm-q0)
            Weights = L/np.sum(L)
            return Weights
        # compute the standard deviation of predictions for every unlabeled datapoint
        std_dev = np.std(predictions, axis=0)
        # Constract a probability density function out of the standard deviation
        weights = Utility(std_dev)

        return weights

    def make_query(self):
        # get the unlabeled entries, i.e. the pool data
        unlabeled_entry_ids, X_pool = self.dataset.get_unlabeled_entries()
        if len(unlabeled_entry_ids)>self.BatchSize:
            # Predict the energies of the unlabeled data
            predictions = np.array([estimator.predict(X_pool) for estimator in self.Trees.estimators_])
            # Construct a probability denstiy function
            weights = self._stochastic_standard_deviation(predictions)
            try:
                ask_idx = np.random.choice(np.shape(X_pool)[0], size=self.BatchSize, replace=False, p=weights)
            except:
                #Fewer non-zero entries in p than batch size. Take the samples with highest uncertainties
                print("Size of nonzero elements in p are less than batch size")
                stddev = np.std(predictions, axis=0)
                ask_idx = np.flip(np.argsort(stddev))[0:self.BatchSize]
        else:
            #The number of remaining unlabeled data is less than batch size, query the remaining data
            ask_idx = np.arange(len(unlabeled_entry_ids))

        return unlabeled_entry_ids[ask_idx]

    def _name(self):
        return "SQBF"
