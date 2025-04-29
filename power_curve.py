import matplotlib.pyplot as plt
from sort import bubble_sort
from load_data import load_data
import numpy as np
from plot import plot_data_array

data = load_data('activity.csv')
power_W = data['PowerOriginal']

npoints = len(power_W)

time = np.arange(npoints)
#print(time)
#print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

# Plotting
plot_data_array(time/60, sorted_power_W[::-1])