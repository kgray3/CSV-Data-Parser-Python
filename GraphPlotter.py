import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from DataParser import DataParser

# Add titles
# Add dual/triple Y-axis for conductivity and temperature
class GraphPlotter:
    # Method to plot graphs for each file in one subplot
    def plot_graph(files, y_axes, scales):
        # Creates the subplot based on the # of files
        figure, axis = plt.subplots(len(files), constrained_layout = True)
        counter = 0
        
        #figure.subplots_adjust(right=0.75)
        y_axes_colors = [None] * len(y_axes)
        for z in range(len(y_axes)):
            y_axes_colors[z] = np.random.rand(3)
        if len(files) == 1:
            # Convert date/time to timestamp for x-axis
            file = files[0]
            timestamp_arr = [None] * len(file['Date'])
            for i in range(len(file['Date'])):
                timestamp_arr[i] = DataParser.parse_date_and_time_str(file['Date'][i] + ' ' + file['Time'][i])
            
            x_axis = timestamp_arr

            axis_counter = 0
            
            label_counter = 0
            for label in y_axes:
                    #print(label)
                    for key in file.keys():
                        print(key)
                    #y_axis = [eval(x) for x in file[label]]
                    axis.set_xlabel('Timestamp')
                    if axis_counter == 0 and file.setdefault(label):
                        y_axis = [eval (m) for m in file[label]]
                        axis.plot(x_axis,y_axis)
                        if scales[label_counter] != 0:
                             axis.yticks(np.arange(min(y_axis), max(y_axis), scales[label_counter]))
                        axis.set_ylabel(label)
                        axis.yaxis.label.set_color('b')
                        axis.tick_params(axis='y', colors='b')
                        axis_counter = axis_counter + 1
                    else: 
                        if file.setdefault(label):
                            y_axis = [eval (m) for m in file[label]]
                            new_axis = axis.twinx()
                            new_axis.spines.right.set_position(("axes",axis_counter))
                            new_axis.set_ylabel(label)
                            new_axis.yaxis.label.set_color(y_axes_colors[label_counter])
                            new_axis.tick_params(axis='y', colors=y_axes_colors[label_counter])
                            new_axis.plot(x_axis, y_axis, color=y_axes_colors[label_counter])
                            if scales[label_counter] != 0:
                                new_axis.yaxis.set_yscale(scales[label_counter])
                            axis_counter = axis_counter + 0.05
                            label_counter = label_counter + 1
            
        else:
            for file in files:
                # Convert date/time to timestamp for x-axis
                timestamp_arr = [None] * len(file['Date'])
                for i in range(len(file['Date'])):
                    timestamp_arr[i] = DataParser.parse_date_and_time_str(file['Date'][i] + ' ' + file['Time'][i])
            
                x_axis = timestamp_arr

                # Convert level values from Strings to integers
                #y_axis = [eval(m) for m in file['LEVEL']]

                # Set the labels and plot the graph for each file

                axis[counter].set_xlabel('Timestamp')

                axis_counter = 0
            
                label_counter = 0
                for label in y_axes:
                    
                    axis[counter].set_xlabel('Timestamp')
                    if axis_counter == 0 and file.setdefault(label):
                        y_axis = [eval (m) for m in file[label]]
                        if scales[label_counter] != 0:
                             axis[counter].yaxis.set_ticks(np.arange(min(y_axis), max(y_axis), scales[label_counter]))
                        axis[counter].plot(x_axis,y_axis)
                        axis[counter].set_ylabel(label)
                        axis[counter].yaxis.label.set_color('b')
                        axis[counter].tick_params(axis='y', colors='b')
                        axis_counter = axis_counter + 1
                        label_counter = label_counter + 1
                    else:
                        if file.setdefault(label):
                            y_axis = [eval (m) for m in file[label]]
                            print(max(y_axis))
                            new_axis = axis[counter].twinx()
                            if scales[label_counter] != 0:
                                new_axis.yaxis.set_ticks(np.arange(min(y_axis), max(y_axis), scales[label_counter]))
                            new_axis.spines.right.set_position(("axes",axis_counter))
                            new_axis.set_ylabel(label)
                            new_axis.yaxis.label.set_color(y_axes_colors[label_counter])
                            new_axis.tick_params(axis='y', colors=y_axes_colors[label_counter])
                            new_axis.plot(x_axis, y_axis, color=y_axes_colors[label_counter])
                            axis_counter = axis_counter + 0.05
                            label_counter = label_counter + 1

            #axis[counter].set_xlabel('Timestamp')
            #axis[counter].set_ylabel('Level')
            #axis[counter].plot(x_axis, y_axis)
                axis[counter].title.set_text(file['filename'])
                counter = counter + 1

        # Display subplot to screen
        plt.show()