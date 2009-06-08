---
layout: post
title: Learn one new language a year
...

<p class="postmeta">June 7 2009 - East Oakland, Ca</p> 

Taking the advice from the [Pragmatic
Programmer](http://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/)
I set out to learn Haskell this year. My plan didn't turn out like I expected. I
started learning Haskell by working through [Real World
Haskell](http://book.realworldhaskell.org/). It was tough going, so I decided I
wanted to start blogging about it. It was than that I remembered that my blog has
been neglegled for a long time (more than a year and maybe 2) and that I had been on the
lookout for a different blogging platform for some time. 

I had recently found [jekyll](http://github.com/mojombo/jekyll/tree/master)
(a static site generator written in Ruby) from a reference on
[HN](http://news.ycombinator.com) and thought it was a great idea.
This is exactly the kind of thing I was looking for. But using
jekyll didn't feel quite (well, sortof-- the layout and some of the styling
does come from jekyll) right since I had often told myself that I
wanted to write my own blogging tool. So I dropped learning Haskell
(for the moment) and set out to write my own blogging tool.

My background is mostly in Perl, PHP, and little bit of Ruby. But over the last 
year I've been creating a few tools in Python for automating some day-to-day
operations at [work](http://www.carsala.com). I chose Python at work after
reading [Why Python?](http://www.linuxjournal.com/article/3882) and having
similar experiences. The small scripts I would write often worked right out of
the editor. I also appreciated how readable the code was. So I started hacking
away at a blogging tool using Python. 

I'm calling the tool
[furthermore](http://github.com/drsnyder/furthermore/tree/master). You can
download or take a look at
[github](http://github.com/drsnyder/furthermore/tree/master). Furthermore is
pretty simple. It is a bare bones static site generator. Here is a brief
summary of the features:

 *  mako templates for python-based template generation
 *  pygments syntax highlighting (via markdown)
 *  markdown for text-to-html generation
 *  a local http server for site previewing 

To get started, you will need the following:

 * [Pygments](http://pygments.org/download/) for syntax highlighting. 
  Also see the [codehighlight](http://www.freewisdom.org/projects/python-markdown/CodeHilite) 
  markdown plugin.
 * [PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html) for RSS feed generation
 * [PyYAML](http://pyyaml.org/wiki/PyYAML) for documents

Posts are contained in the "posts" directory. Each post consists
of a YAML preamble that includes the template type and the post
title. Post files themselves follow the format
YYYYMMDD-post-slug-goes-here.markdown. The year, month, day, and
slug will be parsed out of the file name to produce a url of the
form /archives/YYYY/MM/DD/slug.html. The preamble looks something
like this.

    :::yaml
    ---
    title: Learn one new language a year
    layout: post
    ...

Everything after the close of the YAML preamble (...) is treated as the
document contents in [markdown](http://daringfireball.net/projects/markdown/). 
The layout value will be used to lookup the proper template in the
"templates" directory and the title value will be plugged into the
template to generate the title of the page. At the top level you
will also find a "images" and "css" directories containing the
expected collateral.

And finally, to render your posts and any other files, run futhermore:

    :::bash
    ./bin/furthermore -P -b . -o www -f index.html -S

This will process all of your posts using the current directory as
the base (where to find css, images, posts, and templates directories),
while outputting the rendered content to www. It will also run index.html
through mako and startup a local webserver so you can preview the site. 
To see all of the options provided, run furthermore with -h.

If you get stuck take a look at the
[usage](http://github.com/drsnyder/furthermore/wikis/usage/) document I'm
putting together. I'm still updating, but it should have enought to get the
idea and get started if you want to use it. 

Enjoy!
