print("munge_md.py has loaded..")

# this global causes some strange doings with AWS lambda
# consider making changes to the lambda function to flush things out
global md_to_html
def md_to_html(mdfile, fragments):
        
    class FreshEyesRenderer(Renderer):
        def section_marker(self, cls):
            return '</div><div class="c-item-v2__section {}">'.format(cls)
    
            
    class FreshEyesInlineLexer(InlineLexer):
        def enable_fresh_eyes(self):
            # add section_marker rules
            self.rules.section_marker = re.compile( r'\[\[section\|([\s\S]+?)\]\]' )
            self.default_rules.insert(3, 'section_marker')

        def output_section_marker(self, m):
            stuff = m.group(1)
            return self.renderer.section_marker(stuff)
    
    
    
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
    
    
