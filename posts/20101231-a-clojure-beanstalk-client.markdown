---
layout: post
title: A clojure beanstalk client
...

<p class="postmeta">December 31 2010 - Oakland, Ca</p> 

Towards the end of last year I decided that I wanted to spend some time
learning Lisp (a Lisp e.g. Common Lisp, Scheme, or Clojure) in 2010. I started 
out by working through some of [Pratical Common Lisp](http://gigamonkeys.com/book/). 
I jumped around a bit and learned a lot. Some challenges kept nagging me
though. For example, I wanted to experiment with network programming. This
raised a few questions-- which Lisp do you use or which library do you use? Do
you use something like the SBCL sb-bsd-sockets or an abstraction like IOLib? I
had my working envirnoment setup with CLISP. If I went with SBCL, I would have
to do some re-setup/learning in a different environment. If I went with IOLib I
would have to spend more time delving into package management. None of these
are showstoppers, but they do prompt more decision making than you are
typically used to when you want to start tinkering with a language. 

Another criteria I was using to ask the "which Lisp?" question is viability at
work (I have been working for web startups the last few years). While I was exploring 
Scheme it looked like [Racket](http://racket-lang.org/) has most active 
community and through documentation but I could find only one
[reference](http://www.lava.net/~shiro/Private/essay/gdc2002.html) where
someone was using Scheme in production.

I finally settled on [Clojure](http://clojure.org/) towards the end of the
year. The production usage is limited (one [example](http://flightcaster.com/)
that I'm aware of) but it seemed promising. I appreciated the emphasis the
language designers put on immutability
