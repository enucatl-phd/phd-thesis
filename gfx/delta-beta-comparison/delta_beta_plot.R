#!/usr/bin/env Rscript

library(argparse)
library(ggplot2)
library(data.table)

commandline_parser = ArgumentParser(
        description="draw results for fit analysis") 

commandline_parser$add_argument('input')
commandline_parser$add_argument('output')
args = commandline_parser$parse_args()

dt = fread(args$input)
print(dt)

width = 10
factor = 0.618
height = width * factor

plot = ggplot(dt, aes(x=energy, y=delta/beta)) +
    geom_line(aes(linetype=material, colour=material)) +
    scale_y_log10() +
    ylab("δ/β") +
    xlab("energy (keV)")

print(plot)
ggsave(args$output, plot, width=width, height=height, dpi=300)
