#!/usr/bin/env python
"""mapper.py"""

import sys
topwords =['senate,'nixon','governor','assembly','cuomo','campaign','state','budget','school','albany']
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for i,word in enumerate(words):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word.lower() not in topwords):
            continue
        if(i < len(words)-1):
            wordco = word + "," + words[i+1] 
        else:
            wordco = word + "," + words[i-1]
        
        print('%s\t%s' % (wordco, 1))
