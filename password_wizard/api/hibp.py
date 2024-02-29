""" Functions related to interacting with 'Have I Been Pwned' (HIBP) API

    Full details of how the API works can be found at:
    https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange
    Short summary: it uses k-Anonymity model that allows searching
    previously leaked passwords by the first 5 characters of a SHA-1 hash.
    The password itself is never sent via the API; just the first 5
    characters of the hash. The API returns any matching hashes that
    start with those 5 characters (but only the remaining parts of the 
    full hash string, i.e. they do not have the first 5 characters).
    The results can then be combined with the original 5 characters locally
    to find if any combined hash matches the full hash of the password.
    If a match has been found: that password has been leaked at some point.
"""

import re
import requests

HIBP_ENDPOINT = "https://api.pwnedpasswords.com/range/"
HIBP_EXCEPT_MSG = "Error with results given from HIBP API"


def _get_matching_hashes(search_hash: str) -> list[str]:
    """Call HIBP API to find any matching hashes

    Results from the API come as a text string:
      {matching hash remainder}:{count of times leaked}\n
      {matching hash remainder}:{count of times leaked}\n...
    """
    search_hash = search_hash.upper()
    _check_search_hash(search_hash, 5)

    headers = {"Add-Padding": "true"}
    r = requests.get(HIBP_ENDPOINT + search_hash, headers=headers, timeout=5)
    r = r.text.splitlines()

    if len(r) == 0:
        raise ValueError(f"{HIBP_EXCEPT_MSG}: empty results given")
    _check_result_format(r[0])

    found = []
    for result in r:
        found.append(result.split(":"))

    return found


def get_matched_hash_count(hashed_password: str) -> int:
    """Get the count of the times the search hash has been found"""
    hashed_password = hashed_password.upper()
    _check_search_hash(hashed_password, 40)
    for result in _get_matching_hashes(hashed_password[:5]):
        if hashed_password == hashed_password[:5] + result[0]:
            return int(result[1])

    return 0


def _check_search_hash(search_hash: str, length: int = 5) -> None:
    """Helper to check if string is in expected search hash format"""
    if len(search_hash) != length:
        raise ValueError(
            f"Search hash expecting {length} characters, {len(search_hash)} given"
        )

    regex = re.compile(f"^[A-F0-9]{{{length}}}$")
    if regex.match(search_hash) is None:
        raise ValueError(
            "Search hash given looks to be plain text - please provide a hash"
        )


def _check_result_format(result: str) -> None:
    """Helper to check if result given from API matches expected format"""
    check = result.split(":")
    _check_search_hash(check[0], 35)
    if int(check[1]) <= 0:
        raise ValueError(f"{HIBP_EXCEPT_MSG}: int expected")
