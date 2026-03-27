import numpy as np

def function(x):
    return np.exp(-x**2)*np.sin(5*x)+(x**3-2*x+1)/(x**2+1) # can use any function here

def Reimann_Sum(x):   # i know i dont have to define function for one line code but I felt like keeping it structured like this
    return function(x)*delta_x

if __name__ == "__main__":
    steps = 100000
    starting_point = 0
    ending_point = 4
    Reimann = []
    delta_x = (ending_point - starting_point)/steps
    x_k = np.arange(starting_point + delta_x, ending_point + delta_x, delta_x)    
    for j in range(steps):
        Reimann.append(Reimann_Sum(x_k[j]))
    integral = np.sum(Reimann)
    print("Integral: ",integral)
