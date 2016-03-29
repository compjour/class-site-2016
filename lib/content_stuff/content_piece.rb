require 'hashie'
require 'lib/content_stuff/ur_locatable'
module ContentStuff
  class ContentPiece
    include URLocatable
    attr_reader :title, :description, :kind, :text
    def initialize(obj)
      @title = obj[:title]
      @description = obj[:description]
      @url = obj[:url] #TK should be in URLocatable
      @kind = (obj[:kind] || :text).to_sym
      @text = obj.text
    end


    def [](some_attr)
      instance_variable_get "@#{some_attr}"
    end
  end
end
