#!/usr/bin/python

import argparse

from extern.wrapper.square import Math

def main():

    # Define number argument
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="Integer to square", type=int)

    # Get number argument
    number = parser.parse_args().number

    # Invoke and print result of Python wrapper
    print(Math.square(number))

main()

