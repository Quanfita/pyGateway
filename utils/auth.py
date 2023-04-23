from hashlib import sha256, md5
from .key import generate_key

class Auth:

    def __init__(self, hash_fun='sha256') -> None:
        self._hash_fun_map = {
            'sha256': sha256,
            'md5': md5
        }
        self._hash_fun = self._hash_fun_map.get(hash_fun, sha256)

    def _auth_token(self, token: str) -> bool:
        return True
    
    def _auth_signature(self, token: str, timestamp: str, signature: str) -> bool:
        if self._hash_fun('-'.join([token, timestamp]).encode('utf-8')).hexdigest() == signature:
            return True
        return False
    
    def authentication(self, token: str, timestamp: str, signature: str) -> bool:
        return self._auth_token(token) and self._auth_signature(token, timestamp, signature)
    
    @staticmethod
    def genetate_key():
        return generate_key(length=16)