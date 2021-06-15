from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import scipy.integrate
import numpy as np



# limits

avg = float(input("What is the mean? "))
stdev = float(input("What is the standard deviation? "))
ulc = float(input("What is the upper limit of your range? "))
llc = float(input("What is your lower limit of your range? "))
ul = (ulc - avg) / stdev
ll = (llc - avg) / stdev



# finding the probability


def f(x):
    e = 2.718281828459
    pi = 3.14159265
    c = 1 / (stdev * ((2 * pi) ** 0.5))
    exponent = -(((x - avg) ** 2) / (2 * (stdev ** 2)))
    standard_normal_curve = c * (e ** exponent)
    return standard_normal_curve



probability, error = scipy.integrate.quad(f, llc, ulc)
print(round(probability, 5))
g = str(round(probability, 5))


# plot
x = []
y = []
e = 2.718281828459
pi = 3.14159265

c = 1/(stdev*((2*pi)**0.5))

i = avg-4*stdev
while i < avg+4*stdev:
    i = i + stdev/100
    x.append(i)

for a in x:
    expo = -(((a-avg) ** 2) / (2*(stdev**2)))
    dis = c * (e ** expo)
    y.append(dis)

a, b = llc, ulc
xx = np.linspace(avg-4*stdev,avg+4*stdev )
yy = f(xx)
fig, ax = plt.subplots()
ax.set_ylim(bottom=0)
ix = np.linspace(a, b)
iy = f(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.5', edgecolor='0.7')
ax.add_patch(poly)

plt.plot(x, y)
plt.title("Normal Distribution")
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
