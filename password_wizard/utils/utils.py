import hashlib


def sha1_hash(s: str) -> str:
    return hashlib.sha1(s.encode()).hexdigest()
