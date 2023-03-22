import json, xmltodict, csv

from DataParser import DataParser
from DataTrimmer import DataTrimmer
from GraphPlotter import GraphPlotter

#Log contains all of the data
def main():
    
    
    # Open files here
    f1_data = DataParser.parse_csv('F1\'19 Bostwick.csv')
    f2_data = DataParser.parse_csv('F1\'19 Lowery In.csv')
    f3_data = DataParser.parse_csv('F1\'19 Lowery Out.csv')
    f4_data = DataParser.parse_csv('F1\'19 Newton E.csv')
    f5_data = DataParser.parse_csv('F1\'19 Newton W.csv')
    #f6_data = DataParser.parse_csv('June-Aug 2019 Weather Data.csv')
    f7_data = DataParser.parse_csv('F1\'19 Phillip Out.csv')
    f8_data = DataParser.parse_csv('F1\'19 Bostwick.csv')

    #print(f2_data['filename'])

    # Add files to array
    fileArr = [f2_data,f3_data]

    # use min/max to plot graph
    minimum, maximum = DataParser.parseDates(fileArr)

    print(minimum)

    # Trim the files to share the same timeframe
    graph_files = DataTrimmer.trim_data(fileArr, minimum, maximum)

    # TO-DO: Add graph options for setting dual axis
    # Graph the files

    y_axes = ['ms','LEVEL','TEMPERATURE', 'CONDUCTIVITY'] #- add as parameter to plot_graph method
    GraphPlotter.plot_graph(graph_files,y_axes)


    # if label contains input axis label, use it (?)


main()

# look into graphing library to display
# multiple graphs side by side 
# line up by shared timeframe
# 8-9 maximum files of site data

# 0.5) parse for date/time channels or separate date & time header
# 1) trim files by time frame = first step
# 2) find graphing side-by-side stuff
# maybe spit out into html or pdf?