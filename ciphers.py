
class AtbashCipher:
    
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    REVERSE_ALPHA = ''.join(reversed(ALPHA))

    @classmethod
    def encrypt(cls, message):
        encrypted_message = ''
        for char in message:
            idx = AtbashCipher.ALPHA.index(char.lower())
            encrypted_message += AtbashCipher.REVERSE_ALPHA[idx]

        return encrypted_message

    @classmethod
    def decrypt(cls, encrypted_message):
        decrypted_message = ''
        for char in encrypted_message:
            idx = AtbashCipher.REVERSE_ALPHA.index(char.lower())
            decrypted_message += AtbashCipher.ALPHA[idx]

        return decrypted_message


class CaesarCipher:
    
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'

    @classmethod
    def encrypt(cls, message, shift):
        encrypted_alpha = CaesarCipher.shift_alpha(shift)
        encrypted_message = ''
        for char in message:
            idx = CaesarCipher.ALPHA.index(char)
            encrypted_message += encrypted_alpha[idx]

        return encrypted_message

    @classmethod
    def decrypt(cls, encrypted_message, shift):
        encrypted_alpha = CaesarCipher.shift_alpha(shift)
        decrypted_message = ''
        for char in encrypted_message:
            idx = encrypted_alpha.index(char)
            decrypted_message += CaesarCipher.ALPHA[idx]

        return decrypted_message 

    @classmethod
    def shift_alpha(cls, shift):
        encrypted_alpha = CaesarCipher.ALPHA[shift:] + CaesarCipher.ALPHA[:shift]
        
        return encrypted_alpha

    @classmethod
    def find_shift(cls, encrypted_message):
        pass


class Rot13:

    SHIFT = 13

    @classmethod
    def encrypt(cls, message):
        encrypted_message = CaesarCipher.encrypt(message, Rot13.SHIFT)       
        return encrypted_message

    @classmethod
    def decrypt(cls, encrypted_message):
        decrypted_message = CaesarCipher.decrypt(encrypted_message, Rot13.SHIFT)
        return decrypted_message


class VigenereCipherSimple:

    ALPHA = 'abcdefghijklmnopqrstuvwxyz'

    @classmethod
    def encrypt(cls, message, key):
        encrypted_message = ''
        for message_idx in range(len(message)):
            m_char = message[message_idx]
            if message_idx < len(key):
                k_char = key[message_idx]
            else:
                key_idx = message_idx % len(key)
                k_char = key[key_idx]
            new_char = VigenereCipherSimple.add_chars(m_char, k_char)
            encrypted_message += new_char
            
        return encrypted_message

    @classmethod
    def decrypt(cls, encrypted_message, key):
        decrypted_message = ''

        return decrypted_message
    
    @classmethod
    def add_chars(cls, m_char, k_char):
        try:
            alpha_length = len(VigenereCipherSimple.ALPHA)
            m_char_idx = VigenereCipherSimple.ALPHA.index(m_char)
            k_char_idx = VigenereCipherSimple.ALPHA.index(k_char)
            new_idx = m_char_idx + k_char_idx
            if new_idx >= alpha_length:
                new_idx -= alpha_length
            new_char = VigenereCipherSimple.ALPHA[new_idx]
            return new_char

        except ValueError:
            print(f"Character {m_char} not in alphabet. Skipping addition...")
            return m_char
