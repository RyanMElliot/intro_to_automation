import millerplasma as mil
import numpy as np
import matplotlib.pyplot as plt


def area(r, z):
    """
    This function calculates the area of the
    cross-sectional area of an axisymmetric tokamak
    """
    return np.abs(np.trapezoid(z, r))


def areas_from_deltas(deltas):
    """calculate areas from input delta values"""
    areas = np.empty(np.shape(deltas))
    for i in range(0, len(deltas)):
        (r, z) = mil.flux_surface(delta=deltas[i])
        areas[i] = area(r, z)
    return areas


def plot_delta_areas(deltas, areas, savefig=True, ax=None):
    """
    Read in delta values and area values and plot figure

    Inputs:
    deltas
    areas
    savefig (= true)
    """
    if ax is None:
        (fig, ax) = plt.subplots()

    ax.plot(deltas, areas)
    ax.axis("equal")
    ax.set_xlabel("Delta")
    ax.set_ylabel("Area [m^2]")
    if savefig:
        plt.savefig("./areas.png")


def main():
    deltas = np.linspace(0, 0.7, 71)
    areas = areas_from_deltas(deltas)
    (R_s, Z_s) = mil.flux_surface()
    print(Z_s)
    fig, (ax1,ax2) = plt.subplots(1, 2)
    mil.plot_surface(R_s, Z_s, savefig=False,ax=ax1)
    plot_delta_areas(deltas, areas, ax=ax2)
    


if __name__ == "__main__":
    main()
