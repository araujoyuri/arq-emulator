

class Ram:
    addresses: dict = {}

    @classmethod
    def keep_instruction(cls, instruct: bytearray, address: dict):
        cls.addresses[address] = instruct
        print('addresses: ', cls.addresses)
