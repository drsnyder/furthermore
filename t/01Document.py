# vim: set expandtab textwidth=79 ts=4 sts=4 ft=python:
import os
import re
import sys
import yaml
import unittest

sys.path.append("%s/../lib/" % os.path.dirname(__file__))

from Document import Document, VALID_POST_FILE, parse, get_post_meta

class TestDocument(unittest.TestCase):

    def setUp(self):
        self.post_files = os.listdir("%s/../%s/" % (os.path.dirname(__file__), "posts"))
        self.post_files = filter(lambda x: re.match(VALID_POST_FILE, x) != None, \
                self.post_files)
        self.post_files.sort()

    def test_init(self):
        post = self.post_files[1]
        p = Document("%s/../posts/%s" % (os.path.dirname(__file__), post))
        self.assertTrue(hasattr(p, 'header'))
        self.assertTrue(hasattr(p, 'content'))
        self.assertTrue(hasattr(p, 'year'))
        self.assertTrue(hasattr(p, 'month'))
        self.assertTrue(hasattr(p, 'day'))
        self.assertTrue(hasattr(p, 'slug'))
        self.assertTrue(hasattr(p, 'url'))

        self.assertTrue(len(p.date) > 0)
        self.assertTrue(len(p.slug) > 0)
        self.assertTrue(len(p.content) > 0)
        self.assertTrue(len(p.url) > 0)

        html = p.render()
        self.assertTrue(len(p.html) > 0)


        p = Document("%s/../index.markdown" % os.path.dirname(__file__))
        self.assertTrue(hasattr(p, 'header'))
        self.assertTrue(hasattr(p, 'content'))
        self.assertTrue(hasattr(p, 'year'))
        self.assertTrue(hasattr(p, 'month'))
        self.assertTrue(hasattr(p, 'day'))
        self.assertTrue(hasattr(p, 'slug'))
        self.assertEquals(p.year, None)
        self.assertEquals(p.month, None)
        self.assertEquals(p.day, None)
        self.assertEquals(p.slug, "index")
        self.assertTrue(len(p.url) > 0)




    def testparse(self):
        """ split post into yaml header and post rest """
        post = self.post_files[1]
        (header, content) = parse("%s/../posts/%s" % \
                (os.path.dirname(__file__), post))
        self.assertTrue(header.has_key('layout'))
        self.assertTrue(header.has_key('title'))
        self.assertTrue(re.search("Some text", content))


    def testget_post_meta(self):
        meta = get_post_meta("20090420-my-first-post.markdown")
        (year, month, day, slug, type) = meta
        self.assertEqual(year, "2009")
        self.assertEqual(month, "04")
        self.assertEqual(day, "20")
        self.assertEqual(slug, "my-first-post")

        meta = get_post_meta("index.html")
        (year, month, day, slug, type) = meta
        self.assertEqual(year, None)
        self.assertEqual(month, None)
        self.assertEqual(day, None)
        self.assertEqual(slug, "index")

    def testget_path(self):
        post = self.post_files[1]
        p = Document("%s/../posts/%s" % (os.path.dirname(__file__), post), \
                outdir="%s/../tmp/www" % os.path.dirname(__file__))
        path = p.get_path()
        self.assertEqual("t/../tmp/www/archives/2009/04/11/", path)

    def testwrite_post(self):
        post = self.post_files[1]
        p = Document("%s/../posts/%s" % (os.path.dirname(__file__), post), \
                outdir="%s/../tmp/www/" % os.path.dirname(__file__))
        p.write()
        
        file = "%s/../tmp/www/archives/%s/%s/%s/%s.html" \
                % (os.path.dirname(__file__), p.year, \
                p.month, p.day, p.slug)
        self.assertTrue(os.path.isfile(file))

    def testwrite_index(self):
        posts = []
        for post in self.post_files:
            p = Document("%s/../posts/%s" % (os.path.dirname(__file__), post), \
                    outdir="%s/../tmp/www" % os.path.dirname(__file__))
            posts.append(p)

        properties = { 'posts':posts }
        i = Document("%s/../index.markdown" % os.path.dirname(__file__), \
                properties=properties)
        print i.render()


        

if __name__ == '__main__':
    unittest.main()
