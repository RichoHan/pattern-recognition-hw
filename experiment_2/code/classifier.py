from sklearn.linear_model import Perceptron, LinearRegression
from lms import LMS


class classifier(object):
    """
    The class containing all three kind of classifiers.
    """
    def __init__(self, method, data, target):
        super(classifier, self).__init__()
        self.method = method
        self.data = data
        self.target = target
        if self.method == "perceptron":
            self.clf = Perceptron(n_iter=30, shuffle=False)
            self.clf.fit(self.data, self.target)
        elif self.method == "linear_model":
            self.clf = LinearRegression()
            self.clf.fit(self.data, self.target)
        elif self.method == "lms":
            self.clf = LMS()
            self.clf.fit(self.data, self.target)

    def coef(self):
        if self.method == "perceptron":
            return self.clf.coef_
        elif self.method == "linear_model":
            return self.clf.coef_
        elif self.method == "lms":
            return self.clf.coef_
        else:
            return "Non-classifier"

    def predict(self):
        if self.method == "perceptron":
            return self.clf.predict(self.data)
        elif self.method == "linear_model":
            return [int(round(i)) for i in self.clf.predict(self.data)]
        elif self.method == "lms":
            return self.clf.predict(self.data)
        else:
            return "Non-classifier"

    def score(self):
        return self.clf.score(self.data, self.target)
