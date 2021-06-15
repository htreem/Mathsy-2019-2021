import matplotlib.pyplot as plt
import keyboard
from numpy import linspace
import time

r = 3.35
x0 = 0.3
running = True


def cobweb(f, x0):
    ax.cla()
    t = linspace(0, 1, 100)
    plt.plot(t, f(t))
    plt.plot(t, t)

    x, y = x0, f(x0)
    for _ in range(100):
        fy = f(y)
        plt.plot([x, y], [y, y], 'b', linewidth=1)
        plt.plot([y, y], [y, fy], 'b', linewidth=1)
        x, y = y, fy

    plt.xlabel("X n")
    plt.ylabel("X n+1")
    plt.title("r = %1.2f" % r)
    fig.canvas.draw()
    time.sleep(0.01)


plt.ion()
fig, ax = plt.subplots()

while running:
    if keyboard.is_pressed('up'):
        r += 0.1
    if keyboard.is_pressed('down'):
        r -= 0.1
    cobweb(lambda x: r * x * (1 - x), x0)
