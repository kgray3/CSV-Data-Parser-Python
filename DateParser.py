import csv
class DateParser:
    def parseDates(files):
        minimum: str = None
        maximum: str = None
        for f in files:
            # Need to check for the greatest minimum and the lowest maximum
            # for shared timeframe
            min_date_and_time: str = f["Date"][0] + " " + f["Time"][0]
            if minimum is None or min_date_and_time > minimum:
                minimum = min_date_and_time
            
            max_date_and_time: str = f["Date"][len(f[i]) - 1] + " " + f["Time"][len(f) - 1]
            if maximum is None or max_date_and_time < maximum:
                maximum = max_date_and_time

            return min_date_and_time + " | " +  max_date_and_time
    
    def parse_csv(fileName):
        f = open(fileName)
        counter = 0
        for i in range(DateParser.find_date(fileName)):
            next(f)
        
        file = csv.DictReader(f)
        result = {}
        for row in file:
            # need to skip first 11 lines somehow
            for column, value in row.items():
                result.setdefault(column, []).append(value)
        return result

    def find_date(file_name):
        file = open(file_name)
        counter = 0
        for line in file:
            counter = counter + 1
            #print(line.find('Date'))
            if line.find('Date') > - 1:
                print(line)
                print(counter)

                return counter - 1
            #next(file)
        

