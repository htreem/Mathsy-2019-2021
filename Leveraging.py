#Return on asset

import matplotlib.pyplot as plt

investmentReturnPerc = 0.1
it = investmentReturnPerc*300
interestRate = 0
amInvested = 100
amBorrowed = 100
y1 = []
y2 = []
x = []
RnoD = amInvested * investmentReturnPerc
for i in range(int(it)):
    x.append(interestRate)
    y1.append(RnoD)
    RD = ((amInvested + amBorrowed) * investmentReturnPerc) - (amBorrowed * interestRate)
    y2.append(RD)
    interestRate += 0.01

plt.plot(x,y1,label = 'nolev')
plt.plot(x,y2,label = 'lev')
plt.xlabel('interestRate')
plt.ylabel("Return")
plt.title("Leveraging")
plt.legend()
plt.show()

#print("Amount invested: ", amInvested)
#print("Return w/out leveraging debt: ", RnoD)
#print("Return w/ leveraging: ", RD)