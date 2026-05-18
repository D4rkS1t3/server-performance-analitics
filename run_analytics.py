import pandas as pd

df1 = pd.read_csv('server_info.csv')
df2 = pd.read_csv('server_metrics.csv')

df3 = pd.merge(df1, df2, on='server_id')

naGranicy = df3[
    ((df3['environment'] == 'PROD') & (df3['cpu_usage'] > 85) & (df3['ram_usage'] > 70))
]

pd.DataFrame(naGranicy).to_csv('heavy_load_report.csv', index=False)

df3['cpu_free'] = 100 - df3['cpu_usage']
df3['ram_free'] = 100 - df3['ram_usage']

df3_grouped = df3.groupby('server_name', as_index=False).agg({
    'cpu_usage': 'mean',
    'ram_usage': 'mean',
    'cpu_free': 'mean',
    'ram_free': 'mean'
})

df3_grouped['cpu_usage'] = df3_grouped['cpu_usage'].round(1)
df3_grouped['ram_usage'] = df3_grouped['ram_usage'].round(1)
df3_grouped['cpu_free'] = df3_grouped['cpu_free'].round(1)
df3_grouped['ram_free'] = df3_grouped['ram_free'].round(1)

pd.DataFrame(df3_grouped).to_csv('server_efficiency_stats.csv', index=False)

print("      /`·.¸")
print("     /¸...¸`:·")
print(" ¸.·´  ¸   `·.¸.·´)")
print(": © ):´;      ¸  {")
print(" `·.¸ `·  ¸.·´\\`·¸)")
print("     `\\\\´´\\¸.·´")
