import numpy as np

if __name__ == "__main__":
    displacement = []
    square_disp = []
    trial = 1000
    steps = 1000
    for i in range(trial):
        initial = 0
        for j in range(steps):
            n = np.random.choice([-1,1])
            initial += n
        displacement.append(initial)
        square_disp.append(initial**2)
    
    avg1 = np.average(displacement)
    avg2 = np.average(square_disp)
    print("Average displacement: ", avg1)
    print("Average square displacement: ", avg2)


