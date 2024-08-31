# How To Use

1. Generte a key pair (do this once, offline):

```
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get public key
public_key = private_key.public_key()

# Serialize public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Public Key:")
print(public_key_pem.decode())

# Save private key securely offline
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(private_key_pem)
```
2. Sign your API key (do this offline, with the private key):

```
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from base64 import b64encode

with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

api_key = "your_fred_api_key_here"
signature = private_key.sign(
    api_key.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Signature:")
print(b64encode(signature).decode())
```
Use in Application

```
fred_api = FredPyAPI()

# Set the public key (this could be stored in a config file)
public_key_pem = """
-----BEGIN PUBLIC KEY-----
... (your public key here) ...
-----END PUBLIC KEY-----
"""
fred_api.set_public_key(public_key_pem)

# Set the API key and its signature
api_key = "your_fred_api_key_here"
signature = "base64_encoded_signature_here"
fred_api.set_token(api_key, signature)

# Now you can use fred_api as before
data = fred_api.get_series_data("GDP")
```
