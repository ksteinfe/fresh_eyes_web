print("munge_md.py has loaded..")

# this global causes some strange doings with AWS lambda
# consider making changes to the lambda function to flush things out
global md_to_html
def md_to_html(mdfile, fragments):
    
    """
    parse md metadata
    """
    meta = {}
    meta_delimiter = "---"
    mdlines = [line.strip() for line in mdfile.split('\n')]
    if mdlines[0] == meta_delimiter:
        i = mdlines[1:].index(meta_delimiter)
        if i>0:
            print("stripping meta")
            mdfile = "\n".join(mdlines[i+1:])
            for ln in mdlines[1:i]:
                match = re.search(r'^(\w+):\s*(.+?)$', ln)
                if match:
                    print("found key:{}, val:{}".format(match.group(1), match.group(2)))
                    meta[match.group(1).lower] = match.group(2)
                    
            
            
    
    """
    define custom md parser
    """
    class FreshEyesRenderer(Renderer):
        
        def image(self, src, title, alt_text):
            return '<img src="{}" alt="{}" title="{}" style="width: auto;">'.format(src,alt_text,title)
        
        def section_marker(self):
            return self.section_marker_ex("")

        def section_marker_ex(self, cls):
            return '</div><div class="c-item-v2__section {}">'.format(cls)
            
            
    class FreshEyesInlineLexer(InlineLexer):
        def enable_fresh_eyes(self):
            # add section_marker rules
            self.rules.section_marker_ex = re.compile( r'\[\[section\|([\s\S]+?)\]\]' )
            self.default_rules.insert(3, 'section_marker_ex')
            self.rules.section_marker = re.compile( r'\[\[section\]\]' )
            self.default_rules.insert(3, 'section_marker')

        def output_section_marker_ex(self, m):
            return self.renderer.section_marker_ex(m.group(1))
    
        def output_section_marker(self, m):
            return self.renderer.section_marker()    
    
    renderer = FreshEyesRenderer()
    inline = FreshEyesInlineLexer(renderer)
    inline.enable_fresh_eyes() # enable the feature
    markdown = Markdown(renderer, inline=inline)
    
    
    """
    parse md and assemble html
    """
    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
