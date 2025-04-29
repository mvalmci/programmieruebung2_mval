
def plot_data_array(x,y):

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(x, y, label='Power Curve', color='blue')
    plt.xlabel('Time (min)') 
    plt.ylabel('Power (W/kg)')
    plt.title('Power Curve')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 30)  # Set x-axis limits to 0 to 60 minutes

    yticks = range(0, y, 2)
    ytick_labels = [f"{val}W/kg" for val in yticks]

    plt.yticks(yticks, ytick_labels)






    plt.show()