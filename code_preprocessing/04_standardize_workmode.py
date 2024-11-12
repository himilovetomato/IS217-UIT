import pandas as pd

files = ['2022.csv', '2019.csv']

for file in files:
    df = pd.read_csv(f'your_path/{file}', encoding='UTF-8', low_memory=False)

    if file == '2022.csv':
        df["RemoteWork"] = df["RemoteWork"].replace({
            'Fully remote': 'Remote',
            'Fully in-person': 'In-person'
        })
    elif file == '2019.csv':
        df = df.rename(columns={"WorkRemote": "RemoteWork"})
        df["RemoteWork"] = df["RemoteWork"].replace({
			'It\'s complicated': "Hybrid (some remote, some in-person)",
            'All or almost all the time (I\'m full-time remote)': 'Remote',
            'Less than once per month / Never': 'In-person',
            'More than half, but not all, the time': 'In-person',
            'About half the time': 'In-person',
            'Less than half the time, but at least one day each week': 'In-person',
            'A few days each month': 'In-person'
		})
    
    df.to_csv(f'your_path/{file}', index=False)
    print(f"Processed file: {file}, saved as: {file}")
        

