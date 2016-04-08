require 'addressable'
module UniformContentResource
  module UniformContentResourceHelpers

    # TODOTODO TKTK
    # needs access to `sitemap`, which is why it's a helper
    # but someday I will learn how to make a proper Middleman plugin
    def sitemap_resources
      sitemap.resources
    end

  # def sitemap_content_resources
  #   sitemap.resources.select{ |r|
  #     r.path =~ /^(?:guides|articles|assignments)\/.+/ && r.data.title.present?
  #   }.map{ |r| uniform_content_resource_adapter(r)
  #   }.sort_by{ |r| r.title }
  # end

    def find_sitemap_resource_by_relative_url(relative_url)
      rel_url = relative_url.to_s
      rel_url += '/' unless rel_url[-1] == '/'
      r = sitemap_resources.find{|p| p.url == rel_url }

      return r
    end

    # used to handle resources that could be either UniformContentResources or MiddlemanResources
    def uniform_content_resource_adapter(obj)
      if obj.is_a?(String)
        url = Addressable::URI.parse(obj)
        if url.relative? ## assume it is a Middleman resource
          xo = find_sitemap_resource_by_relative_url(url)
          if xo.blank?
            raise ::CannotFindMiddlemanResourceBySlugError.new(url)
          end
        else
          xo = {:url => url, :title => url.to_s }
        end
      else
        xo = obj
      end

      return UniformContentResource(xo)
    end


    def link_to_content_resource(obj, opts = {})
      ucrobj = uniform_content_resource_adapter(obj)
      _title = opts[:title] || ucrobj.title
      link_to _title, ucrobj.url, opts
    end

    alias_method :link_cro, :link_to_content_resource

    def content_resource_element(obj, tag = :div, opts = {})
      opts[:class] = [opts[:class], "uniform-content-resource"].compact.join(' ')
      ucrobj = uniform_content_resource_adapter(obj)
      buff = ActiveSupport::SafeBuffer.new
      content_tag(:div, opts.merge("data-href" => ucrobj.url)) do
        buff.safe_concat link_to_content_resource(ucrobj, :class => 'title')
        if ucrobj.description?
          buff.safe_concat content_tag(:div, ucrobj.description, :class => 'description')
        end

        buff
      end
    end
  end
end


class CannotFindMiddlemanResourceBySlugError < StandardError; end;
