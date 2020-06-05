import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit

plt.style.use('bmh')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'

data = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/NMR/Zellen_10msT37C_manypoints_2ndday - Data.csv')
#graph = data[['GradAna'], ['EchoAmp']]
reduced = data[['EchoAmp', 'GradAna']].dropna()
y = reduced['EchoAmp']
x = reduced['GradAna']
x_values, y_values = x.to_numpy(dtype = float), y.to_numpy(dtype = float)
index = 8
tangentx_range = np.linspace(float(x_values[index - 1]), float(x_values[index+1]), 50)
x_range = np.linspace(x_values[0], x_values[-1], num=200)
"""
Approximation to be in another file
"""

approx = np.polyfit(x_values, np.log(y_values), deg = 6, w=np.sqrt(y_values))
p = np.poly1d(approx)
der = np.polyder(p)
def tangent_line(f, ax, x_0, a, b):
    x = np.linspace(a, b)
    y = np.exp(f(x))
    y_0 = np.exp(f(x_0))
    derivative = np.polyder(f)
    y_tan = (derivative(x_0)*np.exp(f(x_0)))*(x- x_0) + y_0
    ax.plot(x, y_tan, color=green, label='Tangent Line')

#Plotting

fig, ax = plt.subplots()
#Scatter Dots
ax.scatter(x_values, y_values)
#Plot Line
#ax.plot(x_values,y_values, label=('Something?'))
#Plot Approximation
ax.plot(x_range, np.exp(p(x_range)), color=orange, label='Approximation Linear')
#Tangent Line
#ax.plot(x_values, np.gradient(p(x_values)), color='gold')
ax.plot(tangentx_range, tangenty_range, color=green)
ax.set_xlabel('GradAna')
ax.set_ylabel('EchoAmp')

#Create Zoom
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
axins = zoomed_inset_axes(ax, 3.8, loc=1)
axins.set_facecolor('#e1eded')
tangent_line(p,axins, x_values[8], x_values[7], x_values[9] )
axins.plot(x_range, np.exp(p(x_range)), color=orange, label='Approximation')
axins.scatter(x_values, y_values, label='Data Points')
#axins.plot(tangentx_range, tangenty_range, color=green, label='Tangent Line at ')
axins.set_xlim(x_values[index-2], x_values[index+2])
axins.set_ylim(y_values[index+2], y_values[index-2])
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/NMR/files/tangent_line_view2.png')
