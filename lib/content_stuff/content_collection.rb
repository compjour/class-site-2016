require 'lib/content_stuff/content_piece'
require 'lib/content_stuff/content_piece_factory'
module ContentStuff
  class ContentCollection < ContentPiece
    attr_reader :lede
    def initialize(obj)
      super(obj)
      @lede = ContentPieceFactory(obj.lede)
      @_content = []
      Array(obj.content).each do |c|
        @_content << ContentPieceFactory(c)
      end
    end


    def content
      @_content
    end
  end
end
