from setuptools import setup, find_packages

setup(
    name="fred-api-wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "cryptography",
        "python-dotenv",
    ],
)