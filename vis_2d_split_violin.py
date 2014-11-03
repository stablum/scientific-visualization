#!/usr/bin/env python

err,warn,info = __import__('log').setup("vis_2d_split_violin")
import numpy as np
import pylab
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cmap=plt.get_cmap('brg')

def normalize(m):
    _min = np.min(m)
    _max = np.max(m)
    ret = (m - _min)/(_max - _min)
    return ret,_min,_max

def markers_specs():
    return {
        'Japan':'o',
        'US': '*',
        'Europe': 's',
    }

def markers_offsets_specs():
    return {
        'o': 0.25,
        's': 0.0,
        '*': -0.25
    }

def get_markers_offsets(markers):
    specs = markers_offsets_specs()
    markers_offsets = [
        specs[m]
        for m 
        in markers
    ]
    return np.array(markers_offsets)
    

def get_markers(origin):
    ret = origin
    for before,after in markers_specs().items():
        ret = ret.replace(to_replace=before,value=after)
    return ret.tolist()

def show(df):
    info("show")
    
    fig = plt.figure()
    
    axs = [ fig.add_subplot(n) for n in [211, 212]]

    axs[0].set_title("violin plot: trends in car manufacturing")

    for ax in axs:
        ax.set_xlabel("year")
    
    
    years = df.year
    
    markers = get_markers(df.origin)
    xs = years + get_markers_offsets(markers)

    years_uniq = list(set(years.tolist()))
    years_uniq.sort()

    s = np.power(df.cylinders,2.6)*2
    MPG_norm,MPG_min,MPG_max = normalize(df.MPG)
    c = cmap(MPG_norm)
    mappable = pylab.cm.ScalarMappable(cmap=cmap)
    mappable.set_array(np.array([MPG_min,MPG_max]))
    

    for ax,ys,ylabel in zip(axs,
                    [df.horsepower,df.weigth],
                    ["horsepower","weigth"]
                    ):

        for x in years_uniq[:-1]:
            info(x)
            ax.axvline(x=x+0.5,ls='--',color='k',alpha=0.3)
        ax.xaxis.set_ticks(np.arange(min(years), max(years)+1, 1.0))
        ax.set_ylabel(ylabel)
        #import pdb; pdb.set_trace()
        violin_data = [ getattr(df.query("year=="+str(yr)),ylabel) for yr in years_uniq]
        ax.violinplot(violin_data, years_uniq,showmedians=True,showextrema=False,points=1000,bw_method="silverman")
        for i,m in enumerate(markers):
            scatter = ax.scatter(xs[i], ys[i], s=s[i],c=c[i],alpha=0.2,marker=m)
        cbar = plt.colorbar(mappable,ax=ax)
        cbar.set_label("MPG")

    circle = plt.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="white")
        
    mobjs = []
    for m in markers_specs().values():
        mobj = plt.Line2D(range(1), range(1), color="white", marker=m, markerfacecolor="white")
        mobjs.append(mobj)
        
    axs[0].legend([circle]+mobjs,['marker size: cylinders']+markers_specs().keys())
    info("end.")
    pylab.show()
