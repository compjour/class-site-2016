require 'addressable/uri'

module GeneralHelpers
  # helpers for common meta attributes
  module MetadataHelpers

    def meta_author
      page_author || site_author
    end

    def meta_description
      (page_description || site_description).strip
    end

    def meta_image_url
      if page_image_url.present?
        _m = Addressable::URI.parse(page_image_url)
        m_url = _m.relative? ? Addressable::URI.join(site_baseurl, _m) : _m
      else
        m_url = site_image_url
      end
      return m_url
    end

    def meta_title
      default_title = site_title
      the_title = ""
      ptitle = page_title
      if ptitle.blank?
        the_title = default_title
      else
        if ptitle != default_title
          the_title = "#{ptitle} | #{default_title}"
        else
          the_title = default_title
        end
      end

      return the_title.strip
    end

    def meta_url
        Addressable::URI.join site_baseurl, page_url
    end

  end
end
