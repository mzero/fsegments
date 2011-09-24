
# In response to Guido's question about frange()
#    https://plus.google.com/115212051037621986145/posts/ZnrWDiHHiaW
# I think the problem is the API doesn't work for floating point. A more usual
# scenario is the need to divide a floating point range into segments, perhaps
# for bucketing, or discrimination of values. Hence, I offer the following.
#    - Mark Lentczner

def fsegments(num, *args):
    """fsegments(num [[,start], end]) -> generator
    
    A float generator that supplies the segments formed by dividing the range
    [start, end] into num equal intervals. Note that the end value of each
    segment is exactly the start value of the next. Note also that supplied
    start and end values will appear exactly in the first and last segments
    respectively.
        
    If not specified, the start is 0.0 and the end is 1.0. Note that specifying
    just one value specifies the end.
    
    >>> list(fsegments(4))
    [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.0)]
    
    >>> list(fsegments(3, 2.1))
    [(0.0, 0.7), (0.7, 1.4), (1.4, 2.1)]
    
    >>> list(fsegments(3, 1.0, 2.2))
    [(1.0, 1.4), (1.4, 1.8), (1.8, 2.2)]
    
    >>> list(fsegments(2, -9e+307, 9e+307))
    [(-9e+307, 0.0), (0.0, 9e+307)]
    
    Due to the limitations of doctest, it is hard to demonstrate that start and
    end values result exactly, but they do!
    """
    
    start = 0.0
    end = 1.0
    n = len(args)
    if n == 2:
        start, end = args
    elif n == 1:
        end = args[0]
    elif n != 0:
        raise TypeError('fsegments expects 1-3 arguments, got %d' % n)
    if num < 1 or int(num) != num :
        raise TypeError('fsegments expects positive integer number of segments, got %d' % n)
    
    last = start
    for i in xrange(1, num+1):
        next = start * (float(num - i)/num) + end * (float(i)/num)
        yield (last, next)
        last = next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
