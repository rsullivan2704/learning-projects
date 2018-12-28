ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.!?,;: '

class CaesarCipher(object):
    def __init__(self, plain_text:str, shift:int, is_shift_left:bool):
        self._plain_text = plain_text
        # Normalize the shift to 0 <= shift < len(ALPHA)
        self._shift = shift % len(ALPHA)
        # Negate the shift if is_shift_left == True
        if is_shift_left:
            self._shift *= -1        

    def decode(self, encoded_text:str):
        result = ''
        for char in encoded_text:
            # Get the index by reversing the shift and normalizing to 0 <= index < len(ALPHA)
            index = (ALPHA.find(char) - self._shift) % len(ALPHA)
            result += ALPHA[index]
        return result

    def encode(self):
        result = ''
        for char in self._plain_text:
            # Get the index by adding the shift and normalizing to 0 <= index < len(ALPHA)
            index = (ALPHA.find(char) + self._shift) % len(ALPHA)
            result += ALPHA[index]
        return result

if __name__ == '__main__':
    cipher = CaesarCipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, True)
    encoded = cipher.encode()
    print('Encoded:', encoded)
    print('Decoded:', cipher.decode(encoded))
    
    cipher = CaesarCipher('The quick brown fox jumps over the lazy dog!', 22, True)
    encoded = cipher.encode()
    print('Encoded:', encoded)
    print('Decoded:', cipher.decode(encoded))