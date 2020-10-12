from sklearn.naive_bayes import MultinomialNB

from asreview.models.base import BaseTrainModel


class NaiveBayesDefaultParamsModel(BaseTrainModel):
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters.
    """

    name = "nb_example"

    def __init__(self):

        super(NaiveBayesDefaultParamsModel, self).__init__()
        self._model = MultinomialNB()
