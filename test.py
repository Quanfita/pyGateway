import uuid
import requests
import time
from hashlib import sha256


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/test/test1'
    token = '7dfec499714a758d37b013110bbb2d82'
    timestamp = str(time.time())
    signature = sha256('-'.join([token, timestamp]).encode('utf-8')).hexdigest()
    data = {}
    headers = {}
    response = requests.post(url=url, params={'token': token, 'timestamp': timestamp, 'signature': signature}, data=data, headers=headers)
    print(response.text)
    