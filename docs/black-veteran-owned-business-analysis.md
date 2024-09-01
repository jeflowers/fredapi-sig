# Analysis of Black-owned and Veteran-owned Businesses

This example demonstrates how to use the FRED API to analyze data related to Black-owned and veteran-owned businesses.

## Setup and Data Retrieval

```python
from fredpy_api import FredPyAPI
import pandas as pd
import matplotlib.pyplot as plt

fred_api = FredPyAPI()
fred_api.set_token("your_api_key_here")  # Replace with your actual FRED API key

def get_business_data(series_id, start_date, end_date):
    data = fred_api.get_historical_data(series_id, observation_start=start_date, observation_end=end_date)
    df = pd.DataFrame(data['observations'])
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'])
    return df.set_index('date')['value']

start_date = "2002-01-01"
end_date = "2022-12-31"

# Black-owned business data (total number of firms)
black_owned = get_business_data("BOGZ11180021Q", start_date, end_date)

# Veteran-owned business data (total number of firms)
veteran_owned = get_business_data("VOGZ11180021Q", start_date, end_date)
```

## Data Analysis and Visualization

```python
# Combine the data
combined_data = pd.DataFrame({
    'Black-owned': black_owned,
    'Veteran-owned': veteran_owned
})

# Calculate growth rates
growth_rates = combined_data.pct_change().mean() * 100

# Plot the data
plt.figure(figsize=(12, 6))
combined_data.plot(ax=plt.gca())
plt.title('Number of Black-owned and Veteran-owned Businesses')
plt.ylabel('Number of Firms')
plt.legend(['Black-owned', 'Veteran-owned'])
plt.grid(True)

# Add annotations for growth rates
for i, rate in enumerate(growth_rates):
    plt.annotate(f'{rate:.2f}% avg. quarterly growth', 
                 xy=(0.05, 0.95 - i*0.05), 
                 xycoords='axes fraction', 
                 fontsize=10, 
                 ha='left', 
                 va='top')

plt.tight_layout()
plt.show()

# Print summary statistics
print(combined_data.describe())

# Calculate and print the correlation between the two series
correlation = combined_data['Black-owned'].corr(combined_data['Veteran-owned'])
print(f"\nCorrelation between Black-owned and Veteran-owned businesses: {correlation:.2f}")
```

## Analysis Insights

This analysis allows us to compare the growth and trends of Black-owned and veteran-owned businesses over time. We can observe:

1. The relative number of businesses in each category
2. How the numbers have changed over time
3. The average growth rates for each group
4. Any correlation between the growth of these two groups of businesses

This information could be valuable for:
- Policymakers
- Researchers
- Business organizations

It can help in:
- Understanding and supporting these important segments of the business community
- Identifying periods of growth or decline
- Informing targeted support programs
- Highlighting the need for further research into factors affecting these business communities

Remember to replace "your_api_key_here" with your actual FRED API key when running this analysis.
