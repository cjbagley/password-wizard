""" Have I Been Pwned functionality for calling the API """
import requests
from password_wizard.utils.utils import sha1_hash

HIBP_ENDPOINT = "https://api.pwnedpasswords.com/range/"

def getResults(password: str) -> list[str]:
    hashed = sha1_hash(password)
    chunk = hashed[:5]
    headers = {"Add-Padding": "true"}
    r = requests.get(HIBP_ENDPOINT + chunk, headers=headers)
    return r.text.splitlines()
