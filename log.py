#!/usr/bin/env python

import logging
import coloredlogs

# higher order functions
def makefunc(log_fn):
    def ret(stuff):
        s = str(stuff)
        lines = s.split('\n')
        for line in lines:
            log_fn(line)
    return ret
    

def setup(modulename):
    logger = logging.getLogger(modulename)
    coloredlogs.install(level=logging.DEBUG)
    
    error = makefunc(logger.error)
    warn  = makefunc(logger.warn)
    info  = makefunc(logger.info)    

    return (error, warn, info)
