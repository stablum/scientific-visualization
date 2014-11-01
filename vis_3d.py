#!/usr/bin/env python

err,warn,info = __import__('log').setup("vis_3d")
import numpy as np
import pylab
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def normalize(m):
    _min = np.min(m)
    _max = np.max(m)
    ret = (m - _min)/(_max - _min)
    return ret

def show(df):
    info("show")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("year")
    xs = df.year
    ax.set_ylabel("horsepower")
    ys = df.horsepower
    ax.set_zlabel("weigth")
    zs = df.weigth
    s = np.power(df.cylinders,2)
    cmap=plt.get_cmap('gnuplot2')
    c = cmap(normalize(df.MPG))

    ax.scatter(xs, ys, zs, s=s,c=c)
    info("end.")
    pylab.show()
