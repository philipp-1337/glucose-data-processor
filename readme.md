# Glucose Data Processor

## Overview
This Python script is designed to process glucose monitoring data from a CSV file downloaded from LibreView. It cleans and transforms the data by removing unnecessary columns, combining relevant glucose measurement columns, filtering data based on specific date-time ranges, and finally sorting the results in ascending order by date-time.

## Features
- **Data Cleaning:** Combines "Glukosewert-Verlauf mg/dL" and "Glukose-Scan mg/dL" into a single column ("BG") while removing all other columns.
- **Error Handling:** Safely converts glucose data to numeric format, excluding invalid or non-numeric values.
- **Date-Time Formatting:** Adjusts the format of the "Gerätezeitstempel" column to "DD-MM-YYYY HH:MM".
- **Data Filtering:** Filters rows based on specified date-time ranges for selected dates.
- **Sorting:** Orders the filtered results in ascending order based on the date-time column.
- **Output:** Generates a cleaned and filtered CSV file with only the necessary columns, renamed for readability.

## Requirements
- Python 3.x
- Libraries:
  - `pandas`

You can install the dependencies using the following command:
 ```bash
pip install -r requirements.tx
 ```

## How to Use
1.	Set Up Your Environment:
* Create and activate a virtual environment (optional but recommended):
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
 ```
* Install dependencies:
 ```bash
pip install -r requirements.txt
 ```
2.	Prepare Your CSV File:
* Ensure you have a CSV file exported from LibreView. The file should include columns such as “Gerätezeitstempel”, “Glukosewert-Verlauf mg/dL”, and “Glukose-Scan mg/dL”.
* Place the file in the same directory as the script or have its location ready.
3.	Run the Script:
* Execute the script by running:
 ```bash
python glucose_data_processor.py
 ```
* Use the file selection dialog to choose your CSV file.

4.	Review the Output:
* The processed data will be saved in a file named filtered_glucose.csv in the same directory as the script.

## Customization
* Date-Time Filtering:
* The script uses hardcoded date-time ranges to filter data. You can modify the time_ranges list in the script to customize the filtering criteria:
```python
time_ranges = [
    ("20-01-2025 07:19", "20-01-2025 16:05"),
    ("21-01-2025 03:58", "21-01-2025 10:25"),
]
```
* Column Names:
* If your dataset uses different column names, update the script to match those column names in the pd.read_csv and data processing sections.

## Known Limitations
* Input File Format: The script assumes the input CSV file follows the format exported by LibreView. Any deviations may require script modifications.
* Hardcoded Date-Time Ranges: The filtering is static and based on pre-defined ranges. For more dynamic filtering, user input or external configuration would be required.
* Locale-Specific Parsing: The script assumes a dayfirst=True format for dates. Adjust if the date format differs.

## Contributing
Contributions to improve or extend the script are welcome. Feel free to:
* Fork the repository
* Make changes or enhancements
* Submit a pull request with a detailed description of the changes

## License
This project is open-source and available under the MIT License.

## Acknowledgments
This script was created to simplify and streamline glucose data analysis, particularly for LibreView datasets.