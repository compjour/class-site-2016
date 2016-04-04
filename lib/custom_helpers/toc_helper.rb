module TocHelper
  def render_toc(opts = {})
    partial "/layouts/partials/components/toc", locals: opts
  end
end
