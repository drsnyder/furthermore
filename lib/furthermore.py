import os
import sys
import re
import textile
from collections import defaultdict
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer
from mako.template import Template
from optparse import OptionParser

POST_DIR = "posts"
VALID_POST_FILE = ".*\.textile$"
CODE_PATTERN = re.compile(r'{% highlight (.+?) %}(.+?){% endhighlight %}', re.S)

def replace_code(m):
    try: 
        lexer = get_lexer_by_name(m.group(1))
    except ValueError:
        lexer = TextLexer()

    code = highlight(m.group(2), lexer, HtmlFormatter(noclasses=False))
    code = code.replace('\n\n', '\n&nbsp;\n').replace('\n', '<br />')
    return '\n<notextile><div class="code">%s</div></notextile>\n' % code


def get_posts(dir="%s/.." % os.path.dirname(__file__)):
    posts = os.listdir("%s/%s/" % (dir, POST_DIR))
    posts = filter(lambda x: re.match(VALID_POST_FILE, x) != None, posts)
    posts.sort()
    return posts


def parse_post(post, dir="%s/.." % os.path.dirname(__file__)):
    data = open("%s/%s/%s" % (dir, POST_DIR, post), "r").read()
    return tuple(re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL).group(1,2))

def write_post(data, outdir=None, dir="%s/.." % os.path.dirname(__file__)):
    if outdir == None:
        outdir = "%s/out" % dir

    if os.path.isdir(outdir) == False:
        os.makedirs(outdir)

    return


def render_post(post, properties=defaultdict(str)):     
    # seems like we need some kind of post object
    (header, content) = parse_post(post)
    for (k, v) in header.iteritems():
        properties[k] = v

    data = CODE_PATTERN.sub(replace_code, content)
    mytemplate = Template(filename='post.html')
    properties['content'] = textile.textile(content)
    return mytemplate.render(properties)

    

