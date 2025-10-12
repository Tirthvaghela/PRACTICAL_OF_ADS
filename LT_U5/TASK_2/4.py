import matplotlib.pyplot as plt

# Sample Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] # [cite: 26]
city_x_temp = [30, 32, 33, 31, 29, 28, 27] # [cite: 27]
city_y_temp = [25, 26, 27, 26, 24, 23, 22] # [cite: 28]

# Create the plot
plt.figure(figsize=(9, 5))
plt.plot(days, city_x_temp, marker='^', label='City X')
plt.plot(days, city_y_temp, marker='s', label='City Y')

# Add titles, labels, legend, and grid as required
plt.title("Weekly Temperature Comparison: City X vs. City Y") # 
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend() # 
plt.grid(True) # 

# Show the plot
plt.show()