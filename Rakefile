require "rake/clean"

LATEX_TEXT = FileList["*.tex", "FrontBackmatter/*.tex", "Chapters/*.tex"]
PICTURES = FileList["gfx/*"]
CLEAN.include(FileList["*.aux", "*.bbl", "*.blg", "*.brf", "*.idx", "*.ilg", "*.ind", "*.log"])
CLOBBER.include(FileList["*.pdf"])
EEPIC = FileList["gfx/*.xp"]
IMAGES = EEPIC.ext(".eepic") + [
    "gfx/visibility_visibility_100kev.pgf",
    "gfx/visibility_S00618.pgf",
    "gfx/images_S00052.pgf",
    "gfx/mythen-edge-on/efficiency.png",
    "gfx/images_S00075_S00071.pgf",
    "gfx/images_S00613.pgf",
    "gfx/lynch-vs-saxs/plot.png",
    "gfx/alignment-rot-x.png",
    "gfx/delta-beta-comparison/delta-beta-comparison.png",
    "gfx/sinusoidal-phase-stepping/sinusoidal-phase-stepping.png",
    "gfx/spectrum-visibility/spectrum.png",
    "gfx/spectrum-visibility/spectrum-100kV.png",
    "gfx/spectrum-visibility/visibility.png",
    "gfx/omnidirectional/visibility-omnidirectional.png",
    "gfx/eiger/efficiency.png",
  ]

namespace :main do

  desc "main pdf"
  file "ClassicThesis.pdf" => ["ClassicThesis.tex", "Bibliography.bib", "version.tex"] + IMAGES + LATEX_TEXT do |f|
    sh "pdflatex ClassicThesis"
    sh "biber ClassicThesis"
    sh "pdflatex ClassicThesis"
    sh "pdflatex ClassicThesis"
  end

  desc "write version text"
  task "version" do |f|
    version_string = `git describe --tags | tr -d '\n'`
    current_version_string = `cat version.txt`
    if version_string != current_version_string
      File.open "version.txt", "w" do |output|
        p "writing version #{version_string}"
        output.write version_string
      end
    end
  end

  desc "write version file"
  file "version.tex" => "main:version" do |f|
    version_string = `cat version.txt`
    current_version_string = `cat #{f.name}`
    output_string = "\\newcommand{\\myVersion}{#{version_string}}"
    if output_string != current_version_string
      File.open f.name, "w" do |output|
        p "writing version #{version_string}"
        output.write output_string
      end
    end
  end

  desc "publish compiled version to github"
  task "publish" do |f|
    clean_check = `git status --porcelain`
    unless clean_check.empty?
      abort "uncommitted changes, cannot publish"
    end
    unless system("git describe --exact-match --tags HEAD")
      #create tag if it doesnt exist
      automatic_tag_name = `git describe | tr -d '\n'`
      sh "git tag #{automatic_tag_name}"
    end
    tag_name = `git describe --tags | tr -d '\n'`
    sh "git push"
    sh "git push --tags"
    Rake::Task["ClassicThesis.pdf"].invoke
    token = `cat ~/github_token | tr -d '\n'`
    sh "upload-release.py -vvv --owner Enucatl --repo phd-thesis --tag #{tag_name} --token #{token} ClassicThesis.pdf"
  end

end

namespace :gfx do

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

  file "gfx/spectrum-visibility/visibility.png" => ["gfx/spectrum-visibility/visibility.R", "gfx/spectrum-visibility/12-full-spectrum.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/spectrum-visibility/spectrum-100kV.png" => ["gfx/spectrum-visibility/spectrum.R", "gfx/spectrum-visibility/spectrum-100kV.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/spectrum-visibility/spectrum.png" => ["gfx/spectrum-visibility/spectrum.R", "gfx/spectrum-visibility/12-full-spectrum.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/mythen-edge-on/efficiency.png" => ["gfx/mythen-edge-on/plot_efficiency.R", "gfx/mythen-edge-on/efficiency.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  file "gfx/eiger/efficiency.png" => ["gfx/mythen-edge-on/plot_efficiency.R", "gfx/eiger/efficiency.csv"] do |f|
    sh "./#{f.source} #{f.prerequisites[1]} #{f.name}"
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

  file "gfx/omnidirectional/visibility-omnidirectional.png" => ["gfx/omnidirectional/plot_image.py", "gfx/omnidirectional/171004.144941111316.h5"] do |f|
    sh "python #{f.source} #{f.prerequisites[1]} #{f.name}"
  end

  desc "all images"
  task :all => IMAGES

end
