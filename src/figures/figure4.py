import numpy as np
import matplotlib.pyplot as plt


# Load the "simulation" results
X = [np.loadtxt(f"../data/results_{value}.dat") for value in range(0, 10)]

# Plot them
fig, ax = plt.subplots(1)
ax.imshow(X)
fig.savefig("figure4.pdf", bbox_inches="tight")