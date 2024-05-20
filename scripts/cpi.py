import pandas as pd
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Check if the file exists using an absolute path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'cpi.csv'))
print("Looking for file at:", file_path)
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} does not exist")

# Load the CPI data
cpi_data = pd.read_csv(file_path)

# Display the first few rows of the CPI data
print(cpi_data.head())
