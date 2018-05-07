#!/usr/bin/env python
# encoding: utf-8

"""Pretty plotter for a visibility map"""

import os
import h5py
import numpy as np
import matplotlib as mpl

from readimages.dpc.commandline_parser import commandline_parser
from readimages.utils.hadd import hadd

commandline_parser.add_argument("--language",
                                default="en",
                                choices=["it", "en"],
                                help="language for the text")
commandline_parser.add_argument("output_file_name", nargs=1)
args = commandline_parser.parse_args()

mpl.use("pgf")

from pgf_style import pgf_with_rc_fonts

mpl.rcParams.update(pgf_with_rc_fonts)

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

input_file_name = hadd(args.file)
output_file_name = args.output_file_name[0]
if not os.path.exists(input_file_name):
    raise(OSError("{0} not found".format(input_file_name)))

if args.language == "it":
    legend_text = "visibilit\\`a media"
else:
    legend_text = "average visibility"

input_file = h5py.File(input_file_name, "r")
object_name = "postprocessing/visibility_{0}".format(
    args.pixel)
input_object = input_file[object_name]
pixels = input_object[0]
visibility = input_object[1]
plt.figure(figsize=(4.6, 3))
axis = plt.axes()
plt.plot(pixels, visibility.T, linewidth=1, color='black')
plt.xlabel("pixel")
plt.ylabel("$v = 2 a_1 / a_0$")
mean_visibility = np.mean(visibility)
min_visibility = np.min(visibility)
max_visibility = np.max(visibility)
line = plt.axhline(y=mean_visibility, linewidth=1,
                   color='black', linestyle='--')
legend = plt.legend([line], ["{0}: {1:.1f} $\\%$".format(
    legend_text,
    mean_visibility * 100)])
legend.get_frame().set_linewidth(0)
axis.set_ylim(
    bottom=0,
    top=1.2*max_visibility)
axis.xaxis.tick_bottom()
axis.yaxis.tick_left()
axis.yaxis.set_major_formatter(FuncFormatter(
    lambda x, pos=0: "{0:.0%}".format(x)))
plt.tight_layout()
plt.savefig(output_file_name)
