.. _AL-theory:

************************************************
Outline of pool-based active learning algorithms
************************************************


In our manuscript and the respective codes we considered pool-based active learning.
Here, one starts by defining a pool of molecular geometries that is assumed to follow
the true distribution of data. Then, a policy algorithm queries the labels of these geometries,
as to minimize the number of required datapoints to construct the potential energy surface.
We considered three different active learning algorithms:

Random sampling
===============

Here, the algorithm uniformly samples geometries from the pool.

Query-by-Committee (QBC) [SOS1992]_
====================================

This algorithm trains an ensemble of :math:`n`-learners using the currently-labelled
data. To query points, these learners are then asked to predict the energies of geometries in the pool.
The energies that correspond to the highest prediction's variances are then queried. As an ensemble of learners
we used the trees of a random forest regressor.

Stochastic Query-by-Forest (SQBF)[B2011]_
==========================================

Similar to QBC, an ensemble of learners is trained on the currently-labelled data and prediction's variances
between the ensemble's members are computed. However, to query data one samples from a probability density function that is constructed
from these variances.

These three algorithms are intended to be used for regression problems in a batch setting. The committee of learners in QBC and SQBF are trees of a sklearn's trees' ensemble (random forest regressor or extremely randomized trees).
An ensemble of any other learners can be used with minor changes to the query strategies.

References
==========
.. [B2011] Borisov, Active batch learning with stochastic query-by-forest (SQBF), Active Learning and Experimental Design workshop In conjunction with AISTATS 2010, pages={59--69}, 2011.
.. [SOS1992] H. S. Seung, et al., “Query by committee,” in Proceedings of the fifth annual workshop on Computational learning theory (1992) pp. 287–294.
