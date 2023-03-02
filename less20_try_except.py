

import sys

filename = 'dir21.txt'

while True:
    try:
        filein = open(filename, "r", encoding='utf-16le')
    except Exception:
        print('Error!', sys.exc_info()[1])
        filename = input("Please enter correct filename:")
    else:
        for i, line in enumerate(filein, 1):
            print(i, '\t', line.strip())
        break