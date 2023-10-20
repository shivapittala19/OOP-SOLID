class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_min_difference(self, column_name1, column_name2,column_name3):
        min_diff = float('inf') # initial minimum value as infinity
        min_diff_item = None
        for item in self.data:
            diff = abs(int(item[column_name1]) - int(item[column_name2])) 
            if diff < min_diff:
                min_diff = diff #update the new minimum
                min_diff_item = item #update the corresponding newitem
        return min_diff_item[column_name3]
