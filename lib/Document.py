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
VALID_POST_FILE = "(\d{4})(\d{2})(\d{2})-(.*)\.markdown"

def parse(file):
    data = open(file, "r").read()
    matches = re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL)
    text = matches.group(2)
    header = yaml.load(matches.group(1))
    return (header, text)

def get_post_meta(post_file_name):
    meta = re.match(VALID_POST_FILE, os.path.basename(post_file_name))
    print meta
    if meta != None:
        #        year           month         day             slug
        return (meta.group(1), meta.group(2), meta.group(3), meta.group(4))
    else: 
        meta = re.match("[.*\/]*(\w+).html", post_file_name)
        # a file like index.html; just pull off the index
        return (None, None, None, meta.group(1))

def get_template(dir, template):
    template_lookup = TemplateLookup(directories=[dir])
    return Template(filename="%s/%s.html" % (dir, template), lookup=template_lookup)


def get_post_path(post, dir="%s/.." % os.path.dirname(__file__)):
    outdir = "%s/out/%s" % (dir, ARCHIVE_DIR)
    return "%s/%s/%s/%s/" % (outdir, post.year, post.month, post.day)



class Document:

    def __init__(self, file):
        print "processing file '%s'" % file
        self.file = file
        (self.header, self.content) = parse(file)
        (self.year, self.month, self.day, self.slug) = get_post_meta(file)
        if self.day != None:
            self.date = "%04d/%02d/%02d" % (int(self.year), int(self.month), \
                    int(self.day))
        else: 
            self.date = None

        self.url = self.get_url()

        
    def get_url(self):
        if self.day != None:
            return "/%s/%s/%s/%s/%s.html" % (ARCHIVE_DIR, self.year, self.month, \
                    self.day, self.slug)
        else:
            return "/%s" % self.file
        

