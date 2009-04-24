# vim: ft=python
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


    def testparse_post(self):
        """ split post into yaml header and post rest """
        (header, content) = furthermore.parse_post(furthermore.get_posts().pop())
        self.assertTrue(header.has_key('layout'))
        self.assertTrue(header.has_key('title'))
        self.assertTrue(re.search("Some text", content))

    def testrender_post(self):
        test = furthermore.render_post(furthermore.get_posts().pop())
        self.assertTrue(len(test) > 0)
        self.assertTrue(re.search("My second", test))
        self.assertTrue(re.search("codehilite", test))
        
    
    def testget_post_meta(self):
        meta = furthermore.get_post_meta("20090420-my-first-post.markdown")
        (year, month, day, title) = meta
        self.assertEqual(year, "2009")
        self.assertEqual(month, "04")
        self.assertEqual(day, "20")
        self.assertEqual(title, "my-first-post")
        

if __name__ == '__main__':
    unittest.main()
