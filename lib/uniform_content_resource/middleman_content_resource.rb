require 'lib/uniform_content_resource/uniform_content_resource'
module UniformContentResource
  class MiddlemanContentResource < UniformContentResource::BaseResource
    attr_reader :middleman_resource, :path
    def initialize(resource)
      @middleman_resource = resource
      @data = Hashie::Mash.new(@middleman_resource.data) # note that super(@data) will also make a new hash...
      @data.url = resource.url
    ####  @data.publisher ||= false # by default, all publishers are just the local site...though TODO, should probably just overwrite :byline method
      if [@data.created_at, @data.published_at, @data.date].compact.length > 1
        raise ArgumentError.new("For resource #{@middleman_resource.path}, more than one kind of creation-time date is specified. Only 1 is allowed.")
      end
      @data.created_at = @data.created_at || @data.published_at || @data.date
      super(@data)
      @slug = @url.to_s.chomp("/")
      @path = resource.path
    end

    def source_file
      @middleman_resource.source_file
    end

    def source_file_size
      File.size(source_file)
    end

    # Implemented in the page_helper for now
    # def nav?
    #   @data.nav.present?
    # end


    # # nav.next is expected to be a string
    # def next_nav
    #   nav.next if nav?
    # end

    # # nav.previous is expected to be a string
    # def previous_nav
    #   nav.previous if nav?
    # end


  end
end
