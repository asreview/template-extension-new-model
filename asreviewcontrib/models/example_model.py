__all__ = ["NaiveBayesDefaultParamsModel"]

from sklearn.naive_bayes import MultinomialNB

class NaiveBayesDefaultParamsModel(MultinomialNB):
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters.
    """

    name = "nb_example"
    label = "The Naive Bayes classifier"

    def __init__(self):
        super().__init__()
        self._model = MultinomialNB()

        def fit(self, X, y):
            """Fit the model to the data."""
            return self.fit(X, y)

        def predict_proba(self, X):
            """Get the inclusion probability for each sample."""
            return self.predict_proba(X)
