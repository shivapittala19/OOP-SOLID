from DataExtractor import DataExtractor
from DataAnalyser import DataAnalyzer
from Caclucator import Calculator


data_extractor = DataExtractor('football.csv')
data_analyzer = DataAnalyzer(data_extractor.extract_data(['Team', 'F', 'A']))
calculator = Calculator(data_extractor, data_analyzer)
result = calculator.calculate_min_difference('F', 'A','Team')

print(result)
