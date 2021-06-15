import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = list(range(0,11))
y = [10]*11

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom = 0.35)
p, = plt.plot(x,y, linewidth=2, color = 'blue')
plt.axis([0,10,0,100])

axSlider2 = plt.axes([0.1,0.1,0.8,0.05])
slider2 = Slider(ax = axSlider2,label = "Slider 2",valmin=0,valmax=100,valinit=30)

def val_update(val):
    yval = slider2.val
    p.set_ydata(yval)
    plt.draw()
slider2.on_changed(val_update)

plt.show()

#slider1 = plt.axes([0.1, 0.93, 0.3, 0.05])
#slider = Slider(slider1, "r", valmin=0, valmax=4, valinit=3.35, closedmax=True)


#def val_update(val):
  #  global r
  #  rval = slider.val
  #  l.set_ydata(rval)
  #  plt.draw()


#slider.on_changed(val_update)


import keyboard  # using module keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop wi