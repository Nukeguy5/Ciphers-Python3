
class AtbashCiper:
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alpha = ''.join(reversed(alpha))

    @classmethod
    def encrypt(cls, og_str):
        encrypted_str = ''
        for char in og_str:
            idx = AtbashCiper.alpha.index(char)
            encrypted_str += AtbashCiper.reverse_alpha[idx]

        return encrypted_str

    @classmethod
    def decrypt(cls, encrypted_str):
        decrypted_str = ''
        for char in encrypted_str:
            idx = AtbashCiper.reverse_alpha.index(char)
            decrypted_str += AtbashCiper.alpha[idx]

        return decrypted_str


class CaesarCiper:
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    @classmethod
    def encrypt(cls, og_str, shift):
        encrypted_alpha = CaesarCiper.shift_alpha(shift)
        encrypted_str = ''
        for char in og_str:
            idx = CaesarCiper.alpha.index(char)
            encrypted_str += encrypted_alpha[idx]

        return encrypted_str

    @classmethod
    def decrypt(cls, encrypted_str, shift):
        encrypted_alpha = CaesarCiper.shift_alpha(shift)
        decrypted_str = ''
        for char in encrypted_str:
            idx = encrypted_alpha.index(char)
            decrypted_str += CaesarCiper.alpha[idx]

        return decrypted_str 

    @classmethod
    def shift_alpha(cls, shift):
        encrypted_alpha = CaesarCiper.alpha[shift:] + CaesarCiper.alpha[:shift]
        
        return encrypted_alpha

    @classmethod
    def find_shift(cls, encrypted_str):
        pass


class Rot13:

    shift = 13

    @classmethod
    def encrypt(cls, og_str):
        shift = Rot13.shift
        encrypted_sr = CaesarCiper.encrypt(og_str, shift)
        
        return encrypted_sr

    @classmethod
    def decrypt(cls, encrypted_str):
        shift = Rot13.shift
        decrypted_str = CaesarCiper.decrypt(encrypted_str, shift)

        return decrypted_str
        