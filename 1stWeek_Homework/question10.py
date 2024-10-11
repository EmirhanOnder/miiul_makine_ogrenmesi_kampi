import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col.upper()+"_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns]