import pandas as pd 

df = pd.read_csv('your_path', encoding='UTF-8', low_memory=False)

df = df.fillna('Unknown')
df = df.replace('', 'Unknown')

df.to_csv('your_path', index=False)
