import requests
from typing import Optional
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
from base64 import b64encode, b64decode

class FredPyAPI:

    # main web address our application will talk to
    BASE_URL = "https://api.stlouisfed.org/fred/"
    
    def __init__(self, token: Optional[str] = None, token_signature: Optional[str] = None):
        self.token = token
        self.token_signature = token_signature
        self.public_key = None  # This should be set with a method

    def set_public_key(self, public_key_pem: str):
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        self.public_key = load_pem_public_key(public_key_pem.encode())

    def set_token(self, token: str, token_signature: str) -> None:
        if self.verify_token(token, token_signature):
            self.token = token
            self.token_signature = token_signature
        else:
            raise ValueError("Token verification failed")

    def verify_token(self, token: str, signature: str) -> bool:
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
    # This is a private helper function (that's why it starts with
    # _). It's like the robot's internal communication system.
    def _make_request(self, endpoint: str, params: dict) -> dict:
        # This checks if the robot has its password (api_key). If not, it stops and tells us to set the password.
        if not self.token:
           raise ValueError("API token is not set. Use set_token() method to set it.")
           
        # These lines add the password and ask for the response in a specific format (JSON).
        params['api_key'] = self.token
        params['file_type'] = 'json'
           
        # This sends the request to FRED, checks for errors, and returns the data.
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        
        return response.json()
    
    # This function gets data about a specific economic series (like GDP).
    def get_series_data(self, series_id: str) -> dict:
        return self._make_request("series", {"series_id": series_id})
    
    # This gets historical data for a series, with optional start and end dates.
    def get_historical_data(self, series_id: str, observation_start: Optional[str] = None, observation_end: Optional[str] = None) -> dict:
        params = {"series_id": series_id}
        if observation_start:
            params["observation_start"] = observation_start
        if observation_end:
            params["observation_end"] = observation_end
            
        return self._make_request("series/observations", params)
   
    # This gets information about categories of economic data. 
    def get_categories(self, category_id: int = 0) -> dict:
        return self._make_request("category", {"category_id": category_id})
   
    # This gets information about when new economic data is released.
    def get_releases(self, realtime_start: Optional[str] = None, realtime_end: Optional[str] = None) -> dict:
        params = {}
        if realtime_start:
            params["realtime_start"] = realtime_start
            
        if realtime_end:
            params["realtime_end"] = realtime_end
            
        return self._make_request("releases", params)
