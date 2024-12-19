import numpy as np
import matplotlib.pyplot as plt


def flux_surface(A=2.2, kappa=1.5, delta=0.3, R0=2.5):
    """
    This function calculates the flux surface

    Inputs:
    A (= 2.2 by default)
    kappa (= 1.5 by default)
    delta (= 0.3 by default)
    R0 (= 2.5 by default)

    Outputs (as tuple):
    R_s
    Z_s
    """
    theta = np.linspace(0, 2 * np.pi)
    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    return (R_s, Z_s)


def plot_surface(R_s, Z_s, savefig=True, ax=None):
    """
    Read in R_s and Z_s and plot figure

    Inputs:
    R_s
    Z_s
    savefig (= true)
    ax (= None)
    """
    if ax is None:
        (fig, ax) = plt.subplots()
    ax.plot(R_s, Z_s)
    ax.axis("equal")
    ax.set_xlabel("R [m]")
    ax.set_ylabel("Z [m]")
    if savefig:
        plt.savefig("./miller.png")


def main():
    (R_s, Z_s) = flux_surface()
    plot_surface(R_s, Z_s)


if __name__ == "__main__":
    main()
