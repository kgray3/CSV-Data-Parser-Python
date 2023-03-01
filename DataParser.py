import csv
from datetime import datetime
class DataParser:
    
    # Method to obtain smallest maximum and greatest minimum timestamps across an array of files
    def parseDates(files):
        minimum: str = None
        maximum: str = None
        for f in files:
            # Need to check for the greatest minimum and the lowest maximum
            # for shared timeframe
            min_date_and_time: str = f['Date'][0] + " " + f['Time'][0]
            if minimum is None or DataParser.parse_date_and_time_str(min_date_and_time) > DataParser.parse_date_and_time_str(minimum):
                minimum = min_date_and_time
            
            max_date_and_time: str = f['Date'][len(f['Date']) - 1] + " " + f["Time"][len(f['Time']) - 1]
            if maximum is None or DataParser.parse_date_and_time_str(max_date_and_time) < DataParser.parse_date_and_time_str(maximum):
                maximum = max_date_and_time
        DataParser.parse_date_and_time_str(min_date_and_time)
        return minimum, maximum

    # Method to create date_time object based on CSV string
    def parse_date_and_time_str(s):
        datetime_object = datetime.strptime(s, '%m/%d/%Y %I:%M:%S %p')
        return datetime_object

    # Method to parse csv file into Python dictionary
    def parse_csv(fileName):
        f = open(fileName)
        for i in range(DataParser.find_date(fileName)):
            next(f)
        
        file = csv.DictReader(f)
        result = {}
        for row in file:
            for column, value in row.items():
                result.setdefault(column, []).append(value)
        return result

    # Method to find where the CSV column titles are located
    def find_date(file_name):
        file = open(file_name)
        counter = 0
        for line in file:
            counter = counter + 1
            if line.find('Date') > - 1:
                return counter - 1
        

