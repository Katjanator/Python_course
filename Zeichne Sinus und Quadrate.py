# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:18:19 2018

@author: Lenovo
"""
import numpy as np 
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
F1 =[]
for i in X:
        if i  >= -2*np.pi and i < -np.pi:
            F1.append(1)
        if i  >-np.pi and i<0:
            F1.append(-1)
        if i  >0 and i < np.pi:
            F1.append(1)
        if i  > np.pi and i <= 2* np.pi:
            F1.append(-1)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3.1, 3.1
plt.axis([startx, endx, starty, endy])
plt.plot(X,F1)
plt.plot(X,F2)
plt.plot(X,F3)
plt.show()