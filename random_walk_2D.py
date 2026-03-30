import numpy as np
import matplotlib.pyplot as plt

def diffusion():
    n_x = np.random.choice([-1,1])
    n_y = np.random.choice([-1,1])
    return n_x,n_y

def drift():
    n_x = np.random.choice([-1,1] , p=[0.3,0.7]) # just change the prob to change bias
    n_y = np.random.choice([-1,1] , p=[0.4,0.6])
    return n_x,n_y

if __name__ == "__main__":
    while True:
        choice = input("Would you like to see drift condition or diffusion condition? ")
        if choice.lower() == "drift":
            print("Please wait while the code runs...")
            r_square = []
            trial = 1000
            steps = 1000
            r_sqr_step = np.zeros(steps)
            N_steps = np.arange(1,steps+1)
            N_trail = np.arange(1,trial+1)
            final_x = []
            final_y = []

            for i in range(trial):
                initial_x = 0
                initial_y = 0
                p_x = []
                p_y = []
                for j in range(steps):
                    n_x,n_y = drift()
                    initial_x += n_x
                    initial_y += n_y
                    r_sqr = initial_x**2 + initial_y**2
                    r_sqr_step[j] += r_sqr
                    p_x.append(initial_x)
                    p_y.append(initial_y)
                r_square.append(initial_x**2 + initial_y**2)
                final_x.append(initial_x)
                final_y.append(initial_y)
           
            r_sqr_step /= trial
            avg = np.average(r_square)
            print("Average square displacement in 2D: ", avg) # <r^2> = <x^2+y^2>
            plt.plot(N_steps,r_sqr_step)
            plt.xlabel("Number of steps")
            plt.ylabel("<r^2>")
            plt.title(f"Random Walk 2D for {steps} steps")
            plt.grid()
            plt.savefig("2Dwalk_drift.png")
            plt.figure()
            plt.hist(r_square,bins=30)
            plt.xlabel("Square of final displacement")
            plt.ylabel("Count")
            plt.title(f"2D walk Histogram for {trial} trial")
            plt.savefig("2D_histogram_drift.png")
            plt.figure()
            plt.hist(final_x,bins=30)
            plt.xlabel("Final position in x axis")
            plt.ylabel("Count")
            plt.title("Final x position")
            plt.savefig("xaxis_2D_drift.png")
            plt.figure()
            plt.hist(final_y,bins=30)
            plt.xlabel("Final position in y axis")
            plt.ylabel("Count")
            plt.title("Final y position")
            plt.savefig("yaxis_2D_drift.png")
            plt.figure()
            # prints the random path of the final random walk
            plt.plot(p_x,p_y)
            plt.savefig("motion_drift.png")
            break
 
        elif choice.lower() == "diffusion":
            print("Please wait while the code runs...")
            r_square = []
            trial = 1000
            steps = 1000
            r_sqr_step = np.zeros(steps)
            N_steps = np.arange(1,steps+1)
            N_trail = np.arange(1,trial+1)
            final_x = []
            final_y = []

            for i in range(trial):
                initial_x = 0
                initial_y = 0
                p_x = []
                p_y = []
                for j in range(steps):
                    n_x,n_y = diffusion()
                    initial_x += n_x
                    initial_y += n_y
                    r_sqr = initial_x**2 + initial_y**2
                    r_sqr_step[j] += r_sqr
                    p_x.append(initial_x)
                    p_y.append(initial_y)
                r_square.append(initial_x**2 + initial_y**2)
                final_x.append(initial_x)
                final_y.append(initial_y)
           
            r_sqr_step /= trial
            avg = np.average(r_square)
            print("Average square displacement in 2D: ", avg) # <r^2> = <x^2+y^2>
            plt.plot(N_steps,r_sqr_step)
            plt.xlabel("Number of steps")
            plt.ylabel("<r^2>")
            plt.title(f"Random Walk 2D for {steps} steps")
            plt.grid()
            plt.savefig("2Dwalk_diffusion.png")
            plt.figure()
            plt.hist(r_square,bins=30)
            plt.xlabel("Square of final displacement")
            plt.ylabel("Count")
            plt.title(f"2D walk Histogram for {trial} trial")
            plt.savefig("2D_histogram_diffusion.png")
            plt.figure()
            plt.hist(final_x,bins=30)
            plt.xlabel("Final position in x axis")
            plt.ylabel("Count")
            plt.title("Final x position")
            plt.savefig("xaxis_2D_diffusion.png")
            plt.figure()
            plt.hist(final_y,bins=30)
            plt.xlabel("Final position in y axis")
            plt.ylabel("Count")
            plt.title("Final y position")
            plt.savefig("yaxis_2D_diffusion.png")
            plt.figure()
            # prints the random path of the final random walk
            plt.plot(p_x,p_y)
            plt.savefig("motion_diffusion.png")
            break

        else:
            print("The input is invalid, input should be drift or diffussion...")
    

