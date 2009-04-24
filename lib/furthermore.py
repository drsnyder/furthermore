import os
import sys
import re
import markdown
import yaml
from collections import defaultdict
from mako.template import Template


# html = markdown.markdown(text, ['codehilite(force_linenos=True)'])

POST_DIR = "posts"
VALID_POST_FILE = "(\d{4})(\d{2})(\d{2})-(.*)\.markdown"


def get_posts(dir="%s/.." % os.path.dirname(__file__)):
    posts = os.listdir("%s/%s/" % (dir, POST_DIR))
    posts = filter(lambda x: re.match(VALID_POST_FILE, x) != None, posts)
    posts.sort()
    return posts

def get_post_meta(post_file_name):
    meta = re.match(VALID_POST_FILE, post_file_name)
    #        year           month         day             title
    return (meta.group(1), meta.group(2), meta.group(3), meta.group(4))


def parse_post(post, dir="%s/.." % os.path.dirname(__file__)):
    data = open("%s/%s/%s" % (dir, POST_DIR, post), "r").read()
    matches = re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL)
    post = matches.group(2)
    header = yaml.load(matches.group(1))
    return (header, post)


def write_post(post, outdir=None, dir="%s/.." % os.path.dirname(__file__)):
    if outdir == None:
        outdir = "%s/out" % dir

    if os.path.isdir(outdir) == False:
        os.makedirs(outdir)


def get_template(dir, template):
    return Template(filename="%s/%s.html" % (dir, template))


def render_post(post, properties=defaultdict(str), \
        template_dir="%s/../templates" % os.path.dirname(__file__)):
    # seems like we need some kind of post object
    (header, content) = parse_post(post)
    if not header['layout']:
        header['layout'] = "post"

    template = get_template(template_dir, header['layout'])
    content = markdown.markdown(content, ['codehilite(force_linenos=True)'])
    return template.render(content=content, title=header['title'])

