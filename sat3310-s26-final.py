# vi ~/Documents/labs/SAT-3310---Final-Exam/sat3310-s26-final.py

#!/usr/bin/python3

# SAT 3310 - Final Exam
# Created by Athena Lieu (xlieu@mtu.edu)
# Date: June 18th, 2026
# Comments: This program downloads a medical facility dataset,
# analyzes it, calculates statistics about facilities, beds,
# and nurse salaries, then save the results to a text file.

# Modules

import csv
import urllib.request
from pathlib import Path

# Create a directory for the data if it doesn't exist

# Create a folder named "data" if it doesn't already exist

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Download the dataset

# # URL of the dataset
url = "http://pages.mtu.edu/~toarney/sat3310/final/medicaldata.csv"

# Location where the dataset will be saved
file_path = data_dir / "medicaldata.csv"

# Check if the file already exists to avoid redundant downloads

# Download the file only if it is not already stored locally
if not file_path.exists():
    print(f"Downloading dataset from {url}...")
    urllib.request.urlretrieve(url, file_path)
    print("Download complete.")

# Initialize variables to store the data

# Variables used to store totals and counts
facilities_count = 0
total_beds = 0

rural_salaries = 0
rural_count = 0

urban_salaries = 0
urban_count = 0

# Read the dataset and process the data

# Open and read the CSV file
with open(file_path, mode="r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    # Process each facility in the dataset
    for row in reader:

        # Count facilities
        facilities_count += 1

        # Add beds to total
        total_beds += int(row["BED"])

        # Separate rural and urban salary data
        salary = float(row["NSAL"])

        # Separate salaries into rural and urban groups
        if int(row["RURAL"]) == 1:
            rural_salaries += salary
            rural_count += 1
        else:
            urban_salaries += salary
            urban_count += 1

# Calculate averages

# Calculate average beds per facility
average_beds = total_beds / facilities_count

# Calculate average rural nurse salary
average_rural_salary = (
    rural_salaries / rural_count if rural_count > 0 else 0
)

# Calculate average urban nurse salary
average_urban_salary = (
    urban_salaries / urban_count if urban_count > 0 else 0
)

# Create output text

# Create a formatted results report
results = (
    f"Total number of facilities: {facilities_count}\n"
    f"Total number of beds: {total_beds}\n"
    f"Average number of beds per facility: {average_beds:.2f}\n"
    f"Average rural nurse salary: {average_rural_salary:.2f}\n"
    f"Average urban nurse salary: {average_urban_salary:.2f}\n"
)

# Display results

# Display the results on the screen
print(results)

# Write results to file

# Create the output file path
output_file = data_dir / "results.txt"

# Save the results to a text file
with open(output_file, "w") as outfile:
    outfile.write(results)

# Confirm that the file was written successfully
print(f"Results written to {output_file}")