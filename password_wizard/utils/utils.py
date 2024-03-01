"""General utilities module"""

import hashlib


def sha1_hash(s: str) -> str:
    """Return the SHA1 string of a given input string"""
    return hashlib.sha1(s.encode(), usedforsecurity=False).hexdigest()
