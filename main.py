import numpy as np
from pt import Plt
import random


class Solution:
    def __init__(self, dataset, low_dimensional_space):
        self.da = np.array(dataset)
        self.d = low_dimensional_space
        self.std = self.normalization()

    def normalization(self):
        return (self.da - np.mean(self.da, axis=0)) / np.std(self.da, axis=0)   # 每一个特征进行去均值化

    def covariance_m(self):
        return np.cov(self.std.T)

    def eigen(self):
        eigen_values, eigen_vectors = np.linalg.eig(self.covariance_m())
        return eigen_values, eigen_vectors

    def select(self):
        eigen_values, eigen_vectors = self.eigen()
        idx = np.argsort(eigen_values)[::-1][:self.d]
        components = eigen_vectors[:, idx]
        return components

    def transform(self):
        x = np.dot(self.std, self.select())
        print('raw data is \n %s,\n low dimensional space is %d,\n new data is \n %s' % (self.da, self.d, x))
        return x


def random_list(n, x_scope, y_scope):
    lst_x = []
    lst_y = []
    for j in range(n):
        lst_x.append(random.uniform(x_scope[0], x_scope[1]))
        lst_y.append(random.uniform(y_scope[0], y_scope[1]))
    list_random = list(zip(lst_x, lst_y))
    return list_random


if __name__ == '__main__':
    low_d = 1
    scope = [[[0, 2], [8, 9]], [[3, 5], [1, 2]]]
    a = random_list(30, scope[0][0], scope[0][1])
    b = random_list(30, scope[1][0], scope[1][1])
    data = a + b
    PCA = Solution(data, low_d)
    PCA.transform()
    plt = Plt(data, PCA.select())
    plt.plot()
