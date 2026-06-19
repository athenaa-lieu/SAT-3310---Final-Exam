# vi ~/Documents/labs/SAT-3310---Final-Exam/sat3310-s26-final.py

#!/usr/bin/python3

# SAT 3310 - Final Exam
# Created by Athena Lieu (xlieu@mtu.edu)
# Date: June 18th, 2026
# Comments:

# Modules

import csv
import urllib.request
from pathlib import Path

# Create a directory for the data if it doesn't exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Download the dataset

url = "http://pages.mtu.edu/~toarney/sat3310/final/medicaldata.csv"
file_path = data_dir / "medicaldata.csv"

# Check if the file already exists to avoid redundant downloads

if not file_path.exists():
    print(f"Downloading dataset from {url}...")
    urllib.request.urlretrieve(url, file_path)
    print("Download complete.")

# Initialize variables to store the data

facilities_count = 0
total_beds = 0

rural_salaries = 0
rural_count = 0

urban_salaries = 0
urban_count = 0

# Read the dataset and process the data

with open(file_path, mode="r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        # Count facilities

        facilities_count += 1

        # Add beds to total

        total_beds += int(row["BED"])

        # Separate rural and urban salary data

        salary = float(row["NSAL"])

        if int(row["RURAL"]) == 1:
            rural_salaries += salary
            rural_count += 1
        else:
            urban_salaries += salary
            urban_count += 1

# Calculate averages

average_beds = total_beds / facilities_count

average_rural_salary = (
    rural_salaries / rural_count if rural_count > 0 else 0
)

average_urban_salary = (
    urban_salaries / urban_count if urban_count > 0 else 0
)

# Create output text

results = (
    f"Total number of facilities: {facilities_count}\n"
    f"Total number of beds: {total_beds}\n"
    f"Average number of beds per facility: {average_beds:.2f}\n"
    f"Average rural nurse salary: {average_rural_salary:.2f}\n"
    f"Average urban nurse salary: {average_urban_salary:.2f}\n"
)

# Display results

print(results)

# Write results to file

output_file = data_dir / "results.txt"

with open(output_file, "w") as outfile:
    outfile.write(results)

print(f"Results written to {output_file}")