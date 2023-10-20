from DataExtractor import DataExtractor
from DataAnalyser import DataAnalyzer
from Caclucator import Calculator

data_extractor = DataExtractor('weather.csv')
data_analyzer = DataAnalyzer(data_extractor.extract_data(['Dy', 'MxT', 'MnT']))
calculator = Calculator(data_extractor, data_analyzer)
result = calculator.calculate_min_difference('MxT', 'MnT','Dy')

print(result)