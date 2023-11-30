# import csvcd
import csv
import pprint
# import pandas
#import pandas as pd
# read csv file to a list of dictionaries


with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
print(data)
print ("hello")