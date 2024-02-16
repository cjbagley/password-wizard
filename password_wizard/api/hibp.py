import hashlib

class HIBP():
    """ Have I Been Pwned functionality for calling the API """

    def hash(self, s: str) -> str:
        return hashlib.sha1(s.encode()).hexdigest()

