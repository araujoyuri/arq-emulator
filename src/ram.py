

class Ram:
    addresses: list = []

    @classmethod
    def keep_instruction(cls, address: list, instruct: list, control: int):
        print('ram address: ', address)
        print('control: ', control)
        cls.addresses.insert(control, {'address': address,
                                       'instruction': instruct})

    @classmethod
    def get_from_address(cls, address, control):
        return cls.addresses[control]
