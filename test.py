import uuid
import requests
import time
from hashlib import sha256


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/test/test1'
    token = '64c37959d4d10e18ae3f53eadfba77f4'
    timestamp = str(time.time())
    signature = sha256('-'.join([token, timestamp]).encode('utf-8')).hexdigest()
    data = {}
    headers = {}
    response = requests.post(url=url, params={'token': token, 'timestamp': timestamp, 'signature': signature}, data=data, headers=headers)
    print(response.text)
    