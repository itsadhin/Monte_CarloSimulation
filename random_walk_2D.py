import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    r_square = []
    trial = 5000
    steps = 1000
    r_sqr_step = np.zeros(steps)
    N_steps = np.arange(1,steps+1)
    N_trail = np.arange(1,trial+1)
    final_x = []
    final_y = []

    for i in range(trial):
        initial_x = 0
        initial_y = 0
        for j in range(steps):
            n_x = np.random.choice([-1,1])
            n_y = np.random.choice([-1,1])
            initial_x += n_x
            initial_y += n_y
            r_sqr = initial_x**2 + initial_y**2
            r_sqr_step[j] += r_sqr
        r_square.append(initial_x**2 + initial_y**2)
        final_x.append(initial_x)
        final_y.append(initial_y)
       
    r_sqr_step /= trial
    avg = np.average(r_square)
    print("Average square displacement in 2D: ", avg) # <r^2> = <x^2+y^2>
    plt.plot(r_sqr_step)
    plt.xlabel("Number of steps")
    plt.ylabel("<r^2>")
    plt.title(f"Random Walk 2D for {steps} steps")
    plt.grid()
    plt.savefig("2Dwalk.png")
    plt.figure()
    plt.hist(r_square,bins=30)
    plt.xlabel("Square of final displacement")
    plt.ylabel("Count")
    plt.title(f"2D walk Histogram for {trial} trial")
    plt.savefig("2D_histogram.png")
    plt.figure()
    plt.hist(final_x,bins=30)
    plt.xlabel("Final position in x axis")
    plt.ylabel("Count")
    plt.title("Final x position")
    plt.savefig("xaxis_2D.png")
    plt.figure()
    plt.hist(final_y,bins=30)
    plt.xlabel("Final position in y axis")
    plt.ylabel("Count")
    plt.title("Final y position")
    plt.savefig("yaxis_2D.png")

