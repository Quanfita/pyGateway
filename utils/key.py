import string
import random

def generate_key(length: int=16) -> str:
    """
    生成指定长度的随机key
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))