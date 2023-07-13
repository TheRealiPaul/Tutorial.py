import pandas as pd

# Specify the path to your Excel file
excel_file_path = "Excel tutorial\Financial Sample.xlsx"

# Read specific columns from the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path, usecols=["Country", "Product"])
df = pd.read_excel(excel_file_path, usecols=["Country", ])

# Display the contents of the DataFrame
print(df)
