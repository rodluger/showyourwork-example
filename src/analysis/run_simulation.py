"""
Run a (fake) simulation and generate a simulation results file.

"""
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import zoom

# Generate a random image with some nice structure
# This is the "expensive" operation that generates
# the figure in our paper.
np.random.seed(0)
X = np.random.randn(300, 300)
scharr = np.array(
    [
        [-3 - 3j, 0 - 10j, +3 - 3j],
        [-10 + 0j, 0 + 0j, +10 + 0j],
        [-3 + 3j, 0 + 10j, +3 + 3j],
    ]
)
X = np.angle(convolve2d(X, scharr, boundary="wrap", mode="same"))
X = zoom(X, 5)[:300, :300]

# Save the "simulation" results to disk
np.savetxt("../data/simulation.dat", X=X)