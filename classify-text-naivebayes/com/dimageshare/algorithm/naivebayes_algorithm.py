from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from com.dimageshare.transformer.world_transformer import WorldTransformer


class NaiveBayesAlgorithm(object):

    def __init__(self):
        self.init = self.init_pipeline()

    def init_pipeline(self):
        pipe_line = Pipeline([("transformer", WorldTransformer()),
                              ("vect", CountVectorizer()),
                              ("tfidf", TfidfTransformer()),
                              ("clf", MultinomialNB())])

        return pipe_line
