# FRED API Wrapper

## Overview

A Python wrapper for the Federal Reserve Economic Data (FRED) API. It simplifies fetching economic data series, historical data, categories, and releases from FRED and adds security through PGP signature verification.

## Features

- Easy-to-use Python interface for FRED API
- Support for fetching series data, historical data, categories, and releases
- Built-in PGP token verification for enhanced security
- Customizable error handling

## Installation

To install the FRED API Wrapper, run the following command:

```bash
pip install fred-api-wrapper gnupg
```

## Usage

Here's a quick example of how to use the FRED API Wrapper with PGP signature verification:

```python
from fred_api_wrapper import FredPyAPI

# Initialize the API
fred_api = FredPyAPI()

# Import the public key
fred_api.import_public_key('path/to/public_key.asc')

# Verify and set the token
fred_api.verify_and_set_token('path/to/signed_token.asc')

# Now you can use the API as before
gdp_data = fred_api.get_series_data("GDP")
print(gdp_data)
```

## Security

This wrapper uses PGP for API key verification. To use this feature:

1. Generate a PGP key pair if you don't have one:
   ```
   gpg --full-generate-key
   ```

2. Export your public key:
   ```
   gpg --armor --export your_email@example.com > public_key.asc
   ```

3. Sign your FRED API key:
   ```
   echo "your_fred_api_key" | gpg --clearsign > signed_token.asc
   ```

4. Use these files with the `import_public_key` and `verify_and_set_token` methods, as shown in the usage example.

## API Reference

[The API reference section remains the same]

## Contributing

Contributions to the FRED API Wrapper are welcome! For guidelines on how to contribute to this project, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. Please take a look at the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Federal Reserve Bank of St. Louis for providing the FRED API
- All contributors to this project

## Contact

For any questions or concerns, please open an issue on the GitHub repository.
