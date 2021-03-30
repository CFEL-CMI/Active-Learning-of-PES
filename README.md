Repository will be updated over the next days.
# Stochastic active learning of potential energy surfaces

The repository contains the three active learning (AL) strategies implemented in [1] to construct the potential energy surface (PES) of pyrrole-water molecules. The implementation of the AL algorithms is based on the abstract implementation of the libact package [2]. The HDF5 file "dataset" contains the molecular geometries and corresponding potential energies used in the simulations as well as the fixed structures of the pyrrole and water monomers. The repository is not a complete AL package and is not fully generic.

## Prerequisites
The codes require an installation of Python, Tensorflow (>2.0), scikit-learn and libact.

## AL algorithms

The AL algorithms we implemented are:
- Query By Committee (QBC)
- Stochastic Query By Forest (SQBF)
- Random Sampling

These three algorithms are intended to be used for regression problems in a batch setting. The committee of learners in QBC
and SQBF are trees of a sklearn's trees' ensemble (random forest regressor or extremely randomized trees). An ensemble of any other learners can be used with minor changes to the query strategies.

## Usage

AL_PES.py demonstrates how to use SQBF to minimize the number of datapoints for constructing the PES of pyrrole-water molecules. The other 2 AL strategies can be used the same way. To evaluate the performance of an AL algorithm, one can train a model on the so-far-labeled data for each algorithm and compute its accuracy on a test dataset. This is demonstrated in AL_PES.py where we use the trees' ensemble as well as a neural network to evaluate the performance. Building and training the neural network is performed in nnutils.py.  

## References

[1] Active learning of potential-energy surfaces of weakly-bound complexes
with regression-tree ensembles,
Y.Saleh, V. Sanjay, A. Iske, A.Yachmenev, J. Küpper.

[2] libact: Pool-based Active Learning in Python, Y.Y. Yang et al.,
https://github.com/ntucllab/libact.
