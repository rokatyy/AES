import AES_standart


class Operations:
    def __init__(self):
        self.Sbox = AES_standart.Sbox
        self.InvSbox = AES_standart.InvSbox
        self.data = None

    def key_addition(self):
        pass

    def byte_substitution(self):
        pass

    def ShiftRows(self):
        pass

    def MixColumn(self):
        pass


class Plaintext(Operations):
    def __init__(self, text):
        Operations.__init__(self)
        self.data = text


class EncData(Operations):
    def __init__(self, data):
        Operations.__init__(self)
        self.data = data


if __name__ == "__main__":
    text = input()
