#!/usr/bin/python3
""" utf8 validation module """


def validUTF8(data):
    """ validate whether a data is utf8 or not """

    data = [i & 255 for i in data]
    ONE_BYTE = 0        # 00000000
    TWO_BYTE = 192      # 11000000
    THREE_BYTE = 224    # 11100000
    FOUR_BYTE = 240     # 11110000
    FIVE_BYTE = 248     # 11111000
    OTHER_BYTE = 128    # 10000000
    while len(data) is not 0:
        if not (data[0] & OTHER_BYTE):
            data.pop(0)
            continue
        elif not ((data[0] & THREE_BYTE) ^ TWO_BYTE):
            if len(data) < 2:
                return False
            if not ((data[1] & TWO_BYTE) ^ OTHER_BYTE):
                data = data[2:]
            else:
                return False
        elif not ((data[0] & FOUR_BYTE) ^ THREE_BYTE):
            if len(data) < 3:
                return False
            if not ((data[1] & TWO_BYTE) ^ OTHER_BYTE) and \
                    not ((data[2] & TWO_BYTE) ^ OTHER_BYTE):
                data = data[3:]
            else:
                return False
        elif not ((data[0] & FIVE_BYTE) ^ FOUR_BYTE):
            if len(data) < 4:
                return False
            if not ((data[1] & TWO_BYTE) ^ OTHER_BYTE) and \
                    not ((data[2] & TWO_BYTE) ^ OTHER_BYTE) and \
                    not ((data[3] & TWO_BYTE) ^ OTHER_BYTE):
                data = data[4:]
            else:
                return False
        else:
            return False
    return True
