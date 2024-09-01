```python
import matplotlib.pyplot as plt
import pandas as pd

# Assume we've already set up the FredPyAPI instance with proper verification
fred_api = FredPyAPI()
fred_api.set_public_key("your_public_key_here")
fred_api.set_token("your_token_here", "your_token_signature_here")

# Fetch data (assuming these methods exist)
white_unemployment = fred_api.get_series_data("LNS14000003")
black_unemployment = fred_api.get_series_data("LNS14000006")
asian_unemployment = fred_api.get_series_data("LNS14000009")
hispanic_unemployment = fred_api.get_series_data("LNS14000009")

# Convert to pandas DataFrames
df_white = pd.DataFrame(white_unemployment['observations'])
df_black = pd.DataFrame(black_unemployment['observations'])
df_asian = pd.DataFrame(asian_unemployment['observations'])
df_hispanic = pd.DataFrame(hispanic_unemployment['observations'])

# Prepare data
for df in [df_white, df_black, df_asian, df_hispanic]:
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'])

# Create plot
plt.figure(figsize=(12, 6))
plt.plot(df_white['date'], df_white['value'], label='White')
plt.plot(df_black['date'], df_black['value'], label='Black')
plt.plot(df_asian['date'], df_asian['value'], label='Asian')
plt.plot(df_hispanic['date'], df_hispanic['value'], label='Hispanic')

plt.title('Unemployment Rate by Race')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate average unemployment rates
avg_white = df_white['value'].mean().round(2)
avg_black = df_black['value'].mean().round(2)
avg_asian = df_asian['value'].mean().round(2)
avg_hispanic = df_hispanic['value'].mean().round(2)

print(f"Average Unemployment Rates:")
print(f"White: {avg_white}%")
print(f"Black: {avg_black}%")
print(f"Asian: {avg_asian}%")
print(f"Hispanic: {avg_hispanic}%")
```
