#!/usr/bin/env python

err,warn,info = __import__('log').setup("vis_3d")
import numpy as np
import pylab
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from mpl_toolkits.mplot3d import Axes3D

def normalize(m):
    _min = np.min(m)
    _max = np.max(m)
    ret = (m - _min)/(_max - _min)
    return ret,_min,_max

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
    MPG_norm,MPG_min,MPG_max = normalize(df.MPG)
    c = cmap(MPG_norm)
    scatter = ax.scatter(xs, ys, zs, s=s,c=c)
    info("scatter:")
    info(scatter)
    #import pdb;pdb.set_trace();
    mappable = pylab.cm.ScalarMappable(cmap=cmap)
    mappable.set_array(np.array([MPG_min,MPG_max]))
    cbar = plt.colorbar(mappable,ax=ax)
    cbar.set_label("MPG")
    c = plt.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="white")
    ax.legend([c],['marker size: cylinders'])
    info("end.")
    pylab.show()
