import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path


# Read the Fibonacci numbers
with open("../data/fibonacci.dat", "r") as f:
    n = [int(l) for l in f.readlines()]

# The dimensions of the image we'll plot
N = len(n)
B = len("{:b}".format(n[-1]))

# Cast each number to binary and then to an array of bits
b = np.zeros((N, B), dtype=int)
b[0] = np.zeros(B)
b[1] = np.zeros(B)
b[1, -1] = 1
for i in range(2, N):
    bi = list("{:b}".format(n[i]))
    b[i, -len(bi) :] = bi

# Plot the Fibonacci sequence in binary; idea from
# https://mathworld.wolfram.com/FibonacciNumber.html and
# https://www.maa.org/editorial/mathgames
fig, ax = plt.subplots(figsize=(6, 6))
cmap = matplotlib.colors.ListedColormap(["white", "C0"])
ax.imshow(b, interpolation="nearest", cmap=cmap, aspect="auto")
ax.axis("off")
fig.savefig("figure3.pdf", bbox_inches="tight")