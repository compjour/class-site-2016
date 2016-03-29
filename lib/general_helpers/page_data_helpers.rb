require 'hashie'

module GeneralHelpers
  # helpers for common page attributes
  # should also deal with dynamic pages...
  module PageDataHelpers

    def page_data_attr(attr_name)
      _dynamic_page_data[attr_name] || _current_page_data[attr_name]
    end

    # for dynamic pages, we expect the option :dynamic_page has been set
    # (holdover from middleman-onthestreet gem)
    def _dynamic_page_data
      local_opts = current_page.metadata[:locals]
      local_opts[:dynamic_data_object] ||= Hashie::Mash.new
      return local_opts[:dynamic_data_object]
    end

    def _current_page_data
      current_page.data
    end

    def page_author
      page_data_attr(:author)
    end

    def page_description
      page_data_attr(:description)
    end

    def page_class
      if (cp = page_data_attr(:page_class))
        return "page page-#{cp}"
      else
        return "page"
      end
    end

    def page_image_url
      page_data_attr(:image_url)
    end

    def page_has_header_class
      hh = page_data_attr(:has_header)
      if hh == false
         return "no-header"
      else
        return "has-header"
      end
    end

    def page_summary
      page_data_attr(:summary)
    end

    def page_url
      page_data_attr(:url) || 'http://www.example.com/'
    end

    def page_title
      page_data_attr(:title)
    end


  end
end
