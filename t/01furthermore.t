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
        header_config = yaml.load(header)
        self.assertTrue(header_config.has_key('layout'))
        self.assertTrue(header_config.has_key('title'))

        

if __name__ == '__main__':
    unittest.main()
