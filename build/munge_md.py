print("munge_md.py has loaded")


global md_to_html
def md_to_html(mdfile, fragments):

    class FreshEyesRenderer(mistune.Renderer):
        def image(self, src, title, alt_text):
            return '<img style="width: auto;" src="{}" alt="{}" title="{}">'.format(src, title, alt_text)
    
    renderer = FreshEyesRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    
    f = fragments['head'] 
    f += markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret
    
    
