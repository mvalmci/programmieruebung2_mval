
def plot_data_array(x,y):

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(x, y, label='Power Curve', color='blue')
    plt.xlabel('Time (s)') 
    plt.ylabel('Power (W)')
    plt.title('Power Curve')

    plt.show()