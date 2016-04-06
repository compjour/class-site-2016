module CustomHelpers
  module AsciinemaHelper
    def asciinema_player(filename, poster_text = '', options = {})
      filename_id = filename.gsub(/\W/, '_').strip()
      opts = Hashie::Mash.new(options)
      opts['autoPlay'] ||= false
      opts['loop'] ||= false
      opts['speed'] ||= 1
      opts['theme'] ||= 'monokai'
      opts['fontSize'] ||= '1rem'
      opts['height'] ||= 20
      if poster_text.present?
        opts['poster'] = "data:text/plain," + poster_text
      end

      %Q{
  <div class="asciinema-wrap">
    <div id="#{filename_id}"></div>
    <script>
      asciinema_player.core.CreatePlayer(
              '#{filename_id}', '#{filename}',
              #{opts.to_json}
            );
    </script>
  </div>
      }
    end
  end

end
