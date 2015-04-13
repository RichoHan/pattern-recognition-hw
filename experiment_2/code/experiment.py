import numpy as np
import classifier
import random
import csv
import matplotlib.pyplot as plt


def data_generate(means, covs, N, num_of_groups):
    """
    The method generate data set based on the input means & covariance matrice.
    N: Size of the dataset
    num_of_groups: Number of groups
    """
    r = lambda m: (
        np.random.multivariate_normal(means[m], covs[m], 1), np.array([m+1])
    )
    data, target = r(
        random.randint(0, num_of_groups)
    )
    for i in range(0, N-1):
        x, group = r(
            random.randint(0, num_of_groups)
        )
        data = np.concatenate((data, x))
        target = np.concatenate((target, group))
    return data, target


def showPlot(data, target, coef):
    """
    The method plot the data in 2-D window
    """
    data_1 = np.array([d[0] for d in zip(data, target) if d[1] == 1])
    data_2 = np.array([d[0] for d in zip(data, target) if d[1] == 2])
    x, y_1 = data_1.T
    x_2, y_2 = data_2.T
    polynomial = np.poly1d(coef)
    plt.clf()
    plt.plot(x, y_1, 'gx')
    plt.plot(x_2, y_2, 'rx')
    xx = range(-10, 10)
    ys = polynomial(xx)
    plt.plot(xx, ys)
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()


def export(problem, classifier, score):
    with open('result.csv', 'a') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow([problem, classifier, score])


if __name__ == "__main__":
    """
    Main function, first create means & covariance matrice
    Then run the experiment turn by turn
    """
    experiment_time = 100
    np.random.seed(0)

    means = (
        ((-5, 0), (5, 0)),
        ((-2, 0), (2, 0)),
        ((-1, 0), (1, 0))
    )
    C = (
        [[1, 0], [0, 1]],
        [[1, 0], [0, 1]]
    )

    for i, m in zip(range(0, 3), means):

        X, target = data_generate(m, C, 200, 1)

        print "For problem 3.%i:" % (i+1)
        perceptron = classifier.classifier("perceptron", X, target)
        print "\tScore for Perceptron: \t\t%f" % perceptron.score()
        showPlot(X, target, perceptron.coef()[0])

        linear_model = classifier.classifier("linear_model", X, target)
        print "\tScore for Linear Regression: \t%f" % linear_model.score()
        showPlot(X, target, linear_model.coef())

        lms = classifier.classifier("lms", X, target)
        print "\tScore for LMS algorithm: \t%f" % lms.score()
        showPlot(X, target, lms.coef())
