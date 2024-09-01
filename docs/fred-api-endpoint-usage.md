# FRED API Endpoint Usage Guide

This guide demonstrates how to use each endpoint of the FredPyAPI class.

## Setup

First, set up the API instance:

```python
from fredpy_api import FredPyAPI

fred_api = FredPyAPI()
fred_api.set_token("your_api_key_here")  # Replace with your actual FRED API key
```

## 1. Get Series Data

```python
# Get data for the GDP series
gdp_data = fred_api.get_series_data("GDP")
print(gdp_data)

# Get data for the Unemployment Rate series
unemployment_data = fred_api.get_series_data("UNRATE")
print(unemployment_data)
```

## 2. Get Historical Data

```python
# Get historical GDP data from 2020 to 2023
historical_gdp = fred_api.get_historical_data("GDP", observation_start="2020-01-01", observation_end="2023-12-31")
print(historical_gdp)

# Get all available historical data for the Consumer Price Index
all_cpi_data = fred_api.get_historical_data("CPIAUCSL")
print(all_cpi_data)
```

## 3. Get Categories

```python
# Get the main categories (category_id 0 is the root)
main_categories = fred_api.get_categories()
print(main_categories)

# Get subcategories of the "Money, Banking, & Finance" category (category_id 32991)
finance_categories = fred_api.get_categories(32991)
print(finance_categories)
```

## 4. Get Releases

```python
# Get all releases
all_releases = fred_api.get_releases()
print(all_releases)

# Get releases from the start of 2023
recent_releases = fred_api.get_releases(realtime_start="2023-01-01")
print(recent_releases)

# Get releases between two specific dates
date_range_releases = fred_api.get_releases(realtime_start="2023-01-01", realtime_end="2023-06-30")
print(date_range_releases)
```

Remember to replace "your_api_key_here" with your actual FRED API key. The actual output will be JSON data containing
various information about the requested series, historical data, categories, or releases.
