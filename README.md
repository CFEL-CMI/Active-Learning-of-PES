# ALPES: Stochastic active learning of potential energy surfaces

The repository contains the three active learning (AL) strategies implemented in
[1] to construct the potential energy surface (PES) of pyrrole-water molecules.
The implementation of the AL algorithms is based on the abstract implementation
of the libact package [2]. The HDF5 file "dataset" contains the molecular
geometries and corresponding potential energies used in the simulations as well
as the fixed structures of the pyrrole and water monomers. The repository is not
a complete AL package and is not fully generic. Extension to other molecules is
straightforward. For further details please consult the documentation and the
manuscript [1].

## Dependencies

The codes were tested on Python 3.7-3.8. We recommend the use of a virtual
environment. To install all necessary packages run:

```
pip install -r requirements.txt
```
Install the libact package with the following custom options:
```
LIBACT_BUILD_HINTSVM=1 LIBACT_BUILD_VARIANCE_REDUCTION=0 pip install git+https://github.com/ntucllab/libact.git
```


## Installation

To install the package run:
```
python setup.py install
```
or in a developer-mode, e.g.:
```
python setup.py develop --user
```


## Usage

Pyrrolew.py demonstrates how to use SQBF to minimize the number of datapoints
for constructing the PES of pyrrole-water molecules. To run this, with terminal
open in the main folder use:

```
python examples/pyrrolew.py
```

The other 2 AL strategies can be used the same way. In this example, evaluating
the performance of SQBF is performed by training a model on the so-far-labeled
data for each AL algorithm and computing its root mean squared error (RMSE) on a test dataset. As
models we used the trees' ensemble (RFR) as well as a neural network (NN). Running the script prints the (RMSE) of the RFR and NN models as a function of the AL iteration.
ALPES/nnutils.py provide the necessary tools to build and train the neural
network.


## Documentation

An overview of the AL algorithms and their implementation is provided in the
documentation, which can be generated by running:

```
python setup.py build_sphinx
```

The generated HTML documentation can then be viewed by opening
`./build/sphinx/html/index.html` in a browser. Further details are provided in
the manuscript and references therein.


## References


[1] Y. Saleh, V. Sanjay, A. Iske, A. Yachmenev, and J. Küpper , Active learning of potential-energy surfaces of weakly bound complexes with regression-tree ensembles, [J. Chem. Phys. 155, 144109] ( https://doi.org/10.1063/5.0057051) (2021).

[2] Y.-Y. Yang, S.-C. Lee, Y.-A. Chung, T.-E. Wu, S.-A. Chen, and H.-T. Lin, *libact: Pool-based active learning in Python*, [arXiv:1710.00379 [cs]]( http://arxiv.org/abs/1710.00379) (2017); [Github repository]( https://github.com/ntucllab/libact).



<!-- Put Emacs local variables into HTML comment
Local Variables:
coding: utf-8
fill-column: 80
End:
-->
