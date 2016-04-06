require 'lib/uniform_content_resource/base_resource'
require 'lib/uniform_content_resource/middleman_content_resource'
require 'lib/uniform_content_resource/uniform_content_resource_error'

module UniformContentResource

end



def UniformContentResource(obj)
  if obj.is_a?(Hash)
    UniformContentResource::BaseResource.new(obj)
  elsif obj.is_a?(Middleman::Sitemap::Resource)
    # if obj.path =~ /\/assignments\//
    #     UniformContentResource::AssignmentResource.new(obj)
    # else
        UniformContentResource::MiddlemanContentResource.new(obj) ## fix
    # end
  elsif obj.is_a?(UniformContentResource::BaseResource)
    obj
  else
    raise UniformContentResource::IncompatibleObjectError, "obj needs to be a Hash or UniformContentResource. Not a #{obj.class}"
  end
end
