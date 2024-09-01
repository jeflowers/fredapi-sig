```python
import matplotlib.pyplot as plt
import pandas as pd

# Assume we've already set up the FredPyAPI instance with proper verification
fred_api = FredPyAPI()
fred_api.set_public_key("your_public_key_here")
fred_api.set_token("your_token_here", "your_token_signature_here")

# Fetch data (assuming these methods exist)
black_male_employment = fred_api.get_series_data("LNS12000006")
illegal_immigration_proxy = fred_api.get_series_data("NETMIGUS")  # Net migration as a proxy

# Convert to pandas DataFrames
df_employment = pd.DataFrame(black_male_employment['observations'])
df_immigration = pd.DataFrame(illegal_immigration_proxy['observations'])

# Prepare data
df_employment['date'] = pd.to_datetime(df_employment['date'])
df_immigration['date'] = pd.to_datetime(df_immigration['date'])
df_employment['value'] = pd.to_numeric(df_employment['value'])
df_immigration['value'] = pd.to_numeric(df_immigration['value'])

# Merge dataframes
df_merged = pd.merge(df_employment, df_immigration, on='date', suffixes=('_employment', '_immigration'))

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Year')
ax1.set_ylabel('Black Male Employment (Thousands)', color='tab:blue')
ax1.plot(df_merged['date'], df_merged['value_employment'], color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Net Migration (Thousands)', color='tab:orange')
ax2.plot(df_merged['date'], df_merged['value_immigration'], color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title('Black Male Employment vs. Net Migration in the US')
fig.tight_layout()
plt.show()

# Calculate correlation
correlation = df_merged['value_employment'].corr(df_merged['value_immigration'])
print(f"Correlation between Black Male Employment and Net Migration: {correlation:.2f}")
```
