import numpy as np
import matplotlib.pyplot as plt


# Load the random numbers
X = [np.loadtxt(f"../data/random_numbers_{value}.dat") for value in range(0, 10)]

# Plot them
fig, ax = plt.subplots(1)
plt.plot(X)
fig.savefig("figure2.pdf", bbox_inches="tight")