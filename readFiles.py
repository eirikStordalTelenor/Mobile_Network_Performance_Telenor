from zipfile import ZipFile

import os
import pandas as pd


def combine_csv_files(input_folder, output_file):
    # Create an empty list to hold DataFrames
    all_dataframes = []

    # Loop through all files in the specified folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):  # Check if the file is a CSV
            file_path = os.path.join(input_folder, filename)
            df = pd.read_csv(file_path)  # Read each CSV into a DataFrame
            all_dataframes.append(df)  # Append the DataFrame to the list

    # Combine all DataFrames in the list into one
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Save the combined DataFrame to the output CSV file
    combined_df.to_csv(output_file, index=False)

    print(f"Combined CSV saved as: {output_file}")


# Example usage
input_folder = 'workshop/OoklaData/OoklaMobilePerformance_Telenor'  # Replace with the path to your folder containing CSVs
output_file = 'combined_ookla.csv'  # Specify the name of the output file

combine_csv_files(input_folder, output_file)
