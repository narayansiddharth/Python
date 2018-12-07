import matplotlib.pyplot as plt
import numpy as np


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(sum(x * y) - n * m_y * m_x)
    SS_xx = np.sum(sum(x * x) - n * m_x * m_x)
    SS_yy = np.sum(sum(y * y) - n * m_y * m_y)
    # print(SS_xy,SS_xx)

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    # calculating r sqaure
    r2 = (b_1 * SS_xy) / SS_yy
    return (b_0, b_1, r2)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    # observations de=driver experience, ip=insurance premium
    de = np.array([5, 2, 12, 9, 15, 6, 25, 16])
    ip = np.array([64, 87, 50, 71, 44, 56, 42, 60])

    # estimating coefficients
    b = estimate_coef(de, ip)
    # print(b)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    print("\nValue of r square is = ", format(b[2]))

    # plotting regression line
    plot_regression_line(de, ip, b)


main()
