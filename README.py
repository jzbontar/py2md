'''
py2md
=====

Convert a python script to markdown. Useful for presenting code to your co-workers.

Install
-------

    sudo ln -s $PWD/py2md /usr/local/bin/

Usage
-----

    py2md README.py > README.md

Example
-------

Import numpy and matplotlib.
'''

import numpy as np
import pylab as plt

'''
### Plan

1. define utility functions
2. compute <img src="https://latex.codecogs.com/gif.latex?sin(x)" title="sin(x)" />
3. plot
'''

def my_sin(x):
    '''This is a docstring'''
    return np.sin(x)

x = np.linspace(0, 2 * np.pi, 100)
y = my_sin(x)

plt.plot(x, y)
plt.savefig('plot.png')

'''
![](plot.png)
'''
