from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from scipy.stats import norm
import scipy.integrate
import numpy as np
from tkinter import *


dc = input("1 for z values, 2 for custom")

# limits
if dc == '2':
    import placeholderND
else:

    ul = float(input("What is your upper Z-value? "))
    ll = float(input("What is your lower Z-value? "))


    # finding the probability
    def f(x):
        e = 2.718281828459
        pi = 3.14159265
        c = 1 / ((2 * pi) ** 0.5)
        exponent = (-x ** 2) / 2
        standard_normal_curve = c * (e ** exponent)
        return standard_normal_curve


    probability, error = scipy.integrate.quad(f, ll, ul)
    print(round(probability, 5))
    g = str(round(probability, 5))

    # plot
    x = []
    y = []
    e = 2.718281828459
    pi = 3.14159265
    c = 1 / ((2 * pi) ** 0.5)

    i = -4
    while i < 4:
        i = i + 0.01
        x.append(i)

    for a in x:
        expo = (-a ** 2) / 2
        dis = c * (e ** expo)
        y.append(dis)

    a, b = ll, ul
    xx = np.linspace(0, 10)
    yy = f(xx)
    fig, ax = plt.subplots()
    ax.set_ylim(bottom=0)
    ix = np.linspace(a, b)
    iy = f(ix)
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.5', edgecolor='0.7')
    ax.add_patch(poly)

    plt.plot(x, y)
    plt.title("Standard Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Density")
    ax.text(0.95, 0.92, g,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=10)
    ax.text(0.8, 0.92, "Normal Cummulative Distribution: ",
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=10)
    plt.show()

# plt.plot(domain, norm.pdf(domain,mean,std),label='$\mathcal{N}$' + f'$(\mu \\approx {round(mean)}, \sigma \\approx {round(std)})$')

# domain = np.linspace(avg - 5 * stdev, avg + 5 * stdev, 1000)
# plt.plot(domain, norm.pdf(domain, avg, stdev))
# plt.title("Normal Distribution")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.show()
