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


class NaiveBayesDefaultParamsModelAlternative(MultinomialNB):
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters. Note how
    this class extends the MultinomialNB class from SKLearn. Since this class
    already has the fit and predict_proba methods, we can simply use it as is.
    This is a good example of how to create a model that is a wrapper around an
    existing SKLearn model. This is useful if you want to create a model that
    has the same interface as the other models in ASReview, but you want to use
    an existing SKLearn model.
    """

    name = "nb_example_alternative"
    label = "The alternative implementation of the Naive Bayes classifier"
