### 2. Monthly Average Temperature and Humidity Levels

This graph shows average temperature and humidity levels over a month, critical for assessing HVAC performance.

python
# Additional data for humidity
humidity_levels = np.random.uniform(low=30, high=70, size=(30,))

fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot temperature
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color='red')
ax1.plot(dates, energy_consumption, color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Create a second y-axis for humidity
ax2 = ax1.twinx()
ax2.set_ylabel('Humidity (%)', color='blue')
ax2.plot(dates, humidity_levels, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.title('Monthly Average Temperature and Humidity Levels')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


