

class Ram:
    addresses: dict = {}

    @classmethod
    def keep_instruction(cls, address: str, instruct: bytearray, size: int):
        print('ram address: ', address)
        cls.addresses[address] = {
            'instruction': instruct,
            'size': size
        }

    @classmethod
    def get_from_address(cls, address, size):
        return cls.addresses[address]
