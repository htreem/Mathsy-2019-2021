import matplotlib.pyplot as plt
import numpy as np

r = 4
newX = []
newXreordered = []
iter = []

def mie50(x):
    newallvalueX = []
    for i in range(50):
        newallvalueX.append(x)
        x = r * x * (1 - x)
    return newallvalueX


x = np.linspace(0, 1, 100)

for i in range(50):
    newX.append(mie50(x[i]))


for i in range(50):
    for j in range(50):
        iter.append(i)
for j in range(50):
    for i in range(50):
        newXreordered.append(newX[i][j])

X = np.array(iter)
Y = np.array(newXreordered)
plt.scatter(X, Y, color="#CC6633", s=1)
plt.xlabel("Iteration")
plt.ylabel("X")
plt.title("r = %1.2f" % r)
plt.show()