from random import uniform
from time import sleep
import sys
import colors


def typewrite(line, slowest_delay=0.3):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, slowest_delay))
    print()


if __name__ == '__main__':
    typewrite("testing out a typewriter effect")
    typewrite("testing it out with a faster speed setting", slowest_delay=0.05)
    # typewrite(colors.fg_3cbae0("testing it out with colors"), slowest_delay=0.14)
