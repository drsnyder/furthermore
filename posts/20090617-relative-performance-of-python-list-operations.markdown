---
layout: post
title: Exploring the relative performance of different list operations in Python
...

<p class="postmeta">June 17 2009 - East Oakland, Ca</p> 

This past weekend, I attended the Python training session at
[USENIX09](http://www.usenix.org/event/usenix09/) in San Diego taught by [David
Beazley](http://www.dabeaz.com/). He posted his [slides and
examples](http://www.dabeaz.com/usenix2009/pythonprog/) on his web site.

One question that came to mind during the session was which form of list
processing is faster: a for loop or a list comprehension. The general consensus
in the class (and from David) was that list comprehensions should be faster.
The normal caveats of context apply.

If you aren't familiar with list comprehensions, they take the following form
in python:

    :::python
    >>> [val for val in xrange(0,10)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
David mentioned that list comprehensions in Python were inspired
by Haskell. The Haskell form of the above looks like this:

    :::haskell
    Prelude> [x | x <- [0..9]]
    [0,1,2,3,4,5,6,7,8,9]
    
To explore this further, I came up with a simple scenario that you
might encounter in working with lists. I pulled down part (about
10M) of an apache access log and came up with some small segment
of each log that I wanted to pull out. For this experiment, I just
pull out the first four elements of each log entry. A sample might
look like this:

<code>
     192.168.0.9 - - [04/Sep/2008:00:21:18 +0000] "GET / HTTP/1.1" 200 2029 "-" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.1) Gecko/2008070206 Firefox/3.0.1"
</code>

And the parsed out pieces look like this:

<code>
    ['192.168.0.9', '-', '-', '[04/Sep/2008:00:21:18 +0000]']
</code>

I pull out these elements by first slicing the first 45 characters from the
line and them splitting by the first 3 spaces (note that this might truncate
part of the timestamp field). Here is the snippit:

    :::python
    line[:45].split(' ', 3)
    
Before I moved ahead, I googled a little about the relative performance of list
comprehensions and for loops in Python. I found an article by Guido called
[Python Patterns - An Optimization
Anecdote](http://www.python.org/doc/essays/list2str/) where he discusses some
of the challenges in trying to optimize converting a list of integers into a
string. Although I'm not trying to optimize anything in my experiment, his
essay provided some insights into how one might approach optimizing python
code. He also provides the code he used for his different iterations and the
function he used to do the timing of each version. I used his timing function
in running my tests. 

I started by creating a function to loop through the lines in the file using a
for loop. Here is the function:

    :::python
    def forloop_listnf(lines):
        records = []
        for line in lines:
            records.append(line[:45].split(' ', 3))
        return records
    
It just loops through each line, pulls out the first three elements and
appends it to a list. The next function uses a list comprehension to do the
same thing:

    :::python
    def lc_listnf(lines):
        return [line[:45].split(' ', 3) for line in lines]

And finally, another approach to processing lists is using the map() function.
Since this is also a common approach (and should be done in C per Guido's
article) I included a function to do the same using map(). One difference with
the map() implementation is that a separate function was need to do the splice and split
operation on each element in the array provided to map(). 

    :::python
    def do_split(line):
        return line[:45].split(' ', 3)

    def map_list(lines):
        return map(do_split, lines)

The result surprised me a little. The map() implementation was the slowest. The
for loop was about 5% faster and the list comprehension was about 10% faster
than map().

I went through a couple of iterations before I settled on the
functions above.  I first used the do_split for all three but I
later decided that this unnecessarily slows down (with an extra
lookup and function call) the for loop and the list comprehension
because they can do the splice and split in-line. I tried to see if a lambda
would improve the map() performance, but it performed about the same. For this
simple test map() may have a handicap due to the function call on each element. 

 
# Conclusion
 
As a noob to python I'm not in a position to say conclusively that
list comprehensions are faster than for loops or the map() function.
This experiment seems to suggest that for simple cases such as this,
the list comprehension is faster.  It also looks cleaner (IMO). Building
the list can be done clearly and concisely on one line. Note also
that list comprehensions can be nested. An initial path that I
started on with this experiment was adding one more pass of processing
over the split out fields. A nested list comprehension worked, but
I backed off of that path to keep it simple.

Why are they faster? My initial thought is that there is less interpreter
overhead with the list comprehension. In the for loop, you need one other
variable (the result array) and you need to lookup this variable during each
iteration of the loop. You may not have that overhead with the list comprehension
(or perhaps it is reduced).

David's training classes are good. You can find out more
[here](http://www.dabeaz.com/training.html). 
