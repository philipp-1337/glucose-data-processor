import pandas as pd

# Load the CSV file
df = pd.read_csv('glucose.csv', parse_dates=['Gerätezeitstempel'], dayfirst=True)

# Combine "Glukosewert-Verlauf mg/dL" and "Glukose-Scan mg/dL" into a single column
df['Glukosewert mg/dL'] = df['Glukosewert-Verlauf mg/dL'].fillna(df['Glukose-Scan mg/dL'])

# Keep only the necessary columns
df = df[['Gerätezeitstempel', 'Glukosewert mg/dL']]

# Sort by "Gerätezeitstempel"
df.sort_values(by='Gerätezeitstempel', inplace=True)

# Define the specific date and time ranges to keep
time_ranges = [
    ("2024-03-22 02:44", "2024-03-22 10:26"),
    ("2024-03-20 02:43", "2024-03-20 21:01"),
    ("2024-03-15 01:32", "2024-03-15 10:16"),
    ("2024-03-12 01:25", "2024-03-12 07:05"),
    ("2024-03-05 00:01", "2024-03-05 21:05"),
    ("2024-03-04 02:15", "2024-03-04 23:59"),
]

# Filter the data based on the specified date and time ranges
filtered_df = pd.DataFrame()
for start, end in time_ranges:
    mask = (df['Gerätezeitstempel'] >= start) & (df['Gerätezeitstempel'] <= end)
    filtered_df = pd.concat([filtered_df, df.loc[mask]])

# Save the cleaned and filtered data to a new CSV file
filtered_df.to_csv('filtered_glucose.csv', index=False)

print("Data processing complete. The filtered data is saved in 'filtered_glucose.csv'.")