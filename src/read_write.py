from src.bus import Bus
import string
import random


class ReadWrite:
    instruction: bytearray

    @classmethod
    def save_instruction(cls, bt_arr: bytearray, size: int):
        cls.instruction = bt_arr
        b = Bus()
        address = random.choice(string.ascii_uppercase) + str(random.randint(0, 9))
        b.send_to_ram(address, cls.instruction, size)
