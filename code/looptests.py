import time
import sys


def do_split(line):
    return line[:45].split(' ', 3)

def forloop_list(lines):
    records = []
    ds = do_split
    for line in lines:
        records.append(ds(line))
    return records

def forloop_listnf(lines):
    records = []
    for line in lines:
        records.append(line[:45].split(' ', 3))
    return records

def map_list(lines):
    return map(do_split, lines)


def map_listlf(lines):
    return map(lambda line: line[:45].split(' ', 3), lines)

def lc_list(lines):
    ds = do_split
    return [ds(line) for line in lines]

def lc_listnf(lines):
    return [line[:45].split(' ', 3) for line in lines]



fd = open("access.log")
lines = fd.readlines()
fd.close()


# Source: http://www.python.org/doc/essays/list2str.html
def timing(f, n, a):
    print f.__name__,
    r = range(n)
    t1 = time.clock()
    for i in r:
        f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a)
    t2 = time.clock()
    print round(t2-t1, 3)

m = map_list(lines)
mlf = map_listlf(lines)
f = forloop_listnf(lines)
l = lc_listnf(lines)

if m == mlf == f == l:
    pass
else:
    print "oops, not consistent"
    sys.exit(1)

#timing(forloop_list, 10, lines)
timing(map_list, 10, lines)
timing(map_listlf, 10, lines)
timing(forloop_listnf, 10, lines)
timing(lc_listnf, 10, lines)
#timing(lc_list, 10, lines)
