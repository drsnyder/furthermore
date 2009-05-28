# vim: set expandtab textwidth=79 ts=4 sts=4 ft=python:
import os
import re
import sys
import yaml
import unittest

sys.path.append("%s/../lib/" % os.path.dirname(__file__))

import furthermore

class TestQueueMon(unittest.TestCase):

    def setUp(self):
        """ no setup necessary """


    def testget_posts(self):
        posts = furthermore.get_posts()
        self.assertTrue(len(posts) > 0)

        post = posts.pop()
        self.assertTrue(post.year > 0)
        self.assertTrue(post.month > 0)
        self.assertTrue(post.day > 0)
        self.assertTrue(len(post.date) > 0)
        self.assertTrue(len(post.slug) > 0)
        self.assertTrue(len(post.content) > 0)
        self.assertTrue(len(post.html) > 0)
        self.assertTrue(len(post.url) > 0)
        self.assertTrue(hasattr(post, 'header'))


    def testwrite_post(self):
        pass



    def testparse_post(self):
        """ split post into yaml header and post rest """
        (header, content) = furthermore.parse_post(furthermore.get_posts().pop())
        self.assertTrue(header.has_key('layout'))
        self.assertTrue(header.has_key('title'))
        self.assertTrue(re.search("Some text", content))


    def testget_post_meta(self):
        meta = furthermore.get_post_meta("20090420-my-first-post.markdown")
        (year, month, day, title) = meta
        self.assertEqual(year, "2009")
        self.assertEqual(month, "04")
        self.assertEqual(day, "20")
        self.assertEqual(title, "my-first-post")


    def testrender_post(self):
        test = furthermore.render_post(furthermore.get_posts().pop())
        self.assertTrue(len(test) > 0)
        self.assertTrue(re.search("A post with pygments", test))
        self.assertTrue(re.search("codehilite", test))

    def testwrite_post(self):
        post = furthermore.get_posts().pop()
        furthermore.write_post(post)
        file = "%s/../out/archives/%s/%s/%s/%s.html" \
                % (os.path.dirname(__file__), post.year, \
                post.month, post.day, post.slug)
        self.assertTrue(os.path.isfile(file))

    ##########################################################
    def testparse_document_file(self):
        file = "%s/../posts/20090410-my-first-post.markdown" \
                % os.path.dirname(__file__)
        (header, content) = furthermore.parse_document_file(file)
        self.assertTrue(header.has_key('layout'))
        self.assertTrue(header.has_key('title'))
        self.assertTrue(re.search("Some text", content))

    def testrender_document(self):
        file = "%s/../posts/20090410-my-first-post.markdown" \
                % os.path.dirname(__file__)
        (header, content) = furthermore.parse_document_file(file)
        text = furthermore.render_document(header, content)
    
        

if __name__ == '__main__':
    unittest.main()
