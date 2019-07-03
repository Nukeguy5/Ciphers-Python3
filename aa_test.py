
from ciphers import CaesarCipher, AtbashCipher, VigenereCipherSimple

string = 'I am a test string'

def prettyfi(f):
    def decorate(cls, string, *args):
        print('-'*32)
        f(cls, string, *args)
        print('-'*32)
    return decorate

@prettyfi
def full_print(cls, string, *args):
    print(f'Cipher: {cls.__name__}')
    print(f'Original String: {string}')
    if len(args) == 0:
        encrypted_str = cls.encrypt(string)
        decrypted_str = cls.decrypt(encrypted_str)
    elif len(args) == 1:
        arg0 = args[0] 
        encrypted_str = cls.encrypt(string, arg0)
        decrypted_str = cls.decrypt(encrypted_str, arg0)
    print(f'Encrypted: {encrypted_str}')
    print(f'Decrypted: {decrypted_str}')

# Atbash Test
full_print(AtbashCipher, string)

# Cesaer Test
full_print(CaesarCipher, string, 5)

# Vigenere Test
full_print(VigenereCipherSimple, string, 'web')
