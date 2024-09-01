# Security Policy

## Supported Versions

Security updates currently supported versions of the project.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 0.9.x   | :white_check_mark: |
| 0.8.x   | :x:                |
| < 0.8   | :x:                |

## Reporting a Vulnerability

We take the security of FRED API Wrapper seriously. If you have discovered a security vulnerability in our project, please follow these steps to report it:

1. **Do Not** disclose the vulnerability publicly until our team has addressed it.
2. Email your findings to [security-email@chaniyk.io]. Please keep your email using our PGP key to ensure the report is safe.
3. Provide as much information as possible about the vulnerability:
   - The steps to reproduce the issue
   - The affected versions
   - Any potential impacts of the vulnerability

Our security team will acknowledge your email within 48 hours and send a more detailed response within 5 days, letting us know the next steps in handling your report.

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine the affected versions.
2. Audit code to find any potential similar problems.
3. Prepare fixes for all supported versions.
4. Release new versions and patches as soon as possible.

## Comments on this Policy

If you have suggestions on improving this process, please submit a pull request or open an issue to discuss.

## Scope

This security policy applies to the core FRED API Wrapper project. If you find vulnerabilities in the FRED API, please report them directly to the Federal Reserve Bank of St. Louis.

## Best Practices

When using the FRED API Wrapper:

1. Keep your API key confidential. Never commit it to version control or share it publicly.
2. Use environment variables or secure secret management solutions to store your API key.
3. Regularly update to the latest version of the wrapper to ensure you have the latest security patches.
4. Be cautious when handling and storing data retrieved from the API, especially if it contains sensitive economic information.

## Security Features

The FRED API Wrapper includes several security features:

1. API Key Verification: The wrapper includes a mechanism to verify the integrity of the API key.
2. HTTPS: All communications with the FRED API are done over HTTPS.
3. Input Validation: The wrapper validates input to prevent injection attacks.

Remember, while we strive to make the FRED API Wrapper secure, it's crucial to implement your own security measures in any application using this wrapper.
