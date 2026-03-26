import numpy as np

if __name__ == "__main__":
    r_square = []
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
        r_square.append(initial_x**2 + initial_y**2)

    avg = np.average(r_square)
    print("Average square displacement in 2D: ", avg) # <r^2> = <x^2+y^2>


