# Special config
require "lib/general_helpers"
require "lib/site_config"
helpers GeneralHelpers
config[:site_config] = SiteConfig.load_site_config("./site_config.yaml")



# General configuration

# Reload the browser automatically whenever files change


activate :directory_indexes
activate :pry
activate :syntax, :line_numbers => false
set :trailing_slash, true

set :js_dir, 'assets/javascripts'
set :css_dir, 'assets/stylesheets'
set :images_dir, 'assets/images'

# Build-specific configuration
configure :build do
  # Minify CSS on build
  activate :minify_css
  # Minify Javascript on build
  activate :minify_javascript
end


configure :development do
  activate :livereload
end
###
# Page options, layouts, aliases and proxies
###

# Per-page layout changes:
#
# With no layout
page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false
page '/*.csv', layout: false
page '/slides', layout: '/layouts/slides'
set :layout, :default_page_layout



# Proxy pages (http://middlemanapp.com/basics/dynamic-pages/)
# proxy "/this-page-has-no-template.html", "/template-file.html", locals: {
#  which_fake_page: "Rendering a fake page with a local variable" }



activate :s3_sync do |s3_sync|
  s3_sync.delete                     = false
  s3_sync.after_build                = true
  s3_sync.prefer_gzip                = true
  s3_sync.path_style                 = true
  s3_sync.reduced_redundancy_storage = false
  s3_sync.acl                        = 'public-read'
  s3_sync.encryption                 = false
  s3_sync.version_bucket             = false
  s3_sync.index_document             = 'index.html'
  s3_sync.error_document             = '404.html'
end
