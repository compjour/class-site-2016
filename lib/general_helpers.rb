require 'lib/general_helpers/metadata_helpers'
require 'lib/general_helpers/page_custom_meta_helpers'
require 'lib/general_helpers/page_data_helpers'
require 'lib/general_helpers/site_config_helpers'
require 'lib/general_helpers/markup_helpers'
require 'lib/custom_helpers/asciinema_helper'
require 'lib/custom_helpers/toc_helper'
require 'lib/custom_helpers/card_helpers'


module GeneralHelpers
    include GeneralHelpers::MarkupHelpers
    include GeneralHelpers::MetadataHelpers
    include GeneralHelpers::PageCustomMetaHelpers

    include GeneralHelpers::PageDataHelpers
    include GeneralHelpers::SiteConfigHelpers
    include AsciinemaHelper
    include TocHelper
    include CardHelpers

end
