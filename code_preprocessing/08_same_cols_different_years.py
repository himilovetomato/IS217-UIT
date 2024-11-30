import pandas as pd

def fix_same_cols_different_years(source_path, des_path, combine_dict):
    df = pd.read_csv(source_path)
    
    for separationYear, colMap in combine_dict.items():
        dfBefore = df[df['Year'] <= separationYear]
        dfAfter =  df[df['Year'] > separationYear]
        for targetCol, orgCol in colMap.items():
            upperSeries = dfAfter[targetCol]
            lowerSeries = dfBefore[orgCol]
            df[targetCol] = pd.concat([upperSeries, lowerSeries], axis=0)
            df[targetCol].reset_index(drop=True)
        removeCols = [c for c in colMap.values() if c != 'ConvertedComp']
        df.drop(columns=removeCols, inplace=True)
    print(len(df.columns))
    df.to_csv(des_path, index=False)
    

# Schema of truth dict:
# {
#     <separationYear>: {
#         <targetCol>: <orgCol>
#     }
# }
# <targetCol> is the column name that will be used in the final dataset
# <orgCol> will become <targetCol> after running this script
truth_dict = {
    2020: {
        "DatabaseHaveWorkedWith": "DatabaseWorkedWith",
        "LanguageHaveWorkedWith": "LanguageWorkedWith",
        "MiscTechHaveWorkedWith": "MiscTechWorkedWith",
        "NEWCollabToolsHaveWorkedWith": "NEWCollabToolsWorkedWith",
        "PlatformHaveWorkedWith": "PlatformWorkedWith",
        "ConvertedCompYearly": "ConvertedComp"
    },
    2023: {  
        "AISearchDevHaveWorkedWith": "AISearchHaveWorkedWith",
    },
}

# Run
# Please substitute the source & dest paths with the correct one
source_path = '../6years_preprocessing.csv'
dest_path = '../6years_preprocessing.csv'
fix_same_cols_different_years(source_path, dest_path, truth_dict)
