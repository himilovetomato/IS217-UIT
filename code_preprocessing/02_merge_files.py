import pandas as pd
import os

def merge_columns(input_path, output_path):
    dataframes = []
    # Get a list of all CSV files in the directory
    all_files = [f for f in os.listdir(input_path) if f.endswith('.csv')]
    
    # Process columns that appear in more than one file
    for filename in all_files:
        file_path = os.path.join(input_path, filename)
        df = pd.read_csv(file_path, encoding='UTF-8', low_memory=False)
     
        dataframes.append(df)
        
    # Concatenate all DataFrames along the row axis
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the merged DataFrame to a new CSV file
    output_file = os.path.join(output_path, 'combine_6years.csv')
    merged_df.to_csv(output_file, index=False)
    print(f"\nMerged columns saved to {output_file}")

input_path = 'your path'
output_path = 'your path'
merge_columns(input_path, output_path)