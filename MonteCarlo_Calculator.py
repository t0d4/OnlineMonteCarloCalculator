""""
Conduct the MonteCarlo method.
Mode 0: Elements of coordinates are decimal between 0(included) and 10(excluded)
Mode 1: Elements of coordinates are integers between 1(included) and 10(included).
"""
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


def MonteCarlo(N: int, mode: int) -> tuple:

    if mode == 0:
        x = 10.0 * np.random.rand(N)
        y = 10.0 * np.random.rand(N)
    elif mode == 1:
        x = np.random.randint(1, 11, (N, ))
        y = np.random.randint(1, 11, (N, ))

    norms = np.linalg.norm((x, y), axis=0)
    is_included = (norms <= 10)
    x_included = x[is_included]
    y_included = y[is_included]
    x_excluded = x[np.logical_not(is_included)]
    y_excluded = y[np.logical_not(is_included)]

    estimated_pi = 4 * np.sum(is_included) / N

    fig = plt.figure()
    axis = fig.add_subplot(111, xlabel="x", ylabel="y")
    axis.cla()

    axis.set_aspect("equal")
    axis.set_xlim(0, 10)
    axis.set_ylim(0, 10)

    # plot random coordinates
    axis.scatter(x_included, y_included, c="blue")
    axis.scatter(x_excluded, y_excluded, c="red")

    # display a circle
    theta = np.linspace(0, np.pi/2)
    axis.plot(10 * np.cos(theta), 10 * np.sin(theta))

    axis.text(8, 9, f"N={N}")
    axis.text(8, 8.5, f"pi={round(estimated_pi, 4)}")

    figdata = BytesIO()
    fig.savefig(figdata, format='png')

    fig_b64str = base64.b64encode(figdata.getvalue()).decode("utf-8")
    fig_b64data = f"data:image/png;base64,{fig_b64str}"

    return (round(estimated_pi, 6), fig_b64data)
