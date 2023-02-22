import json, xmltodict, csv

from DateParser import DateParser

#Log contains all of the data
def main():

    

    #f1 = open("testfile.xle","r")
    f1_data = DateParser.parse_csv('3.csv')
 
    f2_data = DateParser.parse_csv('2.csv')

    print(f1_data.keys())
    #fileArr = [f1_data, f2_data]

    #print(DateParser.parseDates(fileArr))


main()

# look into graphing library to display
# multiple graphs side by side 
# line up by shared timeframe
# 8-9 maximum files of site data

# 0.5) parse for date/time channels or separate date & time header
# 1) trim files by time frame = first step
# 2) find graphing side-by-side stuff
# maybe spit out into html or pdf?