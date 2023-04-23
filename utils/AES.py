from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESCipher:
    def __init__(self, key):
        """
        初始化
        """
        self.key = key.encode('utf-8')
        self.BLOCK_SIZE = 16

    def pad(self, data):
        """
        添加填充字符
        """
        padding_size = self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE
        padding = bytes([padding_size] * padding_size)
        return data + padding

    def unpad(self, data):
        """
        去除填充字符
        """
        padding_size = data[-1]
        return data[:-padding_size]

    def encrypt(self, plaintext):
        """
        AES加密
        """
        iv = get_random_bytes(self.BLOCK_SIZE)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_plaintext = self.pad(bytes(plaintext, 'utf-8'))
        ciphertext = cipher.encrypt(padded_plaintext)
        return (iv + ciphertext).hex()

    def decrypt(self, ciphertext):
        """
        AES解密
        """
        ciphertext_bytes = bytes.fromhex(ciphertext)
        iv = ciphertext_bytes[:self.BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext_bytes[self.BLOCK_SIZE:])
        plaintext = self.unpad(padded_plaintext).decode('utf-8')
        return plaintext


if __name__ == '__main__':
    # 测试
    key = "my secret key is"
    message = "This is a secret message."

    aes = AESCipher(key)
    encrypted_message = aes.encrypt(message)
    print(f'Encrypted Message: {encrypted_message}')

    decrypted_message = aes.decrypt(encrypted_message)
    print(f'Decrypted Message: {decrypted_message}')
