# Using FRED API Wrapper in Jupyter Notebooks

This guide explains how to use the FRED API Wrapper in a Jupyter Notebook environment.

## Setup

1. Install the required packages:
   ```
   !pip install fred-api-wrapper gnupg
   ```

2. Import the FredPyAPI class:
   ```python
   from fred_api_wrapper import FredPyAPI
   ```

3. Initialize the API and set up PGP verification:
   ```python
   fred_api = FredPyAPI()
   fred_api.import_public_key('path/to/public_key.asc')
   fred_api.verify_and_set_token('path/to/signed_token.asc')
   ```

## Usage Examples

1. Fetch GDP data:
   ```python
   gdp_data = fred_api.get_series_data("GDP")
   print(gdp_data)
   ```

2. Get historical unemployment data:
   ```python
   unemployment_data = fred_api.get_historical_data("UNRATE", 
                                                    observation_start="2010-01-01", 
                                                    observation_end="2023-12-31")
   ```

3. Visualize data using matplotlib:
   ```python
   import matplotlib.pyplot as plt
   import pandas as pd

   df = pd.DataFrame(unemployment_data['observations'])
   df['date'] = pd.to_datetime(df['date'])
   df['value'] = pd.to_numeric(df['value'])

   plt.figure(figsize=(12, 6))
   plt.plot(df['date'], df['value'])
   plt.title('US Unemployment Rate')
   plt.xlabel('Date')
   plt.ylabel('Unemployment Rate (%)')
   plt.show()
   ```

## Tips for Jupyter Notebooks

- Use `%matplotlib inline` at the beginning of your notebook for inline plots.
- Store your public key and signed token in a secure location, preferably outside the notebook directory.
- Consider using environment variables or a separate configuration file for sensitive information.

## Troubleshooting

If you encounter issues with PGP verification:
1. Ensure your public key and signed token files are in the correct location.
2. Check that you have the necessary permissions to read these files.
3. Verify that your PGP key pair was generated correctly.

For any other issues, please refer to the main README or open an issue on the GitHub repository.
