module GeneralHelpers
  # helpers for common meta attributes
  module SiteConfigHelpers
    def site_config
      config[:site_config]
    end

    def site_author
      site_config[:author]
    end

    def site_baseurl
      site_config[:baseurl]
    end

    def site_description
      site_config[:description]
    end

    def site_image_url
      site_config[:image_url]
    end

    def site_title
      site_config[:title]
    end

    def site_services(service_slug)
      site_config.services[service_slug] if site_config.services
    end

    ### begin helpers for site services
    ## TODO: make it more meta
    def site_google_analytics_id
      t = site_services(:google_analytics)
      return t.id if t.present?
    end

    def site_google_custom_search_id
      t = site_services(:google_custom_search)
      return t.id if t.present?
    end


  end
end
