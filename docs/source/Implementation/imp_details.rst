.. _implementation-details:

********************************************
Implementation of active learning algorithms
********************************************

Here we give a minimal example on how to use the Stochastic Query by Forest algorithm.

Starting from a dataset :math:`(X,Y)` as numpy arrays one can define a dataset object::

    from libact.base.dataset import Dataset
    dataset = Dataset(X=X, y=Y)

Using this class from libact allows for an effortless update of the labelled and unlabelled examples during the
active learning iterations.

We define an SQBF-object that takes as an input an sklearn-ensemble of trees, required batchsize and the
dataset::

    from ALPES.stochastic_query_by_forest import SQBF
    from sklearn.ensemble import RandomForestRegressor as RFR
    Trees = RFR(n_estimators=100)
    query_strategy = SQBF(Trees=Trees, BatchSize=512, dataset=dataset)

To do one AL iteration, one can use the "make_query" method::

    ids = query_strategy.make_query()

Then a labeller is used to compute the respective potential energies of this geometry and
the dataset is updated accordingly::


    dataset.update(ids, Labeler[ids])

For further details on the implementation consult the python libact package.
