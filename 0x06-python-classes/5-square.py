#!/usr/bin/python3
"""class Square that defines a square by:
Private instance attribute: size:
- property def size(self)
- property setter def size(self, value)
Instantiation with optional size.
Public instance method: def area(self).
Public instance method: def my_print(self).
"""


class Square:
    """Initializes the data."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    """Prints to stdout the square with the character #."""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
