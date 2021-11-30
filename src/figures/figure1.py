"""
Generate a figure from the simulation results.

"""
import numpy as np
import matplotlib.pyplot as plt


# Load the simulation results
X = np.loadtxt("../data/simulation.dat")

# Plot the figure
fig, ax = plt.subplots(1)
ax.imshow(X, cmap="viridis")
ax.axis("off")
fig.savefig("figure1.pdf", bbox_inches="tight")