
from matplotlib import pyplot as plt
import numpy as np

#Bar Charts

#To separate the bars
width = 0.5



age1_x = [25,26,27,28,29,30,31,32,33,34,35]
x_indexes = np.arange(len(age1_x))

sal_y = [50000,51000,55000,59000,61000,65000,69000,72000,75000,78000,80000]
sal_py = [51000,53000,57000,59000,65000,68000,69000,78000,80000,82000,89000]

#Now make the first plot 
#Label to identify C Developers
plt.bar(x_indexes-width, sal_y, width=width, color='#FF0000' ,label = 'C Developer')

#And now the second plot
#Label to identify Python developers
plt.bar(x_indexes, sal_py,width=width, color='#FFFF00', label = 'Python Developer')

#To make sure they show up
plt.legend()

plt.xticks(ticks=x_indexes, labels = age1_x)

plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.title('Median Salaries')
plt.show()

#What we exactly did here, take an array of length of x indexes
#Now since we did that, the labels would become the array from 0 to n
#So we use xticks which sets  sets the x-axis tick values, 
#which are the locations along the x-axis where the tick marks appear.