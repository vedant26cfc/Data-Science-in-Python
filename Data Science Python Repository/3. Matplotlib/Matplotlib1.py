
## TO PLOT MULTIPLE VALUES ON THE AXIS

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#X Axis values
age_x = [25,26,27,28,29,30,31,32,33,34,35]

#C Dev Y Values
sal_y = [65000,66000,67000,68000,69000,70000,71000,72000,73000,74000,75000]

#Python Dev Y Vals
sal_py = [66000,67000,68000,69000,70000,71000,72000,76000,78000,79000,80000]


plt.plot(age_x, sal_y, 'r', label='C Developer')
plt.plot(age_x, sal_py, 'b', label='Python Developer')

plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.title('Salaries of Developer')
plt.legend()
plt.grid()

plt.show()