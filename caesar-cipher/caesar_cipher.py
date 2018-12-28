ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
LEFT = True
RIGHT = False

class CaesarCipher(object):
    def __init__(self, plain_text:str, shift:int, direction:bool):
        self._plain_text = plain_text
        # Normalize the shift to 0 <= shift < len(ALPHA)
        self._shift = shift % len(ALPHA)
        # Set the direction and negate it if direction == LEFT
        self._direction = direction
        if direction == LEFT:
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
    cipher = CaesarCipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, RIGHT)
    encoded = cipher.encode()
    print('Encoded:', encoded)
    print('Decoded:', cipher.decode(encoded))