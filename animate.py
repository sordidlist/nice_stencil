from random import uniform
from time import sleep
import sys
import colors
from termcolor import cprint, colored


def typewrite(line, slowest_delay=0.3):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, slowest_delay))
    print()


def flashing(line, slowest_delay=0.3, repetitions=10, end_state='off', overwrite_length=25, mode='on-off'):
    overwrite = ' ' * overwrite_length
    for rep in range(repetitions - 1):
        sys.stdout.write("\r{}".format(line))
        line_rev = colored(line, attrs=['reverse'])
        sleep(slowest_delay)
        sys.stdout.write("\r{}".format(overwrite))
        if mode == 'reverse-colors':
            sys.stdout.write("\r{}".format(line_rev))
        sleep(slowest_delay)
    if end_state == 'off':
        sys.stdout.write("\r{}".format(line))
        sleep(slowest_delay)
        overwrite = ' ' * overwrite_length
        sys.stdout.write("\r{}".format(overwrite))
        sleep(slowest_delay)
    elif end_state == 'on':
        sys.stdout.write("\r")
        print(line)
        sleep(slowest_delay)


if __name__ == '__main__':
    # typewrite("testing out a typewriter effect")
    typewrite("testing it out with a faster speed setting", slowest_delay=0.05)
    flashing(colors.bg_d40558(colors.fg_faa028(" transient example ")), repetitions=3)
    flashing(colors.bg_d40558(colors.fg_faa028(" transient example with reversed colors ")), repetitions=3, mode='reverse-colors')
    flashing(colors.bg_3cce68(colors.fg_101918(" persistent example ")), repetitions=3, end_state='on')

    banner = colors.bg_d45378(colors.bg_d40558(" A FANCY BANNER "))
    flashing(banner, end_state="on", repetitions=3, slowest_delay=0.4)
