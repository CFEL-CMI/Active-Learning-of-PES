.. _implementation-details:

********************************************
Implementation of active learning algorithms
********************************************

The implementation of the active learning algorithms is based on the abstract codes of libact package.
Please consult its git repository and the corresponding paper for more details.
Here we give an example of how to use it.

Starting from a dataset :math:`(X,Y)` as numpy arrays one can define a dataset object::

    from libact.base.dataset import Dataset
    dataset = Dataset(X=X, y=Y)

Using this class from libact allows for effortless update of the labelled and unlabelled examples.

We define an SQBF-object that takes as an input an sklearn-ensemble of trees, required batchsize and the
dataset::

    from AL_PESs.query_strategies.stochastic_query_by_forest import SQBF
    query_strategy = SQBF(Trees=Trees, BatchSize=BatchSize, dataset=dataset)

To do one AL iteration, one can use the "make_query" method::

    ids = query_strategy.make_query()

Then a labeller is used to compute the respective potential energies of this geometry and
the dataset is updated accordingly::


    dataset.update(ids, Labeler[ids])
