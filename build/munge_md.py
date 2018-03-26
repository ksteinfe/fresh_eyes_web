print("munge_md.py has loaded")

global md_to_html
def md_to_html(mdfile, fragments):
    f = fragments['head'] 
    f += mistune.markdown(mdfile)
    # for line in mdfile: f += line
    f += fragments['foot'] 
    
    
    ret = io.StringIO(unicode(f))
    ret.seek(0)
    return ret