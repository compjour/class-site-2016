require "lib/content_stuff/snippet"
require "lib/content_stuff/image_piece"

module ContentStuff
  def ContentPieceFactory(obj)
    if (k = obj[:kind])
      k = k.to_sym
      if k == :snippet
        Snippet.new(obj)
      elsif k == :image
        ImagePiece.new(obj)
      else
        ContentPiece.new(obj)
      end
    else
      ContentPiece.new(obj)
    end
  end
end
