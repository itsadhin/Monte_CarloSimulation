"""
Based on Wright-Fisher Model
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000    #Population
steps = 1000
trials = 500
history = []

for i in range(trials):
    p = np.random.rand()  # allele freq
    ancestors = []
    for j in range(steps):
        x = np.random.binomial(2*N,p)
        p = x/(2*N)
        ancestors.append(p)
    history.append(ancestors)
# just ploting for a few
for k in range(10):
    plt.plot(history[k],alpha=0.8)
plt.xlabel("Generation")
plt.ylabel("Allele frequency p")
plt.savefig("plot.png")

