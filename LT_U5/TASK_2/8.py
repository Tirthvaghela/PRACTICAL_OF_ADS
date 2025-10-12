import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
departments = ['HR', 'IT', 'Sales', 'IT', 'HR', 'Finance', 'Sales', 'HR', 'IT', 'Sales'] # [cite: 46]

# Create the countplot
plt.figure(figsize=(8, 5))
sns.countplot(x=departments, palette='viridis')

# Add titles and labels
plt.title('Number of Employees per Department')
plt.xlabel('Department')
plt.ylabel('Employee Count')

# Show the plot
plt.show()