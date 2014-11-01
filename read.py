#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

err,warn,info = __import__('log').setup("read")

def csv(filename):
    df = pd.read_csv(filename)
    info(filename+" columns:")
    info(df.dtypes)
    info("MPG:")
    info(df.MPG)
    return df
    
