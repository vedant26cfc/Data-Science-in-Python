
from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()

#Now create the axes
axes = fig.add_axes([0,0,0.8,0.8])

age1_x = [25,26,27,28,29,30,31,32,33,34,35]
sal_y = [50000,51000,55000,59000,61000,65000,69000,72000,75000,78000,80000]
sal_py = [51000,53000,57000,59000,65000,68000,69000,78000,80000,82000,89000]

#First plot
axes.plot(age1_x, sal_y, 'r', label='C Devs')

#Second plot
axes.plot(age1_x, sal_py, 'b--', label= 'Py Devs')

axes.set_xlabel('Ages')
axes.set_ylabel('Median Salaries')
axes.set_title('Salaries by age')
plt.grid(True)
plt.show()