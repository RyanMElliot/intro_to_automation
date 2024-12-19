import numpy as np
import matplotlib.pyplot as plt
def main():
    def flux_surface(A = 2.2,kappa = 1.5,delta = 0.3,R0 = 2.5):
        theta = np.linspace(0, 2 * np.pi)
        r = R0 / A
        R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
        Z_s = kappa * r * np.sin(theta)
        return (R_s,Z_s)

    def plot_surface(R_s,Z_s,savefig = True):
        plt.plot(R_s, Z_s)
        plt.axis("equal")
        plt.xlabel("R [m]")
        plt.ylabel("Z [m]")
        if savefig:
            plt.savefig("./miller.png")


if __name__ == "__main__":
    main()
