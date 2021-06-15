import math

def GeoDis():
    print("Number of tries until success")
    sr = float(input("What is the success rate: "))
    numTry = float(input("Number of tries: "))
    probSRequals = (1 - sr) ** (numTry - 1) * sr
    print(" P(X=n) = ", probSRequals)
    c = numTry                                          #DOUBLE CHECK (numTry - 1)?
    sumofProb = 0
    while c != 0:
        sumofProb = sumofProb + ((1 - sr) ** (c - 1) * sr)
        c = c - 1
    print(" P(X<n) = ", sumofProb)
    print("Mean: ", 1 / sr)
    print("Variance: ", (1 - sr) / sr ** 2)

def BinDis():
    print("What are the odds that if we pick X objects from a group, Y will succeed, given a success rate")
    numGroup = float(input("Amount in group: "))
    sr = float(input("What is the success rate: "))
    numSelected = float(input("Number of objects selected: "))
    probBin = (math.factorial(numGroup)/(math.factorial(numGroup-numSelected)*math.factorial(numSelected)))\
              *sr**numSelected*(1-sr)**(numGroup-numSelected)
    print(" P(X = n) = ", probBin)
    c = numSelected                                     #DOUBLE CHECK (numSelected - 1)?
    sumofProb = 0
    while c != -1:
        sumofProb = sumofProb + (math.factorial(numGroup)/(math.factorial(numGroup-c)*math.factorial(c)))\
                    *sr**c*(1-sr)**(numGroup-c)
        c = c - 1
    print(" P(X < n) = ", sumofProb)
    print("Mean: ", numGroup*sr)
    print("Variance: ", numGroup*sr*(1-sr))

def PoiDis():
    print("Discrete probability distribution of the number of independent events occurring in a given time period, "
          "given the average number of times the event occurs in the same time period")
    avg = float(input("Average number of times event occurs: "))
    numOcc = float(input("Number of times event occurs: "))
    probPoi = math.exp(-avg)*(avg**numOcc)/(math.factorial(numOcc))
    print(" P(X = n) = ", probPoi)
    c = numOcc - 1                                          #DOUBLE CHECK (numOcc - 1)?
    sumofProb = 0
    while c != -1:
        sumofProb = sumofProb + math.exp(-avg)*(avg**c)/(math.factorial(c))
        c = c - 1
    print(" P(X < n) = ", sumofProb)
    print("Mean and Variance: ", avg)

running = True
while running == True:
    a = int(input("1 for Geometric, 2 for Binomial, 3 for Poisson"))
    if a == 1:
        GeoDis()
    if a == 2:
        BinDis()
    if a == 3:
        PoiDis()
    end = input("Go again? (y/n)")
    if end == "n":
        running = False