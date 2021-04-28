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
This script contains utilities for training a neural network to predict
potential energies given molecular structures.
"""

import tensorflow as tf
import numpy as np

class LearningRateScheduler(tf.keras.callbacks.Callback):
    """Learning rate scheduler.

       Args:
       schedule: a function that takes an epoch index (integer, indexed from 0)
       and current learning rate as inputs and returns a new learning rate as
       output (float).
    """

    def __init__(self, schedule):
        super(LearningRateScheduler, self).__init__()
        self.schedule = schedule

    def on_epoch_begin(self, epoch, logs=None):
        if not hasattr(self.model.optimizer, 'learning_rate'):
            raise ValueError('Optimizer must have a "learning_rate" attribute.')
        # Get the current learning rate from model's optimizer.
        learning_rate = float(tf.keras.backend.get_value(self.model.optimizer.learning_rate))
        # Call schedule function to get the scheduled learning rate.
        scheduled_learning_rate = self.schedule(epoch, learning_rate)
        # Set the value back to the optimizer before this epoch starts
        tf.keras.backend.set_value(self.model.optimizer.learning_rate, scheduled_learning_rate)
        #print('\nEpoch %05d: Learning rate is %6.4f.' % (epoch, scheduled_learning_rate))

def learning_rate_schedule(epoch, learning_rate):
    if epoch < 10:
        return learning_rate
    else:
        return learning_rate * 0.9825

escallbacks = tf.keras.callbacks.EarlyStopping(monitor="val_loss",patience=25,verbose=1)

def MLPmodel():
    model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, activation='relu', input_dim = 30),
    tf.keras.layers.Dense(512, activation='relu',  kernel_regularizer = tf.keras.regularizers.l2(1e-5)),
    tf.keras.layers.Dense(256, activation='relu', kernel_regularizer = tf.keras.regularizers.l2(1e-5)),
    tf.keras.layers.Dense(1)])
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.0025)
    model.compile(optimizer= optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def MLPtrain(model, X, Y, Xv, Yv):
    """A utility to train a NN network.

    Args:

    model: a Keras neural network model to train.
    X: numpy array. Training inputs. Shape: (#training_data, #features)
    Y: numpy array. The output corresponding to X. Shape: (#training_data,)
    Xv: numpy array. Validation inputs. Shape: (#validation_data, #features)
    Yv: numpy array. The output corresponding to Xv. Shape: (#validation_data,)
    """
    X = np.asarray(X)
    Y = np.asarray(Y)
    Xv = np.asarray(Xv)
    Yv = np.asarray(Yv)
    model.fit(X, Y, epochs=250, validation_data = (Xv, Yv), callbacks = [escallbacks, LearningRateScheduler(learning_rate_schedule)], verbose=False)
    return model
