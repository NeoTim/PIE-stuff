#!/usr/bin/python

import subprocess
import argparse
import sys

addrs = {}
lib = "libssl"
executable = "where"

def run(key):
    p = subprocess.Popen("./where", stdout = subprocess.PIPE)

    out, _ = p.communicate()

    for line in out.splitlines():
        if key in line:
            data = line.split("-")
            # print data
            addrs[data[0]] = True
            break # buggy?


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', action="store_true", dest="d", help="DSO mode")
    parser.add_argument('-e', action="store_true", dest="e", help="executable mode")
    parser.add_argument('-s', action="store_true", dest="s", help="stack mode")

    results = parser.parse_args()

    if results.d:
        key = lib
    elif results.e:
        key = executable
    elif results.s:
        key = "stack"
    else:
        parser.print_help()
        sys.exit(-1)

    while True:
        run(key)
        print len(addrs)

if __name__ == "__main__":
    main()
