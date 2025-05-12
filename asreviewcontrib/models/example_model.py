__all__ = ["NaiveBayesDefaultParamsModel"]

from sklearn.naive_bayes import MultinomialNB

class NaiveBayesDefaultParamsModel:
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters.
    """

    name = "nb_example"
    label = "The Naive Bayes classifier"

    def __init__(self):
        super().__init__()
        self._model = MultinomialNB()

    def fit(self, X, y, sample_weight=None):
        """Fit the model to the data."""
        return self._model.fit(X, y, sample_weight=sample_weight)

    def predict_proba(self, X):
        """Get the inclusion probability for each sample."""
        return self._model.predict_proba(X)
