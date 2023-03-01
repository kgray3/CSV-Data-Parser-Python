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
    f6_data = DataParser.parse_csv('F1\'19 Phillip level.csv')
    f7_data = DataParser.parse_csv('F1\'19 Phillip Out.csv')

    # Add files to array
    fileArr = [f1_data, f2_data, f3_data, f4_data, f5_data, f6_data, f7_data]

    # use min/max to plot graph
    minimum, maximum = DataParser.parseDates(fileArr)

    # Trim the files to share the same timeframe
    graph_files = DataTrimmer.trim_data(fileArr, minimum, maximum)

    # Graph the files
    GraphPlotter.plot_graph(graph_files)





main()

# look into graphing library to display
# multiple graphs side by side 
# line up by shared timeframe
# 8-9 maximum files of site data

# 0.5) parse for date/time channels or separate date & time header
# 1) trim files by time frame = first step
# 2) find graphing side-by-side stuff
# maybe spit out into html or pdf?