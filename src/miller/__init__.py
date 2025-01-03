import numpy as np
import matplotlib.pyplot as plt
import argparse
import tomli


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


def plot_surface(
    R_s, Z_s, savefig=True, filename="./miller.png", ax=None, showfig=False
):
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
        plt.savefig(filename)

    if showfig:
        plt.show()


def main():
    parser = argparse.ArgumentParser(
        prog="Miller", description="Plots the Miller Surface for certain values"
    )
    parser.add_argument(
        "-i", "--filein", help="input args, Default = None", default=None
    )
    parser.add_argument("-A", "--A", help="Default = 2.2", type=float, default=2.2)
    parser.add_argument("-k", "--kappa", help="Default = 1.5", type=float, default=1.5)
    parser.add_argument("-d", "--delta", help="Default = 0.3", type=float, default=0.3)
    parser.add_argument("-R", "--R0", help="Default = 2.5", type=float, default=2.5)
    parser.add_argument(
        "-f",
        "--filename",
        help="Default = ./miller.png",
        type=str,
        default="./miller.png",
    )
    parser.add_argument("-s", "--showfig", action="store_true")
    args = parser.parse_args()
    args = vars(args)

    filename = args.pop("filename")
    showfig = args.pop("showfig")

    filein = args.pop("filein")
    if filein is not None:
        with open(filein, "rb") as f:
            data = tomli.load(f)
            args = data["miller"]

    print(args)
    (R_s, Z_s) = flux_surface(**args)

    plot_surface(R_s, Z_s, filename=filename, showfig=showfig)


if __name__ == "__main__":
    main()
