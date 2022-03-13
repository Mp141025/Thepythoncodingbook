# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:11:21 2022

@author: mishr
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 1000)

for a in np.arange(-10, 10.1, 0.1):
    y = np.sin(x-a)/x
    plt.clf()
    plt.plot(x, y)
    plt.ylim([-1, 1])
    plt.title(f"a = {a:.1f}")
    plt.pause(0.01)

plt.show()