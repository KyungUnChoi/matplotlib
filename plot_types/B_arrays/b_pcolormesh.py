"""
===================================
pcolormesh([X, Y], Z, [cmap=], ...)
===================================

`~.axes.Axes.pcolormesh` is more flexible than `~.axes.Axes.imshow` in that
the x and y vectors need not be equally spaced (indeed they can be skewed).

"""
import matplotlib.pyplot as plt
import numpy as np

# make full-res data
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2. + X**5 + Y**3) * np.exp(-X**2 - Y**2)
Z = Z - Z.min()

# sample unevenly in x:
dx = np.sqrt((np.arange(16) - 8)**2) + 6
dx = np.floor(dx / sum(dx) * 255)
xint = np.cumsum(dx).astype('int')
X = X[0, xint]
Y = Y[::8, 0]
Z = Z[::8, :][:, xint]

# plot
with plt.style.context('cheatsheet_gallery'):
    fig, ax = plt.subplots()

    ax.pcolormesh(X, Y, Z, vmin=0, vmax=1.5, shading='nearest')

    plt.show()
