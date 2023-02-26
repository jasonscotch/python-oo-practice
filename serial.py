"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """ 
    
    def __init__(self, start=0):
        self.serial_number = self.start = start - 1

    def __repr__(self):
        return f"SerialGenerator start={self.start} next={self.serial_number}"
    
    def generate(self):
        self.serial_number += 1
        return self.serial_number

    def reset(self):
        self.serial_number = self.start
