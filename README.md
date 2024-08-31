# **FRED API in Python**

This guide explains how to work with the **Federal Reserve Economic Data (FRED) API** in Python to retrieve economic data for analysis. FRED provides a wealth of data including U.S. economic indicators, interest rates, and more.

## **Table of Contents**

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Using the FRED API](#using-the-fred-api)
5. [Examples](#examples)
6. [Handling API Responses](#handling-api-responses)
7. [Additional Resources](#additional-resources)

## **Requirements**

- Python 3.6 or higher
- `requests` library for handling HTTP requests
- `pandas` library for data manipulation and analysis

## **Installation**

First, ensure you have Python 3.6 or higher installed. Then, install the necessary libraries using pip:

```bash
pip install requests pandas
```

## **Getting Started**

### **1. Obtain an API Key**

To use the FRED API, you'll need to sign up for an API key:

1. Visit the [FRED API registration page](https://fred.stlouisfed.org/)
2. Sign up for a free account
3. Retrieve your API key from your account settings

### **2. Set Up Your Python Script**

Create a Python script (e.g., `fred_api.py`) and include your API key:

```python
import requests
import pandas as pd

# Replace with your actual API key
API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.stlouisfed.org/fred/'
```

## **Using the FRED API**

To retrieve data, make a GET request to the FRED API endpoint using the `requests` library.

### **Common Endpoints:**

- **Get Economic Data Series**: `/series`
- **Get Observations (Historical Data)**: `/series/observations`
- **Get Categories**: `/category`
- **Get Releases**: `/releases`

### **Example: Fetching Data for a Series**

To fetch data for a specific series, use the `/series/observations` endpoint.

```python
def get_series_data(series_id, api_key):
    url = f'{BASE_URL}series/observations'
    params = {
        'series_id': series_id,
        'api_key': api_key,
        'file_type': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data['observations'])
    else:
        print(f'Error: {response.status_code}')
        return None

# Example Usage
series_id = 'GDP'
df = get_series_data(series_id, API_KEY)
print(df.head())
```

## **Handling API Responses**

The API response is typically in JSON format. Use Python’s `json` library to parse the response and `pandas` to manipulate and analyze the data.

### **Error Handling**

Always check the status code of the response:

```python
if response.status_code == 200:
    # Handle the data
else:
    print(f'Error: {response.status_code}')
```

## **Examples**

1. **Fetch and Plot GDP Data:**

```python
import matplotlib.pyplot as plt

# Fetch the data
df = get_series_data('GDP', API_KEY)

# Convert date to datetime format and plot
df['date'] = pd.to_datetime(df['date'])
df['value'] = pd.to_numeric(df['value'])

plt.plot(df['date'], df['value'])
plt.title('US GDP Over Time')
plt.xlabel('Date')
plt.ylabel('GDP')
plt.show()
```

## **Additional Resources**

- [FRED API Documentation](https://fred.stlouisfed.org/docs/api/fred/)
- [Requests Library Documentation](https://docs.python-requests.org/en/master/)
- [Pandas Library Documentation](https://pandas.pydata.org/)

## **Contributing**

If you'd like to contribute to this guide, please feel free to submit a pull request or open an issue.

## **License**

This project is licensed under the MIT License.

---

This `README.md` file provides a basic overview of how to get started with the FRED API in Python, including setup, usage, and examples. Would you like more details on a specific section?