#! /usr/bin/env python3
# code blocks for aliases

import sys

def alias():
    strn = ""
    args = arguments = len(sys.argv)
    if sys.argv[1] == "set" and sys.argv[2] == "alias":
        i = 3
        while i < args:
            # replace with your own logic
            print(sys.argv[i])
            i+=1

alias()
