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
            #print("stripping meta")
            mdfile = "\n".join(mdlines[i+2:])
            for ln in mdlines[1:i+1]:
                match = re.search(r'^(\w+):\s*(.+?)$', ln)
                if match:
                    #print("found key:{}, val:{}".format(match.group(1), match.group(2)))
                    meta[match.group(1).lower()] = match.group(2)
                    
            
    #pp = pprint.PrettyPrinter(indent=4)
    #print(pp.pformat(meta))        
    
    """
    define custom md parser
    """
    class FreshEyesRenderer(Renderer):
        
        
        def image(self, src, title, alt_text):
            video_extensions = ['mp4', 'm4v', 'ogv', 'webm', 'mpg', 'mpeg']
            file_extension = os.path.splitext(src)[1][1:]
            if any([src.endswith(ext) for ext in video_extensions]):
                """
                handling videos
                """
                try:
                    args = alt_text.split('|')
                    cls = args[1].strip()
                    vid_atts = args[2].strip()
                    ht = '<figure class="{0}"><video {1}><source src="{2}" type="video/{3}"></video><figcaption>{4}</figcaption></figure>'
                    return ht.format(cls,vid_atts,src,file_extension,title)
                except:
                    ht = '<figure class="{0}"><video loop muted><source src="{1}" type="video/{2}"></video><figcaption>{3}</figcaption></figure>'
                    return ht.format(alt_text,src,file_extension,title)
            else:
                """
                handling images
                """            
                # we use alt_text to carry class information, titles are always used as alt text
                if "|" in alt_text:
                    args = alt_text.split('|')
                    args = [a.strip().lower() for a in args]
                    
                    if args[0] == "scroll":
                        """
                        scrolling background
                        scroll | img_width | img_height | frame_height | scroll_time
                        """                    
                        try:
                            img_width, img_height, frame_height, scroll_time = args[1], args[2], args[3], args[4]
                            ht = '<figure><div class="scroll-wrapper" style="height: {3}px"><div style="margin: auto; width: {1}px; height: {2}px;  background: url({0}) repeat 0 0; background-position: 0 -{2}px; -webkit-animation: background-scroller {4}s linear infinite;"></div></div><figcaption>{5}</figcaption></figure>'
                            return ht.format(src, img_width, img_height, frame_height, scroll_time, title)
                        except: 
                            return '<span class="parse-error"> error parsing scrolling background image. format is: scroll | img_width | img_height | frame_height | scroll_time </span>'
                        
                    else:
                        """
                        we assume a standard figure for now
                        first argument = fig
                        """
                        cls = args[1]
                        ht = '<figure class="{0}"><img src="img/veil.gif" data-src="{1}" alt="" /><figcaption>{2}</figcaption></figure>'
                        return ht.format(cls,src,title)
                
                return '<img src="{0}" class="{1}" alt="{2}" title="{2}" style="width: auto;">'.format(src,alt_text,title)
        
        def header(self, text, level, raw=None):
            if level==1:
                return '</div></div></div><div class="slide major_heading js--press-slack"><span>{}</span></div><div class="container"><div class="row"><div class="col-12">'.format(raw)
            return '<h{0}>{1}</h{0}>'.format(level-1, raw)
        
        def section_marker(self):
            return self.section_marker_ex("")

        def section_marker_ex(self, cls):
            return '</div></div><div class="row {}"><div class="col-12">'.format(cls)
            
        def aside_marker(self,content):
            return '<span class="aside">{}</span>'.format(content)
            
    class FreshEyesInlineLexer(InlineLexer):
        def enable_fresh_eyes(self):
            # add section_marker rules
            self.rules.section_marker_ex = re.compile( r'\[\[section\|([\s\S]+?)\]\]' )
            self.default_rules.insert(3, 'section_marker_ex')
            self.rules.section_marker = re.compile( r'\[\[section\]\]' )
            self.default_rules.insert(3, 'section_marker')
            
            # add aside rules 
            self.rules.aside_marker = re.compile( r'\(\((.*?)\)\)' )
            self.default_rules.insert(0, 'aside_marker')

        def output_section_marker_ex(self, m):
            return self.renderer.section_marker_ex(m.group(1))
    
        def output_section_marker(self, m):
            return self.renderer.section_marker()    
            
        def output_aside_marker(self, m):
            return self.renderer.aside_marker(m.group(1))                
    
    renderer = FreshEyesRenderer()
    inline = FreshEyesInlineLexer(renderer)
    inline.enable_fresh_eyes() # enable the feature
    markdown = Markdown(renderer, inline=inline)
    
    
    """
    assemble html head
    """
    html = fragments['head']
    
    if 'title' in meta:
        content = ""
        if 'keystone' in meta: content+= '<img src="{}" class="keystone" alt="keystone image">'.format(meta['keystone'])

        content += '<h1>{}</h1>'.format(meta['title'])
        if 'subtitle' in meta: content += '<h2>{}</h2>'.format(meta['subtitle'])
        if 'attribution' in meta: content += '<p>{}</p>'.format(meta['attribution'])    
        html += fragments['start_content_meta'].replace('{{content}}',content)
    else:
        #print("no metadata")
        html += fragments['start_content_nometa']
    
    """
    assemble html body
    """
    html += markdown(mdfile)
    
    
    """
    assemble html foot
    """
    if 'copyright' not in meta: meta['copyright'] = ""
    
    html += fragments['foot'].replace('{{copyright}}',meta['copyright'])
    
    
    def replace_non_ascii(text):
        return ''.join([i if ord(i) < 128 else '<span class="non-ascii">NON-ASCII</span>' for i in text])
    
    html = replace_non_ascii(html)
    
    # TODO: filter(lambda x: x in printable, s)
    ret = io.StringIO(unicode(html))
    ret.seek(0)
    return ret
    
    
