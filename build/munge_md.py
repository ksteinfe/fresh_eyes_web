print("munge_md.py has loaded")


def md_to_html(mdfile):
    f = "head"  
    f += mistune.markdown(mdfile)
    # for line in mdfile: f += line
    f += "foot"
    
    
    return io.StringIO(unicode(f))