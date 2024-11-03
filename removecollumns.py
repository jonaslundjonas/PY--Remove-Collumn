# This script processes all CSV files in the current directory, removing columns with no data 
# below the header row and saving the cleaned data in new files with necessary headers.
# Written by Jonas Lund, 2024.
#
# Requirements:
# - Python 3.x
# - pandas library
#
# Installation:
# To install pandas, open your terminal or command prompt and run:
#     pip install pandas
#
# Usage:
# Place this script in the same directory as your CSV files. Then, run the script:
#     python removecollumns.py
#
# Output:
# For each CSV file processed, a new CSV file will be created with a "_filtered" suffix, 
# retaining only columns with data and their headers.

import os
import pandas as pd

def remove_empty_columns(csv_file_path):
    """
    This function reads a CSV file, removes columns with no data in any row below the header,
    and writes the cleaned data to a new file with necessary headers.
    Written by Jonas Lund, 2024.

    Args:
    csv_file_path (str): Path to the input CSV file.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Identify columns where all elements are empty or NaN below the header row
    columns_to_drop = [col for col in df.columns if df[col].isnull().all()]

    # Drop the identified columns
    df_cleaned = df.drop(columns=columns_to_drop)

    # Construct the new file path with a suffix "_filtered"
    new_file_path = os.path.splitext(csv_file_path)[0] + "_filtered.csv"

    # Save the cleaned DataFrame to a new CSV file, keeping the headers for columns with data
    df_cleaned.to_csv(new_file_path, index=False, header=True)

# Directory where the script and CSV files are located
directory_path = os.getcwd()

# Loop through all CSV files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv") and not filename.endswith("_filtered.csv"):
        file_path = os.path.join(directory_path, filename)
        remove_empty_columns(file_path)
        print(f"Processed and cleaned file saved as: {os.path.splitext(filename)[0]}_filtered.csv")
