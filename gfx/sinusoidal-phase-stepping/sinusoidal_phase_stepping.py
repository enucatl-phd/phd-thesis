import numpy as np
import scipy.signal as ss
import click
import matplotlib.pyplot as plt


@click.command()
@click.argument("output_file_name", type=click.Path())
def main(output_file_name):
    t = np.linspace(0, 8 * np.pi, 1000)
    a = ss.square(t)
    b = ss.square(t)
    c = ss.gaussian(1000, 20)
    convolved = ss.fftconvolve(a, b, mode="same")
    smooth = ss.fftconvolve(convolved, c, mode="same")
    plt.axis('off')
    plt.plot(smooth)
    plt.savefig(output_file_name, dpi=300)
    plt.show()
    plt.ion()
    input()

if __name__ == "__main__":
    main()
