import numpy as np
import scipy.signal as ss
import click
import matplotlib.pyplot as plt


@click.command()
@click.argument("output_file_name", type=click.Path())
def main(output_file_name):
    t = np.linspace(0, 10 * np.pi, 1000)
    a = ss.square(t)
    b = ss.square(t)
    c = ss.gaussian(1000, 20)
    convolved = ss.fftconvolve(a, b, mode="same")
    smooth = ss.fftconvolve(convolved, c, mode="same")
    # plt.axis('off')
    ax = plt.gca()
    ax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    ax.set_xticklabels(["$0$"] + ["$\pi$"] + ["${}\pi$".format(i) for i in range(2, 11)])
    ax.get_yaxis().set_visible(False)
    plt.plot(smooth)
    plt.savefig(output_file_name, dpi=300)
    plt.show()
    plt.ion()
    input()

if __name__ == "__main__":
    main()
