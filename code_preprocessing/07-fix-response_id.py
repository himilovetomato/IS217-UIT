import pandas as pd

# Transform the column 'ResponseId' in the csv dataset (fix null values)
def fixResponseId(source_path: str, dest_path: str) -> None:    
    df = pd.read_csv(source_path)

    # Add an auto-increasing integer column
    df['ResponseId'] = range(1, len(df) + 1)
    df.to_csv(dest_path, index=False)

# Run
# Please substitute the source & dest paths with the correct one
source_path = '../6years_preprocessing.csv'
dest_path = '../6years_preprocessing.csv'
fixResponseId(source_path, dest_path)