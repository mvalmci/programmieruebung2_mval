
def plot_data_array(x,y):

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(x, y, label='Power Curve', color='blue')
    plt.xlabel('Time (min)') 
    plt.ylabel('Power (W)')
    plt.title('Power Curve')
    plt.legend()
    plt.grid(True,which= 'both', linewidth=0.5)
    plt.xlim(-1, 31)  # Set x-axis limits to 0 to 60 minutes

    yticks = range(0, 433, 43)
    ytick_labels = [f"{val}W" for val in yticks]

    plt.yticks(yticks, ytick_labels)

    plt.savefig('power_curve.png')
    plt.show()