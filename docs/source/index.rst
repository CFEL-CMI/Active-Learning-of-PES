Welcome to CMI Active Learning for PESs's documentation!
========================================================

This repository contains the main codes that were developed to perform the simulations in [SSIYK2021]_. In particular, the
repository contains three pool-based active learning (AL) algorithms used to minimize the number of required datapoints to construct
the potential energy surfaces of pyrrole-water molecules. The AL algorithms are: uniform random sampling, Query-by-Committee (QBC) [SOS1992]_,
and a regression version of Stochastic Query by Forest (SQBF) [B2011]_. All the algorithms were written based on the
abstract implementation of the Libact python package [YSYTSH2017]_. For a quick overview on AL theory and implementation please refer to :ref:`AL-theory`
and :ref:`implementation-details`, respectively. Further details are provided in the manuscript [SSIYK2021]_.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   AL_TH/TH
   Implementation/imp_details
   modules/scripts

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

References
==========
.. [SSIYK2021] Saleh Y., Sanjay V., Iske A., Yachmenev A. Küpper J., ‘Active Learning of Potential-Energy Surfaces of Weakly-Bound Complexes with Regression-Tree Ensembles’. ArXiv:2104.00708 [Physics], Apr. 2021. `arXiv <http://arxiv.org/abs/2104.00708>`_.
.. [YSYTSH2017] Yang Z., et al. ‘Libact: Pool-Based Active Learning in Python’. ArXiv:1710.00379 [Cs], Oct. 2017. `arXiv <http://arxiv.org/abs/1710.00379>`_, `Github repository <https://github.com/ntucllab/libact>`_.
.. [B2011] Borisov, Active batch learning with stochastic query-by-forest (SQBF), Active Learning and Experimental Design workshop In conjunction with AISTATS 2010, pages={59--69}, 2011.
.. [SOS1992] H. S. Seung, M. Opper, and H. Sompolinsky, “Query by committee,” in Proceedings of the fifth annual workshop on Computational learning theory (1992) pp. 287–294.
