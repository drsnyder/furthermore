---
layout: post
title: Learn one new language a year
...

<p class="postmeta">June 7 2009 - East Oakland, Ca</p> 

Taking the advice from the [Pragmatic
Programmer](http://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/)
I setout to learn Haskell this year. My plan didn't turn out like I expected. I
started learning Haskell by working through [Real World
Haskell](http://book.realworldhaskell.org/). It was tough going, so I decided I
wanted to start blogging about it. It was than that I remembered that my blog has
been neglegled for a long time (more than a year) and that I had been on the
lookout for a different blogging platform for some time. 

I had recently stumbled upon
[jekyll](http://github.com/mojombo/jekyll/tree/master) (a static site generator
written in Ruby) and thought it was a great idea. This is exactly the kind of 
thing I was looking for. But using jekyll didn't feel quite right since I had 
often told myself that I wanted to write my own blogging tool. So I dropped
learning Haskell (for the moment) and set out to write my own blogging tool.

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

I'm eating [eating my own dog
food](http://en.wikipedia.org/wiki/Eat_one%27s_own_dog_food). This site was
generated using furthermore.
