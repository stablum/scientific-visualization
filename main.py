#!/usr/bin/env python

import read

err,warn,info = __import__('log').setup("main")

from sys import argv

def main():
    info("main")
    assert len(argv) >=2, usage()
    command = argv[1]
    assert command in available_commands(), usage()
    module = __import__("vis_"+command)
    data = read.csv('cars.csv')
    module.show(data)

def available_commands():
    return [
        '3d'
    ]

def usage():
    return "usage: "+argv[0]+" <command>\n" \
        + "available commands:\n" \
        + "\n".join([ 
            " * " + cmd 
            for cmd 
            in available_commands()
        ])

if __name__ == "__main__":
    main()

