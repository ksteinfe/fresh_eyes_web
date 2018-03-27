print("munge_md.py has loaded")

global md_to_html
def md_to_html(mdfile, fragments):
    
    '''
    class FreshEyesRenderer(mistune.Renderer):
        def image(self, src, title, alt_text):
            return '<img style="width: auto;" src="{}" alt="{}" title="{}">'.format(src, title, alt_text)
    
    
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
    '''
    from mistune import Markdown, Renderer, InlineGrammar, InlineLexer
    
    class WikiLinkRenderer(Renderer):
        def wiki_link(self, alt, link):
            return '<a href="%s">%s</a>' % (link, alt)

    class WikiLinkInlineLexer(InlineLexer):
        def enable_wiki_link(self):
            # add wiki_link rules
            self.rules.wiki_link = re.compile(
                r'\[\['                   # [[
                r'([\s\S]+?\|[\s\S]+?)'   # Page 2|Page 2
                r'\]\](?!\])'             # ]]
            )

            # Add wiki_link parser to default rules
            # you can insert it some place you like
            # but place matters, maybe 3 is not good
            self.default_rules.insert(3, 'wiki_link')

        def output_wiki_link(self, m):
            text = m.group(1)
            alt, link = text.split('|')
            # you can create an custom render
            # you can also return the html if you like
            return self.renderer.wiki_link(alt, link)
    
    
    '''
    renderer = MarkdownRenderer()
    inline = EmojiInlineLexer(renderer=renderer)
    markdown = mistune.Markdown(renderer=renderer, inline=inline)
    '''
    
    renderer = WikiLinkRenderer()
    inline = WikiLinkInlineLexer(renderer)
    # enable the feature
    inline.enable_wiki_link()
    markdown = Markdown(renderer, inline=inline)
    
    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
