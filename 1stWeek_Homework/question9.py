import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


["NUM_"+ col.upper() if df[col].dtype!="O" else col.upper() for col in df.columns]