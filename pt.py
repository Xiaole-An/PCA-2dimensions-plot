import matplotlib.pyplot as plt


class Plt:
    def __init__(self, dat, new_axis):
        """

        :param dat: two dimension data
        """
        self.ax = []
        self.xy = dat
        self.ax.append(new_axis[0][0])
        self.ax.append(new_axis[1][0])
        self.x_mean = 0
        self.y_mean = 0
        for x, y in self.xy:
            self.x_mean += x
            self.y_mean += y
        self.x_mean /= len(self.xy)
        self.y_mean /= len(self.xy)

    def plot_src(self):
        for x, y in self.xy:
            plt.scatter(x, y)

    def plot_transform(self):
        point_line = [[self.x_mean, self.y_mean], [self.x_mean + self.ax[0], self.y_mean + self.ax[1]]]
        axis = [point_line[0], point_line[1]]
        plt.axline(axis[0], axis[1])
        a = point_line[1][1] - point_line[0][1]
        b = point_line[0][0] - point_line[1][0]
        c = point_line[1][0] * point_line[0][1] - point_line[0][0] * point_line[1][1]
        s = - a**2 - b**2
        for x, y in self.xy:
            x1 = (b*(-b*x + a*y) + a*c) / s
            y1 = (b*c - a*(-b*x + a*y)) / s
            plt.scatter(x1, y1)

    def plot(self):
        self.plot_src()
        self.plot_transform()
        plt.show()
