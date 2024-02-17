""" Have I Been Pwned functionality for calling the API """

import requests
import re

HIBP_ENDPOINT = "https://api.pwnedpasswords.com/range/"


def get_matching_hashes(search_hash: str) -> list[str]:
    search_hash = search_hash.upper()
    _check_search_hash(search_hash)
    headers = {"Add-Padding": "true"}
    r = requests.get(HIBP_ENDPOINT + search_hash, headers=headers)
    return r.text.splitlines()


def _check_search_hash(search_hash: str) -> None:
    if len(search_hash) != 5:
        raise ValueError("Search hash must be the first 5 characters only")
    if re.match(r"^[A-F0-9]{5}$", search_hash) is None:
        raise ValueError("Search hash given looks to be plain text")
