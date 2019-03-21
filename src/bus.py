from ram import Ram
import string
import random


class Bus:
    payload: bytearray

    def send_to_ram(self):

        Ram.keep_instruction(instruct=self.payload,
                             address=random.choice(string.ascii_uppercase))
