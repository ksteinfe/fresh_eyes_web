print("munge_md.py has loaded")


class FreshEyesRenderer(mistune.Renderer):
    
    def image(src, title, alt_text)
        return '<img style="width: auto;" src="{}" alt="{}" title="{}">'.format(src, title, alt_text)


global md_to_html
def md_to_html(mdfile, fragments):
    
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
    
    
