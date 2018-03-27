print("munge_md.py has loaded..")

# this global causes some strange doings with AWS lambda
# consider making changes to the lambda function to flush things out
global md_to_html
def md_to_html(mdfile, fragments):
    
    '''
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
    
    class FreshEyesRenderer(Renderer):
        def section_marker(self):
            return '</div>\n<div class="section">'
    
            
    class FreshEyesInlineLexer(InlineLexer):
        def enable_fresh_eyes(self):
            # add section_marker rules
            self.rules.section_marker = re.compile(
                r'\[\[section'                   # [[
                r'|([\s\S]+?)'   # Page 2|Page 2
                r'\]\](?!\])'             # ]]
            )

            # Add section_marker parser to default rules
            # you can insert it some place you like
            # but place matters, maybe 3 is not good
            self.default_rules.insert(3, 'section_marker')

        def output_section_marker(self, m):
            return self.renderer.section_marker()    
    
    renderer = FreshEyesRenderer()
    inline = FreshEyesInlineLexer(renderer)
    inline.enable_fresh_eyes() # enable the feature
    markdown = Markdown(renderer, inline=inline)

    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
