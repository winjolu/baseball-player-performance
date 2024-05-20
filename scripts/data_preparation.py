import pandas as pd
import os

# Define the base directory
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# Load CSV files with absolute paths
print("Loading data...")
batting = pd.read_csv(os.path.join(base_dir, 'core', 'Batting.csv'))
pitching = pd.read_csv(os.path.join(base_dir, 'core', 'Pitching.csv'))
fielding = pd.read_csv(os.path.join(base_dir, 'core', 'Fielding.csv'))
salaries = pd.read_csv(os.path.join(base_dir, 'contrib', 'Salaries.csv'))
hall_of_fame = pd.read_csv(os.path.join(base_dir, 'contrib', 'HallOfFame.csv'))
people = pd.read_csv(os.path.join(base_dir, 'core', 'People.csv'))
cpi_data = pd.read_csv(os.path.join(base_dir, 'cpi.csv'))

# Extract the year from the 'Date' column in CPI data
cpi_data['Year'] = pd.to_datetime(cpi_data['Date']).dt.year

# Filter the data to only include years 1920-2013
cpi_data = cpi_data[(cpi_data['Year'] >= 1920) & (cpi_data['Year'] <= 2013)]
salaries = salaries[(salaries['yearID'] >= 1920) & (salaries['yearID'] <= 2013)]
batting = batting[(batting['yearID'] >= 1920) & (batting['yearID'] <= 2013)]
pitching = pitching[(pitching['yearID'] >= 1920) & (pitching['yearID'] <= 2013)]
fielding = fielding[(fielding['yearID'] >= 1920) & (fielding['yearID'] <= 2013)]
hall_of_fame = hall_of_fame[(hall_of_fame['yearID'] >= 1920) & (hall_of_fame['yearID'] <= 2013)]

# Merge the CPI data with the salaries data on the year
salaries = salaries.merge(cpi_data[['Year', 'Index']], left_on='yearID', right_on='Year', how='left')

# Calculate adjusted salary
salaries['adjusted_salary'] = salaries['salary'] / (salaries['Index'] / 100)

# Rename columns to avoid conflicts during merge
batting = batting.rename(columns={'G': 'G_batting', 'H': 'H_batting', 'AB': 'AB_batting'})
pitching = pitching.rename(columns={'G': 'G_pitching', 'H': 'H_pitching'})
fielding = fielding.rename(columns={'G': 'G_fielding'})

# Merge tables on playerID
batting_salaries = pd.merge(batting, salaries, on=['playerID', 'yearID', 'teamID'], how='left')
pitching_salaries = pd.merge(pitching, salaries, on=['playerID', 'yearID', 'teamID'], how='left')
fielding_salaries = pd.merge(fielding, salaries, on=['playerID', 'yearID', 'teamID'], how='left')

# Merge performance tables into a single DataFrame
performance_data = pd.merge(batting_salaries, pitching_salaries, on=['playerID', 'yearID', 'teamID'], how='outer')
performance_data = pd.merge(performance_data, fielding_salaries, on=['playerID', 'yearID', 'teamID'], how='outer')

# Merge Hall of Fame data
performance_data = pd.merge(performance_data, hall_of_fame[['playerID', 'inducted']], on='playerID', how='left')

# Ensure consistent types for all columns
for col in performance_data.columns:
    if performance_data[col].dtype == object:
        performance_data[col] = performance_data[col].astype(str)

# Handle missing values and outliers
performance_data.fillna(0, inplace=True)  # Filling NA values with 0 for simplicity

# Standardize performance metrics (Example for batting average)
if 'H_batting' in performance_data.columns and 'AB_batting' in performance_data.columns:
    performance_data['batting_avg'] = performance_data['H_batting'] / performance_data['AB_batting']
    performance_data['batting_avg'] = performance_data['batting_avg'].fillna(0)

# Add sabermetrics metrics (e.g., OBP, SLG, OPS without WAR and FIP)
performance_data['1B'] = performance_data['H_batting'] - performance_data['2B'] - performance_data['3B'] - performance_data['HR_x']
performance_data['TB'] = performance_data['1B'] + 2 * performance_data['2B'] + 3 * performance_data['3B'] + 4 * performance_data['HR_x']
performance_data['OBP'] = (performance_data['H_batting'] + performance_data['BB_x'] + performance_data['HBP_x']) / (performance_data['AB_batting'] + performance_data['BB_x'] + performance_data['HBP_x'] + performance_data['SF_x'])
performance_data['SLG'] = performance_data['TB'] / performance_data['AB_batting']
performance_data['OPS'] = performance_data['OBP'] + performance_data['SLG']

# Save the prepared data to a Parquet file for further analysis
performance_data.to_parquet(os.path.join(base_dir, 'performance_data.parquet'), index=False)

print("Data preparation completed successfully.")
