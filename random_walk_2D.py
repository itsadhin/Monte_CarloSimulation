import numpy as np

if __name__ == "__main__":
    displacement_x = []
    displacement_y = []
    square_disp_x = []
    square_disp_y = []
    trial = 1000
    steps = 1000
    for i in range(trial):
        initial_x = 0
        initial_y = 0
        for j in range(steps):
            n_x = np.random.choice([-1,1])
            n_y = np.random.choice([-1,1])
            initial_x += n_x
            initial_y += n_y
        displacement_x.append(initial_x)
        square_disp_x.append(initial_x**2)
        displacement_y.append(initial_y)
        square_disp_y.append(initial_y**2)

    avg = np.average(square_disp_x + square_disp_y)
    print("Average square displacement in 2D: ", avg) # <r^2> = <x^2+y^2>


