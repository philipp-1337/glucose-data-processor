import pandas as pd

# Load the CSV file
df = pd.read_csv('glucose.csv', parse_dates=['Gerätezeitstempel'], dayfirst=True)

# Combine "Glukosewert-Verlauf mg/dL" and "Glukose-Scan mg/dL" into a single column
df['Glukosewert mg/dL'] = df['Glukosewert-Verlauf mg/dL'].combine_first(df['Glukose-Scan mg/dL'])

# Attempt to convert "Glukosewert mg/dL" to floats, safely handling non-numeric values
df['Glukosewert mg/dL'] = pd.to_numeric(df['Glukosewert mg/dL'], errors='coerce')

# Now drop any rows where 'Glukosewert mg/dL' could not be converted to a number (and thus is NaN)
df = df.dropna(subset=['Glukosewert mg/dL'])

# Round and convert to int
df['Glukosewert mg/dL'] = df['Glukosewert mg/dL'].astype(float).round(0).astype(int)

# Format the "Gerätezeitstempel" to remove seconds
df['Gerätezeitstempel'] = df['Gerätezeitstempel'].dt.strftime('%Y-%m-%d %H:%M')

# Keep only the necessary columns
df = df[['Gerätezeitstempel', 'Glukosewert mg/dL']]

# Re-parse the "Gerätezeitstempel" to ensure proper sorting
df['Gerätezeitstempel'] = pd.to_datetime(df['Gerätezeitstempel'], format='%Y-%m-%d %H:%M')

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
    mask = (df['Gerätezeitstempel'] >= pd.to_datetime(start)) & (df['Gerätezeitstempel'] <= pd.to_datetime(end))
    filtered_df = pd.concat([filtered_df, df.loc[mask]])

# Convert "Gerätezeitstempel" back to the desired string format without seconds for final output
filtered_df['Gerätezeitstempel'] = filtered_df['Gerätezeitstempel'].dt.strftime('%Y-%m-%d %H:%M')

# Save the cleaned and filtered data to a new CSV file
filtered_df.to_csv('filtered_glucose_no_seconds.csv', index=False)

print("Data processing complete. The filtered data is saved in 'filtered_glucose_no_seconds.csv'.")
