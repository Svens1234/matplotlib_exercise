# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:43:18 2021

@author: German
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0,100)
b=a-5
c=a**3-b**2
#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b)
#axes.set_xlabel('a label')
#axes.set_ylabel('b label')
#axes.set_title('title label')



#figure=plt.figure()
#axes1=figure.add_axes([0,0,1,1])
#axes2=figure.add_axes([0.2,0.5,0.2,0.3])




#print(axes1.plot(a,b))
#print(axes2.plot(b,c))
#print(figure)






#figure=plt.figure()
#axes1=figure.add_axes([0,0,1,1])
#axes2=figure.add_axes([0.2,0.5,0.3,0.4])


#axes1.plot(a,b)
#axes1.set_xlabel('a array')
#axes1.set_ylabel('b array')
#axes1.set_title('Outer plot')
#axes1.set_xlim(20,60)
#axes1.set_ylim(10,70)




#axes2.plot(a,c)
#axes2.set_xlabel('a array')
#axes2.set_ylabel('c array')
#axes2.set_title('Inner plot')
#axes2.set_xlim(20,60)
#axes2.set_ylim(10000,70000)







#figure, area=plt.subplots(nrows=1, ncols=2, figsize=(11,3))






#figure, axes=plt.subplots(nrows=1, ncols=2, figsize=(11,3))
#axes[0].plot(c,a)
#axes[1].plot(c,b)










#figure, axes=plt.subplots(nrows=1, ncols=2, figsize=(11,3))
#axes[0].plot(c,a, color='purple')
#axes[1].plot(c,b, color='orange')








#figure, axes=plt.subplots(nrows=1, ncols=2, figsize=(11,3))
#axes[0].plot(c,a, color='purple', ls='--')
#axes[1].plot(c,b, color='orange', ls=':')







figure, axes=plt.subplots(nrows=1, ncols=2, figsize=(11,3))
axes[0].plot(c,a, color='purple', ls='--',lw=2)
axes[1].plot(c,b, color='orange', ls=':', lw=10)


