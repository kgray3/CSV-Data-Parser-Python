from DataParser import DataParser
class DataTrimmer:

    # Trim the data based on a calculated minimum & maximum timestamp
    def trim_data(files, minimum_timestamp, maximum_timestamp):
        trimmed_files = []
        for file in files:
            f_new = DataTrimmer.trim_end(DataTrimmer.trim_beginning(file, minimum_timestamp), maximum_timestamp)
            trimmed_files.append(f_new)

        return trimmed_files
    
    # Trim the beginning of a file based on a shared minimum timeframe
    def trim_beginning(file, minimum_timestamp):
        counter = 0
        for i in range(len(file['Date'])):
            timestamp = file['Date'][i] + ' ' + file['Time'][i]
            # if the timestamp is below the minimum, increment the counter
            if DataParser.parse_date_and_time_str(timestamp) < DataParser.parse_date_and_time_str(minimum_timestamp):
                counter = counter + 1
            # when we are within the desired timeframe, trim the beginning using the counter and return the new file
            if DataParser.parse_date_and_time_str(timestamp) >= DataParser.parse_date_and_time_str(minimum_timestamp):
                for k in range(counter):
                    for m in file.keys():
                        file[m].pop(0)
                return file
    
    # Method to trim the end of a file based on a desired timeframe, goes backwards until timeframe is reached
    # basically the reverse of trim_beginning
    def trim_end(file, maximum_timestamp):
        counter = 0
        for i in range(len(file['Date'])):
            timestamp = file['Date'][len(file['Date']) - 1 - i] + ' ' + file['Time'][len(file['Time']) - 1 - i]
            # If a time is greater than the maximum, increment counter
            if DataParser.parse_date_and_time_str(timestamp) > DataParser.parse_date_and_time_str(maximum_timestamp):
                counter = counter + 1
            # Once the timestamp is within the timeframe, trim the excess using counter and return the edited file
            if DataParser.parse_date_and_time_str(timestamp) <= DataParser.parse_date_and_time_str(maximum_timestamp):
                for k in range(counter):
                    for m in file.keys():
                        file[m].pop(len(file[m])-1)          
                return file
        
