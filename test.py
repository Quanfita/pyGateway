import uuid
import requests
import time
from hashlib import sha256


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/test/test1'
    token = '9cd18e53c697b07d7af870b2455cd474'
    timestamp = str(time.time())
    signature = sha256('-'.join([token, timestamp]).encode('utf-8')).hexdigest()
    data = {}
    headers = {}
    response = requests.post(url=url, params={'token': token, 'timestamp': timestamp, 'signature': signature}, data=data, headers=headers)
    print(response.text)
    