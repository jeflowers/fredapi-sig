```python
import requests
from typing import Optional
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
from base64 import b64encode, b64decode
import gnupg

class FredPyAPI:
    BASE_URL = "https://api.stlouisfed.org/fred/"
    
    def __init__(self):
        self.token = None
        self.token_signature = None
        self.public_key = None
        self.gpg = gnupg.GPG()

    def set_public_key(self, public_key_pem: str):
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        self.public_key = load_pem_public_key(public_key_pem.encode())

    def set_token_rsa(self, token: str, token_signature: str) -> None:
        if self.verify_token_rsa(token, token_signature):
            self.token = token
            self.token_signature = token_signature
        else:
            raise ValueError("Token verification failed")

    def verify_token_rsa(self, token: str, signature: str) -> bool:
        if not self.public_key:
            raise ValueError("Public key not set. Use set_public_key method first.")
        
        try:
            self.public_key.verify(
                b64decode(signature),
                token.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def import_public_key_pgp(self, public_key_path: str):
        with open(public_key_path, 'r') as f:
            import_result = self.gpg.import_keys(f.read())
        if not import_result.fingerprints:
            raise ValueError("Failed to import public key")

    def verify_and_set_token_pgp(self, signed_token_path: str):
        with open(signed_token_path, 'r') as f:
            verified = self.gpg.verify_file(f)
        if verified:
            self.token = verified.data.decode().strip()
        else:
            raise ValueError("Token verification failed")

    def _make_request(self, endpoint: str, params: dict) -> dict:
        if not self.token:
            raise ValueError("API token is not set. Use set_token_rsa() or verify_and_set_token_pgp() method to set it.")
        
        params['api_key'] = self.token
        params['file_type'] = 'json'
        
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def get_series_data(self, series_id: str) -> dict:
        return self._make_request("series", {"series_id": series_id})

    def get_historical_data(self, series_id: str, observation_start: Optional[str] = None, observation_end: Optional[str] = None) -> dict:
        params = {"series_id": series_id}
        if observation_start:
            params["observation_start"] = observation_start
        if observation_end:
            params["observation_end"] = observation_end
        return self._make_request("series/observations", params)

    def get_categories(self, category_id: int = 0) -> dict:
        return self._make_request("category", {"category_id": category_id})

    def get_releases(self, realtime_start: Optional[str] = None, realtime_end: Optional[str] = None) -> dict:
        params = {}
        if realtime_start:
            params["realtime_start"] = realtime_start
        if realtime_end:
            params["realtime_end"] = realtime_end
        return self._make_request("releases", params)
```
