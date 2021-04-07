Repository will be updated over the next days.
# Stochastic active learning of potential energy surfaces

The repository contains the three active learning (AL) strategies implemented in [1] to construct the potential energy surface (PES) of pyrrole-water molecules. The implementation of the AL algorithms is based on the abstract implementation of the libact package [2]. The HDF5 file "dataset" contains the molecular geometries and corresponding potential energies used in the simulations as well as the fixed structures of the pyrrole and water monomers. The repository is not a complete AL package and is not fully generic. For further details please consult the documentation and the manuscript [1].

## Dependencies
The codes require an installation of Python(3.7.3), Tensorflow (>=2.2), scikit-learn  and libact.
```
pip3 install -r requirements.txt
```
Since lapack and openblas packages have a functions with the same name, directly installing libact was not possible. A fix is to let go of the variance reduction algorithm in libact:
```
LIBACT_BUILD_HINTSVM=1  LIBACT_BUILD_VARIANCE_REDUCTION=0 pip install git+https://github.com/ntucllab/libact.git
```

## Installation

To install the package run:
```
python setup.py install
```
or in a developer-mode:
```
python setup.py develop
```

## AL algorithms

The AL algorithms we implemented are:
- Query By Committee (QBC)
- Stochastic Query By Forest (SQBF)
- Random Sampling

These three algorithms are intended to be used for regression problems in a batch setting. The committee of learners in QBC
and SQBF are trees of a sklearn's trees' ensemble (random forest regressor or extremely randomized trees). An ensemble of any other learners can be used with minor changes to the query strategies.

## Usage

Pyrrolew.py demonstrates how to use SQBF to minimize the number of datapoints for constructing the PES of pyrrole-water molecules. To run this, with terminal open in the main folder use:
```
python examples/pyrrolew.py
```
The other 2 AL strategies can be used the same way. To evaluate the performance of an AL algorithm, one can train a model on the so-far-labeled data for each algorithm and compute its accuracy on a test dataset. This is demonstrated in AL_PES.py where we use the trees' ensemble as well as a neural network to evaluate the performance. Building and training the neural network is performed in nnutils.py.  

## References

[1] Saleh Y., Sanjay V., Iske A., Yachmenev A. Küpper J., ‘Active Learning of Potential-Energy Surfaces of Weakly-Bound Complexes with Regression-Tree Ensembles’. ArXiv:2104.00708 [Physics], Apr. 2021. arXiv.org, http://arxiv.org/abs/2104.00708.

[2] Yang Z., et al. ‘Libact: Pool-Based Active Learning in Python’. ArXiv:1710.00379 [Cs], Oct. 2017. arXiv.org, http://arxiv.org/abs/1710.00379, Github repository, https://github.com/ntucllab/libact.
