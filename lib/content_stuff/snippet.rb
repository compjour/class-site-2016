require 'lib/content_stuff/content_piece'
module ContentStuff
  class Snippet < ContentPiece
    attr_reader :lang, :code_lines, :stdout_lines
    def initialize(obj)
      super(obj)
      @kind = :snippet  #??
      @lang = obj.lang
      @code_lines = nil # []
      @stdout_lines = nil #[]
      @repl_lines = nil

      if obj.repl
        @_is_repl = true
        @repl_lines = []
        obj.repl.each do |r_line|
          d = Hashie::Mash.new({lang: @lang, repl: true})
          # add the command first
          d.text = r_line.cmd
          @repl_lines << d

          if r_line.stdout
             sd = Hashie::Mash.new({lang: 'plaintext', repl: true})
             sd.text = r_line.stdout
             @repl_lines << sd
          end
        end

      else  # standard block/script
        @_is_repl = false
        @code_lines = obj.code.split("\n").map do |line|
          d = Hashie::Mash.new({lang: @lang, repl: false})
          d.text = line
          d
        end

        if obj.stdout
          @stdout_lines = obj.stdout.split("\n").map do |line|
            d =  Hashie::Mash.new({lang: 'plaintext', repl: false})
            d.text = line
            d
          end
        end
       end
    end

    def repl?
      @_is_repl
    end


    def code
      if @code_lines
        @code_lines.map{|x| x.text }.join("\n")
      else
        nil
      end
    end

    def repl
      @repl_lines
    end

    def stdout
      if @stdout_lines
        @stdout_lines.map{|x| x.text }.join("\n")
      else
        nil
      end
    end

  end
end
