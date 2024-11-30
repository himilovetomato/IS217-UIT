import pandas as pd
import os

def add_column_to_csv(source_path, destination_path, column_name):
    # Ensure the destination folder exists
    os.makedirs(destination_path, exist_ok=True)

    for filename in os.listdir(source_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(source_path, filename)
            df = pd.read_csv(file_path, encoding='UTF-8', low_memory=False)
            
            # Extract the year from the filename
            value = filename[:4]
            # Insert the new column at the beginning of the DataFrame
            df.insert(0, column_name, value)
            
            df.to_csv(os.path.join(destination_path, filename), index=False)
        else:
            print(f"The file {filename} is not a CSV file and was skipped.")
            
input_path = 'your_path'
output_path = 'your_path'
column_name = 'Year'   

add_column_to_csv(input_path, output_path, column_name)
