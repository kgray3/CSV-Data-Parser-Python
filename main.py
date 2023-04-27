import json, xmltodict, csv

from DataParser import DataParser
from DataTrimmer import DataTrimmer
from GraphPlotter import GraphPlotter

#Log contains all of the data
def main():
    
    #NOTE: CSV FILES MUST HAVE ONE LINE OF EMPTY SPACE AT THE TOP

    # Open files here - add variables for each file you want to open
    #f1_data = DataParser.parse_csv('20 Spring Lowery In.csv')
    f2_data = DataParser.parse_csv('F1\'19 Lowery In.csv')
    f3_data = DataParser.parse_csv('F1\'19 Lowery Out.csv')
    #f4_data = DataParser.parse_csv('F1\'19 Newton E.csv')
    #f5_data = DataParser.parse_csv('F1\'19 Newton W.csv')
    #f6_data = DataParser.parse_csv('Spring 2020 Weather Data.csv')
    #f7_data = DataParser.parse_csv('F1\'19 Phillip Out.csv')
    #f8_data = DataParser.parse_csv('F1\'19 Bostwick.csv')

    

    # Add files to array
    fileArr = [f2_data, f3_data]

    # use min/max to plot graph
    minimum, maximum = DataParser.parseDates(fileArr)

    print(minimum)

    # Trim the files to share the same timeframe, minimum and maximum can be edited
    # here to set an arbitrary timestamp. The format is MM/DD/YYYY HH:MM:SS AM/PM
    graph_files = DataTrimmer.trim_data(fileArr, minimum, maximum)

    # TO-DO: fix graph colors and add parsing for the Weather Data csv
    # Graph the files

    # axes to be included for the data
    # level = blue, temperature = red  
    y_axes = ['TEMPERATURE', 'CONDUCTIVITY'] 
    
    # Y AXIS SCALES GET SET IN THIS ARRAY -- LINE UP WHAT SCALE YOU WANT
    # WITH THE CORRESPONDING LABEL IN y_axes -- 0 = USE DEFAULT SCALE
    scales = [0,0]
    # Y AXIS COLORS GET SET IN THIS ARRA -- LINE UP WHAT COLOR YOU WANT
    # WITH THE CORRESPONDING LABEL IN y_axes
    colors = ['r','g']
    GraphPlotter.plot_graph(graph_files,y_axes, scales, colors)



main()

