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

    def testrender_post(self):
        test = furthermore.render_post(furthermore.get_posts().pop())
        self.assertTrue(len(test) > 0)
        self.assertTrue(re.search("A post with", test))
        self.assertTrue(re.search("codehilite", test))
        
        

if __name__ == '__main__':
    unittest.main()
