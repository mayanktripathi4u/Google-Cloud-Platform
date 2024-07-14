import pandas as pd

xlFile = './data/source/Sample_Excel.xlsx'
output_file = './data/source/excel_to_csv_pandas.csv'

df = pd.read_excel(xlFile)

print(df.head())

df.to_csv(output_file, index=False)