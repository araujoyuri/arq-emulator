import string


class CPU:
    proc_register: dict = {}

    @staticmethod
    def receive_interruption(address, size):
        CPU.ask_for_ram(address, size)

    @staticmethod
    def ask_for_ram(address, size):
        from src.bus import Bus
        addr = Bus.fetch_from_ram(address, size)
        CPU.process_instruction(addr['instruction'], addr['size'])

    @staticmethod
    def process_instruction(instruction, size):
        decoded_instruction = instruction.decode('utf-8')\
            .replace('(', '').replace(')', '').replace(' ', '')\
            .replace("'", '').split(',')
        if decoded_instruction[0] == 'add':
            CPU.add_op(decoded_instruction[1], decoded_instruction[2])
        elif decoded_instruction[0] == 'mov':
            CPU.mov_op(decoded_instruction[1], decoded_instruction[2])
        elif decoded_instruction[0] == 'inc':
            CPU.inc_op(decoded_instruction[1])
        elif decoded_instruction[0] == 'imul':
            if len(decoded_instruction) == 3:
                CPU.imul_op(decoded_instruction[1], decoded_instruction[2])
            elif len(decoded_instruction) == 4:
                CPU.imul_op(decoded_instruction[1],
                            decoded_instruction[2],
                            decoded_instruction[3])
            else:
                print('Comando mal formatado')

    @classmethod
    def add_op(cls, reg, val):
        if reg not in cls.proc_register:
            cls.proc_register[reg] = 0

        if val in string.ascii_uppercase:
            if val in cls.proc_register:
                cls.proc_register[reg] += cls.proc_register[val]
                print('### Registradores ###')
                print(reg + ':', str(cls.proc_register[reg]))
                print(val + ':', str(cls.proc_register[val]))
                return
            else:
                cls.proc_register[val] = 0
                cls.proc_register[reg] += cls.proc_register[val]
                print('### Registradores ###')
                print(reg + ':', str(cls.proc_register[reg]))
                print(val + ':', str(cls.proc_register[val]))
                return

        cls.proc_register[reg] += int(val)
        print('### Registradores ###')
        print(reg + ':', cls.proc_register[reg])

    @classmethod
    def mov_op(cls, reg, val):
        if reg not in cls.proc_register:
            cls.proc_register[reg] = 0

        if val in string.ascii_uppercase:
            if val in cls.proc_register:
                cls.proc_register[reg] = cls.proc_register[val]
                print('### Registradores ###')
                print(reg + ':', str(cls.proc_register[reg]))
                print(val + ':', str(cls.proc_register[val]))
                return
            else:
                cls.proc_register[val] = 0
                cls.proc_register[reg] = cls.proc_register[val]
                print('### Registradores ###')
                print(reg + ':', str(cls.proc_register[reg]))
                print(val + ':', str(cls.proc_register[val]))
                return

        cls.proc_register[reg] = int(val)
        print('### Registradores ###')
        print(reg + ':', cls.proc_register[reg])

    @classmethod
    def inc_op(cls, reg):
        if reg not in cls.proc_register:
            cls.proc_register[reg] = 0

        cls.proc_register[reg] += 1
        print('### Registradores ###')
        print(reg + ':', str(cls.proc_register[reg]))

    @classmethod
    def imul_op(cls, reg, reg_mult1, reg_mult2=None):
        if reg not in cls.proc_register:
            cls.proc_register[reg] = 0

        if reg_mult1 in string.ascii_uppercase and reg_mult2 in \
                string.ascii_uppercase:
            if reg_mult1 not in cls.proc_register:
                cls.proc_register[reg_mult1] = 0

            if reg_mult2 not in cls.proc_register:
                cls.proc_register[reg_mult2] = 0

            cls.proc_register[reg] = int(cls.proc_register[reg_mult1]) * \
                                     int(cls.proc_register[reg_mult2])
            print('### Registradores ###')
            print(reg + ':', str(cls.proc_register[reg]))
            print(reg_mult1 + ':', str(cls.proc_register[reg_mult1]))
            print(reg_mult2 + ':', str(cls.proc_register[reg_mult2]))
            return

        elif reg_mult1 in string.ascii_uppercase and reg_mult2 not in \
                string.ascii_uppercase:
            if reg_mult1 not in cls.proc_register:
                cls.proc_register[reg_mult1] = 0

            cls.proc_register[reg] = int(cls.proc_register[reg_mult1]) * int(reg_mult2)
            print('### Registradores ###')
            print(reg + ':', str(cls.proc_register[reg]))
            print(reg_mult1 + ':', str(cls.proc_register[reg_mult1]))
            return

        elif reg_mult1 not in string.ascii_uppercase and reg_mult2 in \
                string.ascii_uppercase:
            if reg_mult2 not in cls.proc_register:
                cls.proc_register[reg_mult2] = 0

            cls.proc_register[reg] = int(reg_mult1) * int(cls.proc_register[reg_mult2])
            print('### Registradores ###')
            print(reg + ':', str(cls.proc_register[reg]))
            print(reg_mult2 + ':', str(cls.proc_register[reg_mult2]))
            return

        elif reg_mult1 not in string.ascii_uppercase and reg_mult2 not in \
                string.ascii_uppercase:
            cls.proc_register[reg] = int(reg_mult1) * int(reg_mult2)
            return

        if reg_mult1.isDigit():
            cls.proc_register[reg] *= int(reg_mult1)
            print('### Registradores ###')
            print(reg + ':', str(cls.proc_register[reg]))

        else:
            if reg_mult1 not in cls.proc_register:
                cls.proc_register[reg_mult1] = 0

            cls.proc_register[reg] *= int(cls.proc_register[reg_mult1])
            print('### Registradores ###')
            print(reg + ':', str(cls.proc_register[reg]))
            print(reg_mult1 + ':', str(cls.proc_register[reg_mult1]))
            return
