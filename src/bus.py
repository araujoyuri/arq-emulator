from src.ram import Ram
from src.cpu import CPU


class Bus:
    data_bus: list = []
    address_bus: list = []

    @classmethod
    def send_to_ram(cls, control):
        print('send to ram address: ', cls.address_bus[0])
        Ram.keep_instruction(cls.address_bus[0], cls.data_bus[0], control)

    @classmethod
    def set_data_bus(cls, payload, control):
        cls.data_bus.insert(control, payload)

    @classmethod
    def set_address_bus(cls, address, control):
        print('bus address: ', address)
        cls.address_bus.insert(control, address)

    @staticmethod
    def send_interruption(address, control):
        CPU.receive_interruption(address, control)

    @staticmethod
    def fetch_from_ram(address, control):
        return Ram.get_from_address(address, control)
