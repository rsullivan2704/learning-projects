ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
LEFT = True
RIGHT = False

class CaesarCipher(object):
    def __init__(self, plain_text:str, shift:int, direction:bool):
        self._plain_text = plain_text
        self._shift = shift % len(ALPHA)
        self._direction = direction
        if direction == LEFT:
            self._shift *= -1        

    def decode(self, encoded_text):
        result = ''
        for char in encoded_text:
            index = (ALPHA.find(char) - self._shift) % len(ALPHA)
            result += ALPHA[index]
        return result

    def encode(self):
        result = ''
        for char in self._plain_text:
            index = (ALPHA.find(char) + self._shift) % len(ALPHA)
            result += ALPHA[index]
        return result

if __name__ == '__main__':
    cipher = CaesarCipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, RIGHT)
    encoded = cipher.encode()
    print('Encoded:', encoded)
    print('Decoded:', cipher.decode(encoded))