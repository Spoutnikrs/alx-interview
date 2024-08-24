#!/usr/bin/python3
"""Define function validUTF8"""


def validUTF8(data):
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        if byte >> 3 == 0b11110:  # 4-byte character
            length = 4
        elif byte >> 4 == 0b1110:  # 3-byte character
            length = 3
        elif byte >> 5 == 0b110:  # 2-byte character
            length = 2
        elif byte >> 7 == 0:  # 1-byte character
            length = 1
        else:
            return False  # Invalid leading byte

        if i + length > len(data) or any(not is_continuation(data[i + j]) for j in range(1, length)):
            return False
        i += length

    return True
