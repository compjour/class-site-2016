module GeneralHelpers
  module BannerHelpers
    def page_banner
      _current_page_data.banner
    end

    def page_banner?  # should this go in page_data_helpers?
      if page_banner.blank?
        return false
      else
        return true
      end
    end

    def page_banner_type
      if page_banner.image.present?
        return :image
      elsif page_banner.iframe.present?
        return :iframe
      else
        raise StandardError, "Banner must be either :image or :iframe"
      end
    end

    def page_banner_data
      btype = page_banner_type
      h = Hashie::Mash.new(banner_type: btype)
      case btype
      when :image
        h.merge!(
          :image_url => page_banner.image.url,
          :caption => page_banner.image.caption,
          :source_name => page_banner.image.source_name,
          :source_url => page_banner.image.source_url
        )
      when :iframe
        h.merge!(
          :iframe_url => page_banner.iframe.url,
          :source_name => page_banner.iframe.source_name,
          :source_url => page_banner.iframe.source_url,
          :caption => page_banner.iframe.caption
        )
        h[:width] = page_banner.iframe.width || nil
      end

      return h
    end


  end
end
