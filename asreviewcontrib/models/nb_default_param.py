from sklearn.naive_bayes import MultinomialNB

from asreview.models.classifiers.base import BaseTrainClassifier


class NaiveBayesDefaultParamsModel(BaseTrainClassifier):
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters.
    """

    name = "nb_example"

    def __init__(self):

        super().__init__()
        self._model = MultinomialNB()

        def fit(self, X, y):
            """Fit the model to the data."""
            return self._model.fit(X, y)

        def predict_proba(self, X):
            """Get the inclusion probability for each sample."""
            return self._model.predict_proba(X)
