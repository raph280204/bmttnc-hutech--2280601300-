from lab_02.cipher import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, plain_text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        plain_text = plain_text.upper()
        encrypted_text = []
        for letter in plain_text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)

    def decrypt_text(self, plain_text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        plain_text = plain_text.upper()
        decrypted_text = []
        for letter in plain_text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)