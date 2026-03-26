import numpy as np
import random

def point():
    x1 = np.random.uniform(0,1)
    y1 = np.random.uniform(0,1)
    return x1,x2,y1,y2

def distance(x1,x2,y1,y2):
    return (np.sqrt((x2 - x1)**2 + (y2 - y1)**2))

if __name__ == "__main__":
    steps = 10000000
    inside_square = 0
    inside_circle = 0
    x2 = 0 # Considering distance from origin
    y2 = 0
    for i in range(steps):
        inside_square +=1
        v = point()
        d = distance(*v)
        if d <= 1:
            inside_circle +=1

    # pi = 4*r^2/r^2  (Area of circle of radius r so square side length 2r)
    pi = 4*(inside_circle/inside_square)
    print(f"Value of pi for {steps} steps is: ",pi)
    """
    More the steps more accurate it would get :)
    """
