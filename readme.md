# Glucose Data Processor

## Overview
This Python script is designed to process glucose monitoring data from a CSV file downloaded from LibreView. It focuses on cleaning the data by removing unnecessary columns, combining relevant glucose measurement columns, filtering data based on specific date-time input, and finally sorting the results in ascending order by date-time.

## Features
- **Data Cleaning:** Merges "Glukosewert-Verlauf mg/dL" and "Glukose-Scan mg/dL" into a single column while removing all other columns.
- **Date-Time Formatting:** Adjusts the format of the date-time column to "DD-MM-YYYY HH:MM".
- **Data Filtering:** Keeps only the rows within specified date-time ranges for certain dates.
- **Sorting:** Orders the filtered results in descending order based on the date-time column.
- **Column Renaming:** Renames columns to "Date" and "BG" for readability.

## How to Use
1. **Prerequisites:**
   - Ensure Python 3 is installed on your system.
   - Install Pandas library: Run `pip install pandas` in your terminal or command prompt.

2. **Place the CSV File:**
   - The script expects a file named `glucose.csv` in the same directory. Ensure this file exists and follows the expected format.
   - For testing you can rename the provided test file `glucose.csv.testfile`.
   - Note: If you use the file from www.libreview.com remove the first row

3. **Running the Script:**
   - Navigate to the directory containing the script.
   - Run the script by executing `python glucose_data_processor.py` in your terminal or command prompt.

4. **Output:**
   - The script generates a file named `filtered_glucose.csv` with the processed data.

## Customization
To adjust the script for different datasets or requirements, consider modifying the following sections:
- **Data Filtering Ranges:** Edit the `time_ranges` list to include or exclude different date-time ranges.
- **Column Names and Formats:** Adjust column names and date-time formats in the script as needed for different datasets.

## Known Limitations
- The script expects the input CSV file to have specific column names as per the given dataset. Changes in the input file structure may require corresponding adjustments in the script.
- Date-time filtering is based on hardcoded ranges. Dynamic filtering based on user input or other criteria would require script modifications.

## Contributing
Contributions to improve the script or extend its functionality are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

