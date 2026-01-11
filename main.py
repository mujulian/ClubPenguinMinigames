#!/usr/bin/env python3

import sys

import setup
import catchinwaves

def main():
    setup.start()
    catchinwaves.start()

    sys.exit(0)    

if __name__ == "__main__":
    main()