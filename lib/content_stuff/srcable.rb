require 'active_support/concern'

module ContentStuff
  module SRCable
    extend ActiveSupport::Concern
    included do
      attr_reader :src # need to hook into initialize lifesycle
    end
  end
end
