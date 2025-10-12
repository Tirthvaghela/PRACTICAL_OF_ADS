import matplotlib.pyplot as plt

# Sample Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] # [cite: 9]
visitors = [100, 120, 90, 150, 180, 200, 170] # [cite: 10]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(days, visitors, marker='o', linestyle='--', color='purple')

# Add titles, labels, and grid as required
plt.title("Weekly Website Visitors") # 
plt.xlabel("Day of the Week")
plt.ylabel("Number of Visitors")
plt.grid(True) # 

# Show the plot
plt.show()