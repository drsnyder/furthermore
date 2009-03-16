import os
import sys
import re

POST_DIR = "posts"
VALID_POST_FILE = ".*\.textile$"

def get_posts():
    posts = os.listdir("%s/../%s/" % (os.path.dirname(__file__), POST_DIR))
    posts = filter(lambda x: re.match(VALID_POST_FILE, x) != None, posts)
    posts.sort()
    return posts

def parse_post(post):
    data = open("%s/../%s/%s" % (os.path.dirname(__file__), POST_DIR, post), "r").read()
    return tuple(re.match(r"(.*)\.\.\.(.*)", data, re.MULTILINE|re.DOTALL).group(1,2))


