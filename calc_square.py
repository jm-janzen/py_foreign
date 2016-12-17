#!/usr/bin/python

import sys

from extern.wrapper.square import Math

def main():

    if not len(sys.argv) > 1:
        print("Usage:\t./calc_square <NUMBER>")
        exit(1)

    print(Math.square(sys.argv[1]))

main()
