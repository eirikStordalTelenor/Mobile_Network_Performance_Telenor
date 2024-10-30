import os
import pandas as pd

def combine_csv_files_to_dataframe(input_folder):
    # Create an empty list to hold DataFrames
    all_dataframes = []

    # Loop through all files in the specified folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):  # Check if the file is a CSV
            file_path = os.path.join(input_folder, filename)
            df = pd.read_csv(file_path)  # Read each CSV into a DataFrame
            all_dataframes.append(df)    # Append the DataFrame to the list

    # Combine all DataFrames in the list into one
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Return the combined DataFrame
    return combined_df

# Example usage
input_folder = 'OoklaMobilePerformance_Telenor'  # Replace with the path to your folder containing CSVs

# Get the combined DataFrame
combined_df = combine_csv_files_to_dataframe(input_folder).cache()
