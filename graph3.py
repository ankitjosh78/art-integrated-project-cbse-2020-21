# Import libraries 
import numpy as np 
import matplotlib.pyplot as plt 


# Creating dataset 
religion = ['Hindu', 'Muslim',  
		'Buddhist', 'Others'] 

data = [22882, 19057, 88635, 2913] 



# Creating color parameters 
colors = ( "orange", "cyan", "brown", 
		"grey", "indigo", "beige") 

# Wedge properties 
wp = { 'linewidth' : 1, 'edgecolor' : "green" } 

# Creating autocpt arguments 
def func(pct, allvalues): 
	absolute = int(pct / 100.*np.sum(allvalues)) 
	return "{:.1f}%\n({:d} g)".format(pct, absolute) 

# Creating plot 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data, 
								autopct = lambda pct: func(pct, data), 
								labels = religion, 
								shadow = True, 
								colors = colors, 
								startangle = 90, 
								wedgeprops = wp, 
								textprops = dict(color ="black")) 

# Adding legend 
ax.legend(wedges, religion, 
		title ="Religion", 
		loc ="center left", 
		bbox_to_anchor =(1, 0, 0.5, 1)) 

plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Religion wise population of Ladakh (as per 2011 CENSUS)") 

# show plot 
plt.show() 

