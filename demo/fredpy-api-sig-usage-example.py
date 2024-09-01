import os
from fredpy_api import FredPyAPI

# Initialize the API
fred_api = FredPyAPI()

# Set the public key (this should be provided by the API service)
public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAx
... (rest of the public key)
-----END PUBLIC KEY-----
"""
fred_api.set_public_key(public_key_pem)

# Set the API token (you should get this securely, e.g., from environment variables)
api_token = os.environ.get("FRED_API_TOKEN")
api_token_signature = os.environ.get("FRED_API_TOKEN_SIGNATURE")
fred_api.set_token(api_token, api_token_signature)

# Example 1: Get series data for GDP (Series ID: GDP)
gdp_series = fred_api.get_series_data("GDP")
print("GDP Series Information:")
print(gdp_series)

# Example 2: Get historical data for unemployment rate (Series ID: UNRATE)
unemployment_data = fred_api.get_historical_data("UNRATE", observation_start="2020-01-01", observation_end="2023-12-31")
print("\nUnemployment Rate Data (2020-2023):")
print(unemployment_data)

# Example 3: Get categories information
categories = fred_api.get_categories(category_id=32991)  # 32991 is the category ID for "Money, Banking, & Finance"
print("\nMoney, Banking, & Finance Category Information:")
print(categories)

# Example 4: Get recent releases
recent_releases = fred_api.get_releases(realtime_start="2023-01-01")
print("\nRecent Economic Data Releases:")
print(recent_releases)

# Error handling example
try:
    invalid_series = fred_api.get_series_data("INVALID_SERIES_ID")
except requests.exceptions.HTTPError as e:
    print(f"\nError occurred: {e}")

# Note: Make sure to handle exceptions and errors appropriately in a production environment
