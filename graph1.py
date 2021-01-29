# Import libraries
import matplotlib.pyplot as plt

# Creating dataset
x = ['Ladakh', 'Kolkata']
y = [1.334, 44.966]

# Creating plot and bar
plt.bar(x, y, color=['red', 'green'], edgecolor=['black','black'])

# Creating y-axis label
plt.ylabel("Population (in lakhs) ->")

# Creating title
plt.title("Population of Ladakh and Kolkata (as per 2011 CENSUS data)")

# show plot
plt.show()

