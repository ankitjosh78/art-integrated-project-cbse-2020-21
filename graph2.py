# Import libraries
import matplotlib.pyplot as plt

# Creating dataset
x = ['Ladakh', 'Kolkata']
y = [93.7, 358.8]

# Creating plot and bar
plt.bar(x, y, color=['red', 'green'], edgecolor=['black','black'])

# Creating y-axis label
plt.ylabel("Total Literates (in thousands) ->")

# Creating title
plt.title("Literatcy of Ladakh and Kolkata (as per 2011 CENSUS data)")

# show plot
plt.show()

