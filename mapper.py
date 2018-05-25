#!/usr/bin/env python
"""mapper.py"""

import sys
stopwords =['would','will','who','was','to','that','so','on','of','of','it','have','and','or','is','advertisement','ad','the','this','when',"if","with","how"]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if any(word.lower() in s for s in stopwords):
            continue
        print '%s\t%s' % (word, 1)
