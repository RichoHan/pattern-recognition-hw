import numpy as np
from scipy import stats


class LMS(object):
    """
    A classifier using Least Mean Square algorithm
    """
    def __init__(self, eta=0.1, iterations=100):
        super(LMS, self).__init__()
        self.eta = eta
        self.iterations = iterations

    def fit(self, data, target):
        self.data = data
        self.target = target
        X = data
        Y = target
        dim = X.shape[1]
        num_points = X.shape[0]
        w = np.ones(dim)

        for i in range(self.iterations):
            next = np.random.randint(num_points)
            predict = np.dot(X[next], w)
            error = Y[next] - predict
            w = w + self.eta*error*X[next]
        self.coef_ = w
        self.direction(data, target)

    def direction(self, data, target):
        self.up, self.down = 1, 2
        pred = self.predict(data)
        if float((target != pred).sum())/float(target.shape[0]) > 0.5:
            self.up, self.down = self.down, self.up

    def predict(self, data):
        # target = np.array([])
        # foo = lambda x: (
        #     # np.dot(x, self.coef_)
        #     x[0]*self.coef_[0] + self.coef_[1]
        # )
        # for x in data:
        #     target = np.concatenate((target, np.array([foo(x)])))
        x, y = data.T
        polynomial = np.poly1d(self.coef_)
        target = polynomial(x)
        return target

    def score(self, data, target):
        pred = self.predict(data)
        slope, intercept, r_value, p_value, std_err =\
            stats.linregress(pred, target)
        return abs(r_value)
