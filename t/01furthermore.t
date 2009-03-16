# vim: ft=python
import os
import re
import sys
import unittest

sys.path.append("%s/../lib/" % os.path.dirname(__file__))

import furthermore

class TestQueueMon(unittest.TestCase):

    def setUp(self):
        """ no setup necessary """

    def testget_posts(self):
        posts = get_posts()
        self.assertTrue(len(posts) > 0)


    def testsplit_post(self):
        """ split post into yaml header and post rest """
        pass
        

if __name__ == '__main__':
    unittest.main()
