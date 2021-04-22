
# Stochastic active learning of potential energy surfaces

The repository contains the three active learning (AL) strategies implemented in [1] to construct the potential energy surface (PES) of pyrrole-water molecules. The implementation of the AL algorithms is based on the abstract implementation of the libact package [2]. The HDF5 file "dataset" contains the molecular geometries and corresponding potential energies used in the simulations as well as the fixed structures of the pyrrole and water monomers. The repository is not a complete AL package and is not fully generic. Extension to other molecules is straightforward. For further details please consult the documentation and the manuscript [1].

## Dependencies
The codes require an installation of Python(3.7.3). To install all necessary packages run:
```
pip install -r requirements.txt
```
Install the libact package with the following custom options:
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

## Usage

Pyrrolew.py demonstrates how to use SQBF to minimize the number of datapoints for constructing the PES of pyrrole-water molecules. To run this, with terminal open in the main folder use:
```
python examples/pyrrolew.py
```
The other 2 AL strategies can be used the same way. To evaluate the performance of an AL algorithm, one can train a model on the so-far-labeled data for each algorithm and compute its accuracy on a test dataset. This is demonstrated in AL_PES.py where we use the trees' ensemble as well as a neural network to evaluate the performance. Building and training the neural network is performed in nnutils.py.  
## Documentation

An overview of the AL algorithms and their implementation is provided in the documentation, which can be generated by running:
```
python setup.py build_sphinx
```
The generated HTML documentation can then be viewed by opening `./build/sphinx/html/index.html` in a browser. Further details are provided in the manuscript and references therein.
## References

[1] Saleh Y., Sanjay V., Iske A., Yachmenev A., and Küpper J., ‘Active Learning of Potential-Energy Surfaces of Weakly-Bound Complexes with Regression-Tree Ensembles’. [ArXiv:2104.00708]( http://arxiv.org/abs/2104.00708) [Physics], Apr. 2021.

[2] Yang Z., et al. ‘Libact: Pool-Based Active Learning in Python’. [ArXiv:1710.00379](http://arxiv.org/abs/1710.00379) [Cs], Oct. 2017, [Github repository](https://github.com/ntucllab/libact).
