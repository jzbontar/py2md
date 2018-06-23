'''
Header 1
========

some text, bla bla
'''

import pathlib
import sys

import numpy as np
import pylab as plt

'''
This is where we do some lists:

- ena
- dva
- tri
'''

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x)
plt.savefig('foo.png')

'''
![foo](foo.png)
'''
