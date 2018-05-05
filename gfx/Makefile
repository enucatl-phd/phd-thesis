PICTURES = $(wildcard *.png *.jpg) interaction.eepic phase_stepping.eepic\
			grating_interferometer.eepic\
			foam_sample.eepic\
			visibility_visibility_100kev.pgf visibility_S00618.pgf\
			images_S00052.pgf images_S00075_S00071.pgf images_S00613.pgf\
			profile_S00613.pgf stats_phase_constant_kurtosis.pgf\
			stats_phase_visibility_median.pgf\
			stats_visibility_constant_skewness.pgf stats_phase_constant_mean.pgf\
			stats_phase_visibility_sd.pgf\
			stats_visibility_visibility_kurtosis.pgf stats_phase_constant_median.pgf\
			stats_phase_visibility_skewness.pgf     stats_visibility_visibility_mean.pgf\
			stats_phase_constant_sd.pgf          stats_visibility_constant_kurtosis.pgf\
			stats_visibility_visibility_median.pgf stats_phase_constant_skewness.pgf\
			stats_visibility_constant_mean.pgf      stats_visibility_visibility_sd.pgf\
			stats_phase_visibility_kurtosis.pgf  stats_visibility_constant_median.pgf\
			stats_visibility_visibility_skewness.pgf stats_phase_visibility_mean.pgf\
			stats_visibility_constant_sd.pgf

all: $(PICTURES)

%.eepic: %.xp
	epix --tikz $^

visibility_visibility_100kev.pgf: visibility_100kev.hdf5 plot_visibility_pgf.py
	python plot_visibility_pgf.py --steps 25 --pixel 510 $<

visibility_S00618.pgf: S00618.hdf5 plot_visibility_pgf.py
	python plot_visibility_pgf.py --steps 25 --pixel 510 $<

images_S00052.pgf: S00052.hdf5 plot_images.py
	python plot_images.py $< 6

images_S00075_S00071.pgf: S00075_S00071.hdf5 plot_images.py
	python plot_images.py $< 7

images_S00613.pgf: S00613.hdf5 plot_images.py
	python plot_images.py $< 2.5

profile_S00613.pgf: S00613.hdf5 plot_profile.py
	python plot_profile.py $<

stats_%.pgf: plots.R data_analysis.rda
	./plots.R
