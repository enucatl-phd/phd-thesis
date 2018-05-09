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
