require 'lib/content_stuff/content_piece'
require 'lib/content_stuff/content_piece_factory'
module ContentStuff
  class Recipe < ContentCollection
    attr_reader :chapter, :book
    def initialize(obj)
      super(obj)
      @chapter = obj.chapter
      @book = obj.book
    end
  end
end
