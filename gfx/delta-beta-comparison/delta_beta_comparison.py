import click
import csv
import nist_lookup.xraydb_plugin as xdb


@click.command()
@click.argument("output_file", type=click.File("w"), default="-")
def main(output_file):
    materials = ["C", "O", "Au", "Si"]
    densities = [2, 1.429e-3, 19.3, 2.33]
    energies = range(10, 200)
    csv_output = csv.writer(output_file)
    csv_output.writerow(["material", "energy", "delta", "beta"])
    for energy in energies:
        for material, density in zip(materials, densities):
            delta, beta, _ = xdb.xray_delta_beta(
                material, density, energy * 1e3)
            csv_output.writerow([material, energy, delta, beta])


if __name__ == "__main__":
    main()
