# py--removecollumn
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
