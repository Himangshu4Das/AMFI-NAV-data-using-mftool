# AMFI-NAV-data-using-mftool
This codes fetches both historical and latest NAV data of all the listed schemes using mftool package in python.

# AMFI-NAV-data-using-mftool implementation

This script fetches historical NAV data for mutual funds from the Mftool API and saves it to a CSV file. The script uses the Mftool library to fetch scheme codes and historical NAV data for mid-cap, small-cap, and flexi-cap mutual funds.

## Requirements

- Python 3
- pandas library
- mftool library

## Usage

1. Clone the repository to your local machine.
2. Update the start_date and end_date variables in the script to the desired date range.
3. Run the script:
```
python AMFI_MF_NAV_Complete.ipynb
```
5. The script will generate a CSV file named 'MF_NAV_DATA.csv' in the same directory as the script.

## Output

The generated CSV file contains the following columns:
- scheme_code: the unique identifier for the mutual fund scheme
- scheme_name: the name of the mutual fund scheme
- date: the date for which the NAV data is provided
- nav: the NAV for the mutual fund scheme on the given date

Note: the script processes the data to keep only the latest records for each scheme. If you want to keep all the records, remove the processing step in the script.
