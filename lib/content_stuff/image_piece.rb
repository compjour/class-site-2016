require 'lib/content_stuff/content_piece'
module ContentStuff
  class ImagePiece < ContentPiece
    def initialize(obj)
      super(obj)
      @src = obj.src
      @kind = :image  #??
    end
  end
end
