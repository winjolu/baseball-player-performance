import pandas as pd
import os

# Define the base directory
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# Load CSV files with absolute paths
batting = pd.read_csv(os.path.join(base_dir, 'core', 'Batting.csv'))
pitching = pd.read_csv(os.path.join(base_dir, 'core', 'Pitching.csv'))
fielding = pd.read_csv(os.path.join(base_dir, 'core', 'Fielding.csv'))
salaries = pd.read_csv(os.path.join(base_dir, 'contrib', 'Salaries.csv'))
hall_of_fame = pd.read_csv(os.path.join(base_dir, 'contrib', 'HallOfFame.csv'))
people = pd.read_csv(os.path.join(base_dir, 'core', 'People.csv'))

# Rename columns to avoid conflicts during merge
batting = batting.rename(columns={'G': 'G_batting', 'H': 'H_batting', 'AB': 'AB_batting'})
pitching = pitching.rename(columns={'G': 'G_pitching', 'H': 'H_pitching'})
fielding = fielding.rename(columns={'G': 'G_fielding'})

# Print columns to debug
print("Batting columns:", batting.columns)
print("Pitching columns:", pitching.columns)
print("Fielding columns:", fielding.columns)
print("Salaries columns:", salaries.columns)
print("HallOfFame columns:", hall_of_fame.columns)
print("People columns:", people.columns)

# Merge tables on playerID
batting_salaries = pd.merge(batting, salaries, on=['playerID', 'yearID', 'teamID'], how='left')
pitching_salaries = pd.merge(pitching, salaries, on=['playerID', 'yearID', 'teamID'], how='left')
fielding_salaries = pd.merge(fielding, salaries, on=['playerID', 'yearID', 'teamID'], how='left')

# Print columns after merging with salaries
print("Batting+Salaries columns:", batting_salaries.columns)
print("Pitching+Salaries columns:", pitching_salaries.columns)
print("Fielding+Salaries columns:", fielding_salaries.columns)

# Merge performance tables into a single DataFrame
performance_data = pd.merge(batting_salaries, pitching_salaries, on=['playerID', 'yearID', 'teamID'], how='outer')
performance_data = pd.merge(performance_data, fielding_salaries, on=['playerID', 'yearID', 'teamID'], how='outer')

# Print columns after merging performance data
print("Performance Data columns (before HallOfFame merge):", performance_data.columns)

# Merge Hall of Fame data
performance_data = pd.merge(performance_data, hall_of_fame[['playerID', 'inducted']], on='playerID', how='left')

# Print columns after merging with Hall of Fame data
print("Performance Data columns (after HallOfFame merge):", performance_data.columns)

# Handle missing values and outliers
performance_data.fillna(0, inplace=True)  # Filling NA values with 0 for simplicity

# Standardize performance metrics (Example for batting average)
if 'H_batting' in performance_data.columns and 'AB_batting' in performance_data.columns:
    performance_data['batting_avg'] = performance_data['H_batting'] / performance_data['AB_batting']
    performance_data['batting_avg'] = performance_data['batting_avg'].fillna(0)
else:
    print("Columns 'H_batting' and 'AB_batting' are not in the DataFrame")

# Save the prepared data to a CSV file for further analysis
performance_data.to_csv(os.path.join(base_dir, 'performance_data.csv'), index=False)
