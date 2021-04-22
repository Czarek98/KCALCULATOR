import pandas as pd
csvFilePath = r'kcalCSV.csv'
jsonFilePath = r'foodJSON2.json'

csv = pd.read_csv(csvFilePath)
json = csv.to_json()
with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json)
