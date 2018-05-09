#!/usr/bin/env Rscript
library(data.table)
library(argparse)
library(ggplot2)

commandline_parser = ArgumentParser(
        description="draw results for fit analysis") 

commandline_parser$add_argument('input')
commandline_parser$add_argument('output')
args = commandline_parser$parse_args()

dt = fread(args$input)
print(dt)
dt[, photons := photons / sum(photons)]

plot = ggplot(dt, aes(x=energy, y=visibility)) +
    geom_line(size=1.2) +
    xlab("energy (keV)") +
    ylab("visibility")

width = 10
factor = 0.618
height = width * factor
print(plot)
ggsave(args$output, plot, width=width, height=height, dpi=300)
invisible(readLines(n=1))
