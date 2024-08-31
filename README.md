# FRED API Wrapper

## Overview

This project provides a Python wrapper for the Federal Reserve Economic Data (FRED) API. It simplifies the process of fetching economic data series, historical data, categories, and releases from FRED.

## Features

- Easy-to-use Python interface for FRED API
- Support for fetching series data, historical data, categories, and releases
- Built-in token verification for enhanced security
- Customizable error handling

## Installation

To install the FRED API Wrapper, run the following command:

```bash
pip install fred-api-wrapper
```

## Usage

Here's a quick example of how to use the FRED API Wrapper:

```python
from fred_api_wrapper import FredPyAPI

# Initialize the API with your token
fred_api = FredPyAPI("your_api_key_here")

# Get series data
gdp_data = fred_api.get_series_data("GDP")

# Get historical data
historical_gdp = fred_api.get_historical_data("GDP", observation_start="2020-01-01", observation_end="2023-12-31")

# Get categories
main_categories = fred_api.get_categories()

# Get releases
recent_releases = fred_api.get_releases(realtime_start="2023-01-01")

print(gdp_data)
print(historical_gdp)
print(main_categories)
print(recent_releases)
```

## API Reference

### `FredPyAPI`

The main class for interacting with the FRED API.

#### Methods:

- `get_series_data(series_id: str) -> dict`
- `get_historical_data(series_id: str, observation_start: Optional[str] = None, observation_end: Optional[str] = None) -> dict`
- `get_categories(category_id: int = 0) -> dict`
- `get_releases(realtime_start: Optional[str] = None, realtime_end: Optional[str] = None) -> dict`

For detailed information on each method, please refer to the [FRED API documentation](https://fred.stlouisfed.org/docs/api/fred/).

## Security

This wrapper includes a built-in mechanism for verifying the integrity of the API key. For more information on setting up and using this feature, please refer to the [security documentation](docs/security.md).

## Contributing

Contributions to the FRED API Wrapper are welcome! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Federal Reserve Bank of St. Louis for providing the FRED API
- All contributors to this project

## Contact

For any questions or concerns, please open an issue on the GitHub repository.