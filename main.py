import json, xmltodict, csv

from DataParser import DataParser

#Log contains all of the data
def main():

    

    #f1 = open("testfile.xle","r")
    f1_data = DataParser.parse_csv('3.csv')
 
    f2_data = DataParser.parse_csv('2.csv')

    #print(f1_data['Date'][0])
    fileArr = [f1_data, f2_data]

    minimum, maximum = DataParser.parseDates(fileArr)

    print(minimum)
    print(maximum)


main()

# look into graphing library to display
# multiple graphs side by side 
# line up by shared timeframe
# 8-9 maximum files of site data

# 0.5) parse for date/time channels or separate date & time header
# 1) trim files by time frame = first step
# 2) find graphing side-by-side stuff
# maybe spit out into html or pdf?