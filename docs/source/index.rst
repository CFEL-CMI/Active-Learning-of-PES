Welcome to ALPES' documentation!
========================================================

This repository contains the main codes that were developed to perform the simulations in [SSIYK2021]_. In particular, the
repository contains three pool-based active learning (AL) algorithms used to minimize the number of required datapoints to construct
the potential energy surfaces of pyrrole-water molecules. The AL algorithms are: uniform random sampling, query by committee (QBC) [SOS1992]_,
and a regression version of stochastic query by forest (SQBF) [B2011]_. All the algorithms were written based on the
abstract implementation of the Libact python package [YSYTSH2017]_. For a quick overview on AL theory and implementation please refer to :ref:`AL-theory`
and :ref:`implementation-details`, respectively. Further details are provided in the manuscript.

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
.. [SSIYK2021] Y. Saleh, V. Sanjay, A. Iske, A. Yachmenev, J. Küpper, *Active
               Learning of Potential-Energy Surfaces of Weakly-Bound Complexes
               with Regression-Tree Ensembles*, `arxiv:2104.00708 [physics]
               <http://arxiv.org/abs/2104.00708>`_ (2021).
.. [YSYTSH2017] Y.-Y. Yang, S.-C. Lee, Y.-A. Chung, T.-E. Wu, S.-A. Chen, H.-T.
                Lin, *Libact: Pool-Based Active Learning in Python*,
                `arxiv:1710.00379 [cs] <http://arxiv.org/abs/1710.00379>`_
                (2017); `Github repository
                <https://github.com/ntucllab/libact>`_.
.. [B2011] A. Borisov, E. Tuv, G. Runger, *Active batch learning with stochastic
           query-by-forest (SQBF)*, Active Learning and Experimental Design
           workshop in conjunction with AISTATS 2010, 59--69 (2011).
.. [SOS1992] H. S. Seung, M. Opper, H. Sompolinsky, *Query by committee*, in
             Proceedings of the fifth annual workshop on Computational learning
             theory (1992) pp. 287–294.
