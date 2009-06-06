# Furthermore
Furthermore is a simple static site generator inspired by
[jekyll](http://github.com/mojombo/jekyll/tree/master) but written in python.
It currently supports posts written in
[markdown](http://daringfireball.net/projects/markdown/) and uses
[mako](http://www.makotemplates.org/) templates to generate the site. 
Pygments (via markdown) is used to add syntax highlighting to code segments. 
It also comes with a webserver so you can preview your site locally.

This project got started because of the advice from the [Pragmatic
Programmer](http://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/)
to learn one new language a year. I started out this year wanting to learn
Haskell and realized that I wanted to blog about learning Haskell but wasn't
satisfied with my current blogging [platform](http://wordpress.org/). Which
remided me that I always wanted to write my own blog software. I'm supposed to
be a hacker! Why not write my own? So I changed gears and started writing
furthermore using Python-- a language I also wanted to learn. 
So in the end, I ended up learning more Python than Haskell. But now
that I have something usable, maybe I can go back to the language I started
the year wanting to learn!

# Features

Furthermore is pretty simple right now. It is a bare bones static site generator with the following:

 * mako templates for python-based template generation
 * pygments syntax highlighting 
 * markdown for text-to-html generation
 * a local http server for site previewing 


# Getting Started
 * Dependencies
   * [Pygments](http://pygments.org/download/) for syntax highlighting
   * [PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html) 
   * [PyYAML](http://pyyaml.org/wiki/PyYAML)
 * [Usage](http://github.com/drsnyder/furthermore/wikis/usage/) 

Enjoy!

# License

Copyright (c) 2009 Damon Snyder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.



