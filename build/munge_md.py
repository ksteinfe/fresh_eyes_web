print("munge_md.py has loaded")

global md_to_html
def md_to_html(mdfile, fragments):
    
    '''
    class FreshEyesRenderer(mistune.Renderer):
        def image(self, src, title, alt_text):
            return '<img style="width: auto;" src="{}" alt="{}" title="{}">'.format(src, title, alt_text)
    '''
    
    class EmojiRenderer(object):
        def emoji(self, text):
            return "<emoji>%s</emoji>" % text

    class EmojiInlineLexer(mistune.InlineLexer):
        def __init__(self, **kwargs):
            super(EmojiInlineLexer, self).__init__(**kwargs)
            self.default_rules.insert(0, "emoji")
            self.rules.emoji = re.compile(r'^:([a-zA-Z0-9\+\-_]+):', re.I)

        def output_emoji(self, m):
            text = self.output(m.group(1))
            return self.renderer.emoji(text)


    class MarkdownRenderer(mistune.Renderer, EmojiRenderer):
        def __init__(self, **kwargs):
            super(MarkdownRenderer, self).__init__(**kwargs)
    
    
    renderer = MarkdownRenderer()
    inline = EmojiInlineLexer(renderer=renderer)
    markdown = mistune.Markdown(renderer=renderer, inline=inline)
    
    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
