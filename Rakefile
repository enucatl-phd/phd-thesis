require "rake/clean"

LATEX_TEXT = FileList["*.tex, FrontBackmatter/*.tex, Chapters/*.tex"]
PICTURES = FileList["gfx/*"]
CLEAN.include(FileList["*.aux", "*.bbl", "*.blg", "*.brf", "*.idx", "*.ilg", "*.ind", "*.log"])
CLOBBER.include(FileList["*.pdf"])

namespace :main do

  desc "main pdf"
  file "ClassicThesis.pdf" => ["ClassicThesis.tex", "Bibliography.bib", "gfx:all"] + PICTURES + LATEX_TEXT do |f|
    sh "pdflatex ClassicThesis"
    sh "biber ClassicThesis"
    sh "pdflatex ClassicThesis"
    sh "pdflatex ClassicThesis"
  end

end

namespace :gfx do

  EEPIC = FileList["gfx/*.xp"]
  for picture_filename in EEPIC do
    file picture_filename.ext(".eepic") => picture_filename do |t|
      Dir.chdir("gfx") do
        sh "epix --tikz -o #{File.basename(t.name)} #{File.basename(t.source)}"
      end
    end
  end

  file "gfx/visibility_visibility_100kev.pgf" => ["gfx/visibility_100kev.hdf5", "gfx/plot_visibility_pgf.py"] do |f|
    sh "python #{f.prerequisites[1]} --steps 25 --pixel 510 #{f.source} #{f.name}"
  end

  file "gfx/visibility_S00618.pgf" => ["gfx/S00618.hdf5", "gfx/plot_visibility_pgf.py"] do |f|
    sh "python #{f.prerequisites[1]} --steps 25 --pixel 510 #{f.source} #{f.name}"
  end

  file "gfx/images_S00052.pgf" => ["gfx/S00052.hdf5", "gfx/plot_images.py"] do |f|
    sh "python #{f.prerequisites[1]} #{f.source} #{f.name} 6"
  end

  file "gfx/images_S00075_S00071.pgf" => ["gfx/S00075_S00071.hdf5", "gfx/plot_images.py"] do |f|
    sh "python #{f.prerequisites[1]} #{f.source} #{f.name} 7"
  end

  file "gfx/images_S00613.pgf" => ["gfx/S00613.hdf5", "gfx/plot_images.py"] do |f|
    sh "python #{f.prerequisites[1]} #{f.source} #{f.name} 2.5"
  end

  file "gfx/lynch-vs-saxs/plot.png" => ["gfx/lynch-vs-saxs/plot_lynch_saxs.R", "gfx/lynch-vs-saxs/lynch.csv", "gfx/lynch-vs-saxs/saxs.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.prerequisites[2]} #{f.name}"
  end

  file "gfx/alignment-rot-x.png" => ["gfx/image_series.py", "#{ENV["HOME"]}/afsproject_backup/raw_data/2015/mythen/2015.06.22/S00000-00999/S00083.hdf5"] do |f|
    sh "python #{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/alignment-rot-z.png" => ["gfx/image_series.py", "#{ENV["HOME"]}/afsproject_backup/raw_data/2015/mythen/2015.06.22/S00000-00999/S00035.hdf5"] do |f|
    sh "python #{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/delta-beta-comparison/delta-beta-comparison.png" => ["gfx/delta-beta-comparison/delta_beta_plot.R", "gfx/delta-beta-comparison/delta_beta.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/delta-beta-comparison/delta_beta.csv" => ["gfx/delta-beta-comparison/delta_beta_comparison.py"] do |f|
    sh "python #{f.source} #{f.name}"
  end

  file "gfx/sinusoidal-phase-stepping/sinusoidal-phase-stepping.png" => ["gfx/sinusoidal-phase-stepping/sinusoidal_phase_stepping.py"] do |f|
    sh "python #{f.source} #{f.name}"
  end


  desc "all images"
  task :all => EEPIC.ext(".eepic") + [
    "gfx/visibility_visibility_100kev.pgf",
    "gfx/visibility_S00618.pgf",
    "gfx/images_S00052.pgf",
    "gfx/images_S00075_S00071.pgf",
    "gfx/images_S00613.pgf",
    "gfx/lynch-vs-saxs/plot.png",
    "gfx/alignment-rot-x.png",
    "gfx/delta-beta-comparison/delta-beta-comparison.png",
    "gfx/sinusoidal-phase-stepping/sinusoidal-phase-stepping.png",
  ]

end
