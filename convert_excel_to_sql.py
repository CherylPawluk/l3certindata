import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('Messy_Sales_Data_Tredify.xlsx')

# Create an SQLite database file in the repository
engine = create_engine('sqlite:///Tredify_Sales_Data.db', echo=True)

# Save the DataFrame to an SQL database (SQLite)
df.to_sql('sales_data', con=engine, if_exists='replace', index=False)

print("Data has been saved to the SQLite database.")
