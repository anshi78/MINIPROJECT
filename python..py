import pandas as pd

# Read the CSV file
df = pd.read_csv('data/air_quality.csv')

# Print the columns to check for the correct column name
print("Columns in the DataFrame:", df.columns)

# Attempt to access the 'AQI' column (adjust name as needed)
try:
    data = df['AQI Value'].values.reshape(-1, 1)
except KeyError:
    print("Column 'AQI' not found! Available columns are:", df.columns)
    # Optionally, raise an exception or handle this case further

