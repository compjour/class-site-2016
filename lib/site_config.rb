require 'yaml'
require 'hashie'


module SiteConfig
  def self.load_site_config(config_path)
    ::Hashie::Mash.new(YAML.load_file(config_path))
  end
end
