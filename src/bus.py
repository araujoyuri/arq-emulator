from src.ram import Ram
from src.cpu import CPU


class Bus:

    @staticmethod
    def send_to_ram(address, payload, size):
        Ram.keep_instruction(address, payload, size)

    @staticmethod
    def send_interruption(address, size):
        CPU.receive_interruption(address, size)

    @staticmethod
    def fetch_from_ram(address, size):
        return Ram.get_from_address(address, size)
