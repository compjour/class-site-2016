module UniformContentResource
  class Error < StandardError; end
  class UniformContentResourceError < StandardError; end
  class URLMissing < Error; end
  class PossibleDataEntryError < Error; end
  class IncompatibleObjectError < Error; end
end
