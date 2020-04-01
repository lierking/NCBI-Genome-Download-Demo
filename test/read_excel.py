import pandas as pd

f = input('文件名：')
sheet = input('表名：')
xlsx = pd.ExcelFile(f)
df = pd.read_excel(xlsx, sheet)
print(df)
