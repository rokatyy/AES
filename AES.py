import AES_standart
from BinaryAES import BinaryAES


class AES(BinaryAES):
    def __init__(self):
        self.Sbox = AES_standart.Sbox
        self.InvSbox = AES_standart.InvSbox
        self.data = None
        self.Binary = BinaryAES()

    def Key_addition(self):
        pass

    def Byte_substitution(self, action='ENCODE'):
        if action == 'ENCODE':
            sub_matrix = self.Sbox
        else:
            sub_matrix = self.InvSbox
        self.data = [sub_matrix[self.data[i][j]] for i in range(4) for j in range(4)]

    def ShiftRows(self, state):
        """
        Transforms input matrix
        | e0 | e4 | e8 | e12|          | e0 | e4 | e8 | e12|   no shift
        | e1 | e5 | e9 | e13|    TO    | e5 | e9 | e13| e1 |   <--- 1 position
        | e2 | e6 | e10| e14|          | e10| e14| e2 | e6 |   <--- 2 positions
        | e4 | e7 | e11| e15|          | e15| e4 | e7 | e11|   <--- 3 position s
        """
        for i in range(4):
            state[i * 4:i * 4 + 4] = self.__rotate(state[i * 4:i * 4 + 4], i)

    def MixColumn(self, s):
        """
        Transforms every column of matrix which was made with ShiftRow
        | c0 |    | 02 | 03 | 01 | 01 |  | e0 |
        | c1 | == | 01 | 02 | 03 | 01 |  | e5 |
        | c2 |    | 01 | 01 | 02 | 03 |  | e10|
        | c3 |    | 03 | 01 | 01 | 02 |  | e15|
        """
        for i in range(4):
            self.__mix_single_column(s[i])

    def ShiftRowsInv(self, state):
        for i in range(4):
            state[i * 4:i * 4 + 4] = self.__rotate(state[i * 4:i * 4 + 4], -i)

    def __mix_single_column(self, a):
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ self.xtime(a[0] ^ a[1])
        a[1] ^= t ^ self.xtime(a[1] ^ a[2])
        a[2] ^= t ^ self.xtime(a[2] ^ a[3])
        a[3] ^= t ^ self.xtime(a[3] ^ u)

    def __inv_mix_columns(self, s):

        for i in range(4):
            u = self.xtime(self.xtime(s[i][0] ^ s[i][2]))
            v = self.xtime(self.xtime(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        self.__mix_columns(s)


class Plaintext(AES):
    def __init__(self, text):
        AES.__init__(self)
        self.data = text


class EncData(AES):
    def __init__(self, data):
        AES.__init__(self)
        self.data = data


if __name__ == "__main__":
    text = input()
