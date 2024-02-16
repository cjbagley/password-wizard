import hashlib
import requests

class HIBP():
    """ Have I Been Pwned functionality for calling the API """
    def __init__(self) -> None:
        self._api_endpoint = "https://api.pwnedpasswords.com/range/"

    def hash(self, s: str) -> str:
        return hashlib.sha1(s.encode()).hexdigest()

    def getResults(self, password: str) -> list[str]:
        hashed = self.hash(password)
        chunk = hashed[:5]
        headers = {"Add-Padding": "true"}
        r = requests.get(self._api_endpoint + chunk, headers=headers)
        return r.text.splitlines()
