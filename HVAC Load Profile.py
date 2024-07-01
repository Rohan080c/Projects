#This graph is used to depict the load profile of an HVAC system throughout a day.
#Note your system must be installed with these modules otherwise code will not work

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example data for load profile
hours = np.arange(24)
load_profile = np.random.uniform(low=10, high=100, size=(24,))

plt.figure(figsize=(10, 5))
plt.bar(hours, load_profile, color='green')
plt.xlabel('Hour of the Day')
plt.ylabel('Load (kW)')
plt.title('HVAC Load Profile Over a Day')
plt.xticks(hours)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
