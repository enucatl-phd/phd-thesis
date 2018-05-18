import click
import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


@click.command()
@click.option("--min_x", default=0)
@click.option("--max_x", default=-1)
@click.argument("input_file_name", type=click.Path(exists=True))
@click.argument("output_file_name", type=click.Path())
@click.option("--group", default="raw_images")
def main(min_x, max_x, input_file_name, output_file_name, group):
    with h5py.File(input_file_name) as input_file:
        dataset = np.vstack(
            d[min_x:max_x] for d in input_file[group].values()
            if isinstance(d, h5py.Dataset))
        print(dataset.shape)
        plt.imshow(dataset,
                   cmap=plt.cm.Greys, aspect='auto')
        limits = stats.mstats.mquantiles(dataset,
                                        prob=[0.02, 0.98])
        plt.clim(*limits)
        plt.tight_layout()
        plt.savefig(output_file_name, dpi=300)
        # plt.show()
        # plt.ion()


if __name__ == "__main__":
    main()
