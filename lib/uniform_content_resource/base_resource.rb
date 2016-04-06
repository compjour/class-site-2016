require "chronic"
require 'hashie'
require 'active_support/core_ext/object/blank'
require 'active_support/core_ext/array/conversions'
require 'addressable'
module UniformContentResource
  class BaseResource
      # TODO: created_at and updated_at need to be aliased to published_at and modified_at?
      attr_reader :title, :description, :created_at, :url, :image_url, :authors, :publisher, :slug
      def initialize(object)
        @data = Hashie::Mash.new(object)
        if @data.url.blank?
          raise URLMissing, "Object needs :url attribute"
        else
          @url = Addressable::URI.parse(@data.url)
        end
        @title = @data.title
        @slug = @data.slug || @url.to_s
        @description = @data.description
        # TODO: Add granularity stuff
        @created_at = @data.created_at.present? ? Chronic.parse(@data.created_at) : nil
        # note: sometimes original creation date is not known
        @image_url = Addressable::URI.parse(@data.image_url) if @data.image_url.present?
        # authors can be either a string or an array of strings
        @authors = if @data.authors && @data.author
          raise ArgumentError.new("Can't specify both :authors and :author attribute")
        elsif @data.authors || @data.author
          Array(@data.authors.present? ? @data.authors : @data.author)
        else
          nil
        end

        @publisher = @data.publisher
      end

      [:title, :description, :created_at, :url, :image_url, :authors, :publisher].each do |att|
        define_method("#{att}?") do
          !self.instance_variable_get("@#{att}").nil?
        end
      end

      module GenericDisplayMethods
        def author?; authors?; end
        def author
          @authors.to_sentence() if authors?
        end

        def date?; !date.nil?; end
        def date
          if updated_at?
            @updated_at
          elsif created_at?
            @created_at
          else
            nil
          end
        end
      end
      include GenericDisplayMethods

      module DecorativeDisplayMethods
        def byline
          bstr = []
          bstr << author
          bstr << publisher

          return bstr.compact.join('; ')
        end

        def byline?
          author? || publisher?
        end
      end
      include DecorativeDisplayMethods

  end
end
