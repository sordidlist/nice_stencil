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


def flashing(line, slowest_delay=0.3, repetitions=10, end_state='off'):
    for rep in range(repetitions):
        print(line, end='')
        sleep(slowest_delay)
        print('', end='\r')
        sleep(slowest_delay)
        if (end_state == 'on') & (rep == (len(range(repetitions)) - 1)):
            print(line)
            break


if __name__ == '__main__':
    typewrite("testing out a typewriter effect")
    typewrite("testing it out with a faster speed setting", slowest_delay=0.05)
    flashing(colors.bg_d40558(colors.fg_faa028(" transient example ")), repetitions=2)
    flashing(colors.bg_3cce68(colors.fg_101918(" persistent example ")), repetitions=2, end_state='on')
