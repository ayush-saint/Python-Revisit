# matplotlib : library used for data visualization (making graphs and charts). 

import matplotlib.pyplot as plt 

# hour vs marks 
hours = [2,4,6,8,10]
marks = [21,38,64,85,98]

print(plt.scatter(hours, marks))

#renaming x and y axis 
plt.xlabel("hours spent")
plt.ylabel("marks obtained")
print(plt.scatter(hours, marks))
