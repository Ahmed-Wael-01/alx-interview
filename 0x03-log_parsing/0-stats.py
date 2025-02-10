#!/usr/bin/python3
"""reading and processing a stream of data"""
import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0

try:
    for line in sys.stdin:
        lines_l = line.split(" ")
        if len(lines_l) > 5:
            st_code = lines_l[-2]
            size = int(lines_l[-1])

            if st_code in status_codes.keys():
                status_codes[st_code] += 1

            total_size += size
            count += 1

            if count == 10:
                count = 0

                print('File size: {}'.format(total_size))
                for key, val in sorted(status_codes.items()):
                    if val != 0:
                        print('{}: {}'.format(key, val))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print('{}: {}'.format(key, val))
