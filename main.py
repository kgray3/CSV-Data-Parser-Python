import json, xmltodict, csv

from DataParser import DataParser
from DataTrimmer import DataTrimmer
from GraphPlotter import GraphPlotter

#Log contains all of the data
def main():
    
    
    # Open files here - add variables for each file you want to open
    f1_data = DataParser.parse_csv('F1\'19 Bostwick.csv')
    f2_data = DataParser.parse_csv('F1\'19 Lowery In.csv')
    #f3_data = DataParser.parse_csv('F1\'19 Lowery Out.csv')
    #f4_data = DataParser.parse_csv('F1\'19 Newton E.csv')
    #f5_data = DataParser.parse_csv('F1\'19 Newton W.csv')
    f6_data = DataParser.parse_csv('June-Aug 2019 Weather Data.csv')
    #f7_data = DataParser.parse_csv('F1\'19 Phillip Out.csv')
    #f8_data = DataParser.parse_csv('F1\'19 Bostwick.csv')


    # Add files to array
    fileArr = [f1_data,f2_data,f6_data]

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
    y_axes = ['TEMPERATURE', 'CONDUCTIVITY',"Rain, mm (LGR S/N: 20624173, SEN S/N: 20627658)"] 
    
    # Y AXIS SCALES GET SET IN THIS ARRAY -- LINE UP WHAT SCALE YOU WANT
    # WITH THE CORRESPONDING LABEL IN y_axes -- 0 = USE DEFAULT SCALE
    scales = [0,0,0]
    GraphPlotter.plot_graph(graph_files,y_axes, scales)



main()

# look into graphing library to display
# multiple graphs side by side 
# line up by shared timeframe
# 8-9 maximum files of site data

# 0.5) parse for date/time channels or separate date & time header 
# 1) trim files by time frame = first step
# 2) find graphing side-by-side stuff
# maybe spit out into html or pdf?