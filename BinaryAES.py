class BinaryAES:
    def __init__(self):
        self.xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def __rotate(self, word, n):
        return word[n:] + word[0:n]

    def galoisMult(self, a, b):
        p = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256

    def text2matrix(self, text):
        matrix = []
        for i in range(16):
            byte = (text >> (8 * (15 - i))) & 0xFF
            if i % 4 == 0:
                matrix.append([byte])
            else:
                matrix[i / 4].append(byte)
        return matrix

    def matrix2text(self, matrix):
        text = 0
        for i in range(4):
            for j in range(4):
                text |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
        return text
