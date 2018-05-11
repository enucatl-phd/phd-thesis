#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import h5py
import numpy as np
from scipy import stats
import matplotlib as mpl

mpl.use("pgf")

from pgf_style import pgf_with_rc_fonts

mpl.rcParams.update(pgf_with_rc_fonts)

import matplotlib.pyplot as plt

def draw(input_file_name, absorption_image, differential_phase_image, dark_field_image):
    """Display the profiles with matplotlib."""
    absorption_image_title = "assorbimento"
    differential_phase_image_title = "fase differenziale"
    dark_field_image_title = "riduzione di visibilit\\`a"
    dark_field_image = dark_field_image / absorption_image ** 2
    absorption_profile = np.mean(absorption_image, axis=0)
    dark_field_profile = np.mean(dark_field_image, axis=0)
    plt.figure(figsize=(4.6, 4.6 * 0.618))
    axis = plt.axes()
    plt.xlabel("pixel")
    plt.ylabel("A, B")
    pixels = np.arange(absorption_profile.shape[0])
    plt.plot(pixels, absorption_profile,
            label="transmission $A$",
            color="black",
            linestyle="--",
            linewidth=1)
    plt.plot(pixels, dark_field_profile,
            label="dark field $B$",
            color="black",
            linewidth=1)
    handles, labels = axis.get_legend_handles_labels()
    legend = plt.legend(handles, labels,
            loc="lower right")
    legend.get_frame().set_linewidth(0)
    axis.yaxis.tick_left()
    axis.xaxis.tick_bottom()
    axis.set_ylim(bottom=0, top=1.1)
    axis.set_xlim(left=0, right=650)
    plt.savefig('profile_{0}.pgf'.format(
        os.path.splitext(os.path.basename(input_file_name))[0]))

input_file_name = sys.argv[1]

if not os.path.exists(input_file_name):
    raise(OSError("{0} not found".format(input_file_name)))

input_file = h5py.File(input_file_name, "r")
absorption_image_name = "postprocessing/absorption"
differential_phase_image_name = "postprocessing/differential_phase"
visibility_reduction_image_name = "postprocessing/visibility_reduction"

absorption_image = input_file[absorption_image_name][...]
differential_phase_image = input_file[differential_phase_image_name][...]
visibility_reduction_image = input_file[visibility_reduction_image_name][...]

draw(input_file_name, absorption_image,
        differential_phase_image, visibility_reduction_image)
