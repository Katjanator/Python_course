# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:19:43 2018

@author: Lenovo
"""

#with open ("filename","r") as fo: --> richtig wichtig, dann wird nichts gek´löscht und mann kann fo.close nciht vergessen :D
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-50, 50, 10, endpoint=True)
F1 =[]
for i in X:
    if i <= -25:
        F1.append(np.sin(X*np.random.randint(7, size=10)))
       
    if i > -25 and  i <= 0:
        F1.append(np.sin(X*np.random.randint(15, size=10)))
    if i > 0 and  i <= 25:
        F1.append(np.sin(X*np.random.randint(28, size=10)))
    if i > 25 and  i <= 50:
      
        F1.append(np.sin(X*np.random.randint(49, size=10)))

print(F1)

startx, endx = -51 , 51
starty, endy = -1, 1
plt.axis([startx, endx, starty, endy])
plt.plot(X,F1)
plt.show()
