#!/usr/bin/env Rscript

library(reshape2)
library(data.table)
library(argparse)
library(ggplot2)

parser <- ArgumentParser(description='compare lynch and saxs prediction')
parser$add_argument('lynch', nargs=1)
parser$add_argument('saxs', nargs=1)
parser$add_argument('output', nargs=1)
args <- parser$parse_args()

lynch = fread(args$lynch)[seq(1, 100, 6), ]
lynch[, method := "gi"]
saxs = fread(args$saxs)[seq(3, 100, 5),]
saxs[, method := "usaxs"]

merged = rbindlist(list(lynch, saxs))
merged[, diameter := 1e6 * diameter]
print(merged)

plot = ggplot(merged, aes(x=diameter, y=dfec)) +
    geom_point(aes(shape=method, colour=method), size=2) +
    xlab("diameter (μm)") +
    ylab("μ (1/m)")

dev.new()
print(plot)

width = 10
factor = 0.618
height = width * factor
ggsave(args$output, plot, width=width, height=height, dpi=300)
invisible(readLines(con="stdin", 1))
