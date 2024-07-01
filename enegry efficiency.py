### 4. Energy Efficiency Scatter Plot

This graph compares energy efficiency across different HVAC systems or configurations.

python
# Additional systems data
systems = ['System A', 'System B', 'System C', 'System D']
efficiency = np.random.uniform(low=70, high=95, size=(4,))

plt.figure(figsize=(8, 4))
plt.scatter(systems, efficiency, color='purple')
plt.xlabel('HVAC System')
plt.ylabel('Efficiency (%)')
plt.title('Comparison of HVAC System Efficiencies')
plt.grid(True)
plt.show()
