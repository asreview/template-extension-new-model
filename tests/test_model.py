import pandas as pd
from pathlib import Path

import asreview as asr
from asreview.models.queriers import Max
from asreview.models.feature_extractors import Tfidf
from asreviewcontrib.models.example_model import NaiveBayesDefaultParamsModel

def test_single_nb_example():
    # Load dataset
    dataset_path = Path("tests/data/generic_labels.csv")
    data = asr.load_dataset(dataset_path)

    alc = asr.ActiveLearningCycle(
        classifier=NaiveBayesDefaultParamsModel(),
        feature_extractor=Tfidf(),
        balancer=None,
        querier=Max(),
    )

    # Run simulation
    simulate = asr.Simulate(
        X=data,
        labels=data["included"],
        cycles=[alc],
    )
    simulate.label([0, 1])
    simulate.review()

    # Simple checks
    assert isinstance(simulate._results, pd.DataFrame)
    assert simulate._results.shape[0] > 2 and simulate._results.shape[0] <= 6
    assert "nb_example" in simulate._results["classifier"].unique()
