```python
import matplotlib.pyplot as plt
import pandas as pd

# Assume we've already set up the FredPyAPI instance with proper verification
fred_api = FredPyAPI()
fred_api.set_public_key("your_public_key_here")
fred_api.set_token("your_token_here", "your_token_signature_here")

# Fetch data (assuming these methods exist)
black_owned = fred_api.get_series_data("BOGZ11180021Q")
veteran_owned = fred_api.get_series_data("VOGZ11180021Q")

# Convert to pandas DataFrames
df_black = pd.DataFrame(black_owned['observations'])
df_veteran = pd.DataFrame(veteran_owned['observations'])

# Prepare data
df_black['date'] = pd.to_datetime(df_black['date'])
df_veteran['date'] = pd.to_datetime(df_veteran['date'])
df_black['value'] = pd.to_numeric(df_black['value'])
df_veteran['value'] = pd.to_numeric(df_veteran['value'])

# Create plot
plt.figure(figsize=(12, 6))
plt.plot(df_black['date'], df_black['value'], label='Black-owned')
plt.plot(df_veteran['date'], df_veteran['value'], label='Veteran-owned')
plt.title('Number of Black-owned and Veteran-owned Businesses')
plt.xlabel('Year')
plt.ylabel('Number of Firms')
plt.legend()
plt.grid(True)
plt.show()

# Calculate growth rates
black_growth = (df_black['value'].pct_change().mean() * 100).round(2)
veteran_growth = (df_veteran['value'].pct_change().mean() * 100).round(2)

print(f"Average quarterly growth rate for Black-owned businesses: {black_growth}%")
print(f"Average quarterly growth rate for Veteran-owned businesses: {veteran_growth}%")
```
