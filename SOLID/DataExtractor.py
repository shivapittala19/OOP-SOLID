class DataExtractor:
    def __init__(self, filename):
        self.filename = filename

    def extract_data(self, column_names):
        data = [] 
        # read the csv files
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            # headers
            headers = lines[0].split(',')
            for line in lines[1:]:
                values = line.split(',')
                # Getting the values of the required Column
                record = {column_names[i]: values[headers.index(column_names[i])] for i in range(len(column_names))}
                data.append(record)
        return data

    
