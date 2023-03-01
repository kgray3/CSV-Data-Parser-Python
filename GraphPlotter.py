import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from DataParser import DataParser

class GraphPlotter:
    # Method to plot graphs for each file in one subplot
    def plot_graph(files):
        # Creates the subplot based on the # of files
        figure, axis = plt.subplots(len(files), constrained_layout = True)
        counter = 0
        for file in files:
            # Convert date/time to timestamp for x-axis
            timestamp_arr = [None] * len(file['Date'])
            for i in range(len(file['Date'])):
                timestamp_arr[i] = DataParser.parse_date_and_time_str(file['Date'][i] + ' ' + file['Time'][i])
            
            x_axis = timestamp_arr

            # Convert level values from Strings to integers
            y_axis = [eval(m) for m in file['LEVEL']]

            # Set the labels and plot the graph for each file
            axis[counter].set_xlabel('Timestamp')
            axis[counter].set_ylabel('Level')
            axis[counter].plot(x_axis, y_axis)
            counter = counter + 1

        # Display subplot to screen
        plt.show()