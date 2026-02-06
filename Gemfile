# frozen_string_literal: true
source "https://rubygems.org"

# This is the default theme for new Jekyll sites.
gem "minima"

# Added for GitHub Pages compatibility
gem "github-pages", group: :jekyll_plugins

# Additional plugins
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
platforms :mingw, :x64_mingw, :mswin, :noko_gumbo do
  gem "wdm", "~> 0.1.1", :require => false
end