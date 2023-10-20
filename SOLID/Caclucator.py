class Calculator:
    def __init__(self, data_extractor, data_analyzer):
        self.data_extractor = data_extractor
        self.data_analyzer = data_analyzer

    def calculate_min_difference(self, column_name1, column_name2,column_name3):
        # data = self.data_extractor.extract_data([column_name1, column_name2])
        min_diff_item = self.data_analyzer.find_min_difference(column_name1, column_name2,column_name3)
        return min_diff_item
