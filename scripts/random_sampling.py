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
An implementation of a random sampling (RS) query strategy for regression problems in a batch setting.
"""

from libact.base.interfaces import QueryStrategy
import numpy as np

class RandomSampling(QueryStrategy):
    """RS query strategy object
    Args:
    BatchSize: int. The number of elements to query in a single AL iteration.
    dataset: an object containing the labeled and unlabeled data.

    Attribs:
    make_query: chooses n=BatchSize data points to query from the pool.
    """

    def __init__(self, dataset, **kwargs):

        super(RandomSampling, self).__init__(dataset, **kwargs)
        self.BatchSize = kwargs.pop('BatchSize', 1)

    def make_query(self):
        # get the unlabeled entries, i.e. the pool data
        unlabeled_entry_ids, X_pool = self.dataset.get_unlabeled_entries()
        if len(unlabeled_entry_ids)>self.BatchSize:
            ask_idx = np.random.choice(np.shape(X_pool)[0], size=self.BatchSize, replace=False)
        else:
            #The number of remaining unlabeled data is less than batch size, query the remaining data
            ask_idx = np.arange(len(unlabeled_entry_ids))
        return unlabeled_entry_ids[ask_idx]

    def _name(self):
        return "RS"
