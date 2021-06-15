import numpy as np
import random
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [6,3,9,10,13,12,15,14,17,16,19,15,14,20,24,26,28,29,30,34]
regY = []
m = len(x)

#for i in range(20):
#    x.append(random.randint(1,100))
#    y.append(random.randint(1,100))

#p1 = np.polyfit(x, y, 1)
#print(p1)
#plt.plot(x, y, "x")
#plt.plot(x, np.polyval(p1, x))
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

sxx = 0
for i in range(m):
    sxx = (x[i]-np.mean(x))**2 + sxx
syy = 0
for i in range(m):
    syy = (y[i]-np.mean(y))**2 + syy
sxy = 0
for i in range(m):
    sxy = (x[i] - np.mean(x))*(y[i]-np.mean(y)) + sxy

r = sxy/((sxx*syy)**0.5)
b = sxy/sxx
a = np.mean(y) - b*np.mean(x)

for i in range(m):
    regY.append(a+b*x[i])

plt.plot(x,y,"x")
plt.plot(x,regY)
plt.xlabel("x")
plt.ylabel("y")
plt.text(1,37, "r = ")
plt.text(2,37, r)

plt.text(10,37,"y = ")
plt.text(11,37,"%.3f" % a)
plt.text(12.1,37," +")
plt.text(12.7,37,"%.3f" % b)
plt.text(13.8,37," x ")
plt.show()
