import numpy as np
import random

def point():
    x1 = random.choice(np.linspace(0,1,100)) 
    x2 = random.choice(np.linspace(0,1,100)) 
    y1 = random.choice(np.linspace(0,1,100)) 
    y2 = random.choice(np.linspace(0,1,100)) 
    return x1,x2,y1,y2

def distance(x1,x2,y1,y2):
    return (np.sqrt((x2 - x1)**2 + (y2 - y1)**2))

if __name__ == "__main__":
    d = []
    steps = 10000
    for i in range(steps):
        v = point()
        d.append(distance(*v)) # takes each value from tuple and calculates the function
    
    avg = np.average(d)
    print(f"Average for {steps} steps: ", avg)
