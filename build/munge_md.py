print("munge_md.py has loaded")

global md_to_html
def md_to_html(mdfile, fragments):
    
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

            # Add wiki_link parser to default rules you can insert it some place you like but place matters, maybe 3 is not good
            self.default_rules.insert(0, 'wiki_link')

        def output_wiki_link(self, m):
            text = m.group(1)
            alt, link = text.split('|')
            # you can create an custom render
            # you can also return the html if you like
            return self.renderer.wiki_link(alt, link)
    
    renderer = WikiLinkRenderer()
    inline = WikiLinkInlineLexer(renderer=renderer)
    # enable the feature
    inline.enable_wiki_link()
    markdown = mistune.Markdown(renderer=renderer, inline=inline)
    
    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
