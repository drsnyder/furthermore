# vim: set expandtab textwidth=79 ts=4 sts=4 ft=python:
import os
import sys
import re
import markdown
import yaml
from Document import Document
from collections import defaultdict
from mako.template import Template


# html = markdown.markdown(text, ['codehilite(force_linenos=True)'])

POST_DIR = "posts"
ARCHIVE_DIR = "archives"
VALID_POST_FILE = "(\d{4})(\d{2})(\d{2})-(.*)\.markdown"


def parse_document_file(file):
    data = open(file, "r").read()
    matches = re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL)
    text = matches.group(2)
    header = yaml.load(matches.group(1))
    return (header, text)


def render_document(header, content, template_dir="%s/../templates" % os.path.dirname(__file__)):
    # seems like we need some kind of post object
    if not header['layout']:
        header['layout'] = "post"

    template = get_template(template_dir, header['layout'])
    content = markdown.markdown(content, ['codehilite(force_linenos=True)'])
    return template.render(content=content, title=header['title'])

############################################
def get_posts(dir="%s/.." % os.path.dirname(__file__)):
    post_files = os.listdir("%s/%s/" % (dir, POST_DIR))
    post_files = filter(lambda x: re.match(VALID_POST_FILE, x) != None, post_files)
    post_files.sort()

    posts = []
    for file in post_files:
        post = Document()
        post.filename = file
        (post.year, post.month, post.day, post.slug) = get_post_meta(file)
        (post.header, post.content) = parse_post(post)
        post.html = render_post(post)

        posts.append(post)

    return posts


def get_post_meta(post_file_name):
    meta = re.match(VALID_POST_FILE, post_file_name)
    #        year           month         day             slug
    return (meta.group(1), meta.group(2), meta.group(3), meta.group(4))


def parse_post(post, dir="%s/.." % os.path.dirname(__file__)):
    data = open("%s/%s/%s" % (dir, POST_DIR, post.filename), "r").read()
    matches = re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL)
    text = matches.group(2)
    header = yaml.load(matches.group(1))
    return (header, text)


def get_template(dir, template):
    return Template(filename="%s/%s.html" % (dir, template))


def render_post(post, properties=defaultdict(str), \
        template_dir="%s/../templates" % os.path.dirname(__file__)):


    if not post.header.has_key('layout'):
        layout = "post"
    else:
        layout = post.header['layout']

    if not post.header.has_key('title'):
        title = ""
    else:
        title = post.header['title']

    template = get_template(template_dir, layout)
    content = markdown.markdown(post.content, ['codehilite(force_linenos=True)'])
    return template.render(content=content, title=title)


def get_post_path(post, dir="%s/.." % os.path.dirname(__file__)):
    outdir = "%s/out/%s" % (dir, ARCHIVE_DIR)
    return "%s/%s/%s/%s/" % (outdir, post.year, post.month, post.day)
    

def write_post(post, dir="%s/.." % os.path.dirname(__file__)):
    fullpath = get_post_path(post)
    if os.path.isdir(fullpath) == False:
        os.makedirs(fullpath)

    html = render_post(post)
    fd = open("%s/%s.html" % (fullpath, post.slug), "w")
    ret = fd.write(html)
    fd.close()
