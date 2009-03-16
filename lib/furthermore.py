import os
import sys
import re

POST_DIR = "posts"
VALID_POST = ".*\.textile$"

def get_posts():
    posts = os.listdir("%s/../%s/" % (os.path.dirname(__file__), POST_DIR))
    posts = filter(lambda x: re.match(VALID_POST, x) != None, posts)
    posts.sort()
    return posts
