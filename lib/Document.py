# vim: set expandtab tw=79 ts=4 sts=4 ft=python:
import os
import sys
import re
import markdown
import yaml
from collections import defaultdict
from mako.template import Template
from mako.lookup import TemplateLookup

POST_DIR = "posts"
ARCHIVE_DIR = "archives"
VALID_POST_FILE = "(\d{4})(\d{2})(\d{2})-(.*)\.(\w+)$"

def parse(file):
    data = open(file, "r").read()
    matches = re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL)
    text = matches.group(2)
    header = yaml.load(matches.group(1))
    return (header, text)

def get_post_meta(post_file_name):
    meta = re.match(VALID_POST_FILE, os.path.basename(post_file_name))
    if meta != None:
        #        year           month         day             slug
        return (meta.group(1), meta.group(2), meta.group(3), meta.group(4),\
                meta.group(5)) # type
    else: 
        meta = re.match("(\w+).(.*)", os.path.basename(post_file_name))
        # a file like index.html; just pull off the index
        return (None, None, None, meta.group(1), meta.group(2))

def get_template(dir, template):
    template_lookup = TemplateLookup(directories=[dir])
    return Template(filename="%s/%s.html" % (dir, template), lookup=template_lookup)


class Document:

    def __init__(self, file, properties=defaultdict(str), \
            template_dir="%s/../templates" % os.path.dirname(__file__), \
            outdir="%s/../www" % os.path.dirname(__file__)):
        self.file = file
        self.template_dir = template_dir
        (self.header, self.content) = parse(file)
        (self.year, self.month, self.day, self.slug, self.type) = get_post_meta(file)
        if self.day != None:
            self.date = "%04d/%02d/%02d" % (int(self.year), int(self.month), \
                    int(self.day))
        else: 
            self.date = None

        self.url = self.get_url()
        self.properties = properties
        self.outdir = outdir


        self.layout = not self.header.has_key('layout') and "post" \
                or self.header['layout']
        self.title = not self.header.has_key('title') and "" \
                or self.header['title']

        
    def get_url(self):
        if self.day != None:
            return "/%s/%s/%s/%s/%s.html" % (ARCHIVE_DIR, self.year, self.month, \
                    self.day, self.slug)
        else:
            return "/%s" % self.file

    def get_path(self, dir=None):
        if dir == None:
            dir = self.outdir

        if self.day != None:
            outdir = "%s/%s" % (dir, ARCHIVE_DIR)
            return "%s/%s/%s/%s/" % (outdir, self.year, self.month, self.day)
        else:
            outdir = "%s/" % dir
            

    def render(self, template_dir=None):
        if template_dir == None:
            template_dir = self.template_dir

        pre_pass_template = Template(self.content)
        pre_pass_content = pre_pass_template.render(properties=self.properties)

        if self.type == "markdown":
            template = get_template(template_dir, self.layout)
            content = markdown.markdown(self.content, ['codehilite(force_linenos=True)'])
        elif self.type == "html":
            content = self.content
        else:
            raise InvalidDocumentType

        self.html = template.render(content=content, title=self.title, \
                template_dir=template_dir, properties=self.properties)
        return self.html


    def write(self, outdir=None):
        if outdir == None:
            outdir = self.outdir

        fullpath = self.get_path(outdir)

        if os.path.isdir(fullpath) == False:
            os.makedirs(fullpath)

        html = self.render()
        fd = open("%s/%s.html" % (fullpath, self.slug), "w")
        ret = fd.write(html)
        fd.close()



class InvalidDocumentType(Exception):
    """
    Raised in the the render method when an invalid document extension is
    encountered.
    """
    pass

