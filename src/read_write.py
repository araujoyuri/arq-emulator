from src.bus import Bus
import string
import random
import re


class ReadWrite:
    instruction: list
    control: int = 0

    @classmethod
    def save_instruction(cls, bt_arr: list):
        cls.instruction = bt_arr
        b = Bus()
        print(str(bt_arr[1]))
        if re.match(r'0x(\w+)', bt_arr[1].decode('utf-8')):
            address = bt_arr[1].decode('utf-8')
        else:
            address = random.choice(string.ascii_uppercase) + str(random.randint(0, 9))
        print('address: ', address)
        b.set_address_bus(address, cls.control)
        b.set_data_bus(cls.instruction, cls.control)
        b.send_to_ram(cls.control)
        b.send_interruption(address, cls.control)
        cls.control += 1
