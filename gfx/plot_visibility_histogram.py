import h5py
import numpy as np
import click
import matplotlib.pyplot as plt


@click.command()
@click.argument("input_file_name", type=click.Path(exists=True))
@click.argument("output_file_name")
def main(input_file_name, output_file_name):
    with h5py.File(input_file_name, "r") as input_file:
        min_x = 575
        max_x = 900
        min_y = 500
        max_y = 800
        dataset = input_file["postprocessing/visibility"][min_x:max_x,
                                                          min_y:max_y]
        plt.hist(np.ravel(dataset), bins=50)
        plt.xlabel("visibility")
        plt.ylabel("#pixels")
        print(np.mean(dataset))
        plt.savefig(output_file_name, dpi=300)


if __name__ == "__main__":
    main()
