""" Functions related to interacting with 'Have I Been Pwned' (HIBP) API

    Full details of how the API works can be found at:
    https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange
    In short summary: it uses k-Anonymity model that allows searching
    previously leaked passwords by the first 5 characters of a SHA-1 hash.
    The password itself is never sent via the API; just the first 5
    characters of the hash. The API returns any matching hashes that
    start with those 5 characters (but only the remaining parts of the 
    full hash string, i.e. they do not have the first 5 characters).
    The results can then be combined with the original 5 characters locally
    to find if any combined hash matches the full hash of the password.
    If a match has been found: that password has been leaked at some point.
"""

import requests
import re

HIBP_ENDPOINT = "https://api.pwnedpasswords.com/range/"


def get_matching_hashes(search_hash: str) -> list[str]:
    """Call HIBP API to find any matching hashes

    Results from the API come as a text string:
    {matching hash remainder}:{count of times leaked}\n
    {matching hash remainder}:{count of times leaked}\n...
    """
    search_hash = search_hash.upper()
    _check_search_hash(search_hash, 5)
    headers = {"Add-Padding": "true"}
    r = requests.get(HIBP_ENDPOINT + search_hash, headers=headers)
    return r.text.splitlines()


def _check_search_hash(search_hash: str, length: int=5) -> None:
    """Helper function to check if string is in expected search hash format"""
    if len(search_hash) != length:
        raise ValueError(f"Search hash expecting {length} characters, {len(search_hash)} given")
    if re.match(r"^[A-F0-9]{5}$", search_hash) is None:
        raise ValueError(
            "Search hash given looks to be plain text - please provide a hash"
        )
