import pandas as pd

input_path = 'your_path'
output_path = 'your_path'

cols = [
	"YearsCode",
	"YearsCodePro",
	"Age1stCode",
    "Age",
]
replace_dict = {
    'Less than 1 year': '0', 
    'More than 50 years': '51',
    'Younger than 5 years': '4', 
    'Older than 85': '86',
    'Older than 64': '65',
    'Older than 64 years': '65',
    "Under 18 years old": "17",
    "Prefer not to say": None,
    "65 years or older": "65",
}

# Calculate the average for ranges of ages (Ex: 20 - 25 years)
def calculate_age_range(df, *cols):
    for col in cols:
        age_ranges = df[col].str.extract(r'(\d+)\s*-\s*(\d+)')
        age_ranges = age_ranges.apply(pd.to_numeric, errors='coerce')
        df[col] = age_ranges.mean(axis=1).combine_first(df[col])
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df[col]

def replace_values(df, columns, replace_dict):
    for col in columns:
        df[col] = df[col].replace(replace_dict)

def main():
    try:
        df = pd.read_csv(input_path, encoding='UTF-8', low_memory=False)
        
        cols = ["Age", "Age1stCode"]
        replace_values(df, cols, replace_dict)
        
        calculate_cols = ["Age", "Age1stCode"]
        df = calculate_age_range(*calculate_cols)
        
        df.to_csv(output_path, index=False)
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
