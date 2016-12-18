#!/usr/bin/python

import sys
import argparse

from extern.wrapper.square import Math

def main():
    # Get number argument
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="Integer to square", type=int)
    args = parser.parse_args()

    # Invoke and print result of Python wrapper
    print(Math.square(args.number))

main()
