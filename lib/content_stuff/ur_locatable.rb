require 'active_support/concern'

module ContentStuff
  module URLocatable
    extend ActiveSupport::Concern
    included do
      attr_reader :url
    end

    # class_methods do
    #   def initialize(obj)
    #     @url = obj[:url]
    #   end
    # end
  end
end
