import click
import matplotlib.pyplot as plt
import h5py


@click.command()
@click.argument("input_file_name", type=click.Path(exists=True))
@click.argument("output_file_name")
def main(input_file_name, output_file_name):
    with h5py.File(input_file_name, "r") as input_file:
        dataset = input_file["entry/data/threshold_0/data_000001"][
            285:345, 800:900]
        print(dataset.shape)
        plt.imshow(dataset, cmap=plt.cm.Greys_r, aspect="auto")
        plt.colorbar()
        plt.savefig(output_file_name)
        # plt.show()


if __name__ == "__main__":
    main()
