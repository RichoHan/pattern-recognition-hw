import numpy as np
from scipy import stats


class LMS(object):
    """
    A classifier using Least Mean Square algorithm
    """
    def __init__(self, eta=0.1, iterations=1000):
        super(LMS, self).__init__()
        self.eta = eta
        self.iterations = iterations

    def fit(self, data, target):
        """
        Fit the model with the input data
        """
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

    def predict(self, data):
        """
        Return the prediction result of the data
        """
        x, y = data.T
        polynomial = np.poly1d(self.coef_)
        target = polynomial(x)
        return target

    def score(self, data, target):
        """
        Return the coefficient of determination of the prediction result
        """
        pred = self.predict(data)
        slope, intercept, r_value, p_value, std_err =\
            stats.linregress(pred, target)
        return r_value**2
