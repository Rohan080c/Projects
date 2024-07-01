#This graph will show the daily energy consumption of an HVAC system.
#Note your system must be installed with these modules otherwise code will not work

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Example data
dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
energy_consumption = np.random.uniform(low=200, high=400, size=(30,))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(dates, energy_consumption, marker='o', linestyle='-', color='blue')
plt.title('Daily Energy Consumption of HVAC System')
plt.xlabel('Date')
plt.ylabel('Energy Consumption (kWh)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
