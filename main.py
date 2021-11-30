###############################################################
##
#  by sordidlist
##
###############################################################

import argparse
import time

from alive_progress import alive_bar
import colors
from config import Configuration
from fabulous import color

title = ' a nice title '
config = Configuration(ip="10.10.10.10", port=0)


def show_banner():
    banner = colors.fg_4be998(title)
    fish_length = 400
    with alive_bar(fish_length, bar='fish', monitor=False, stats=False, elapsed=False, spinner=None) as bar:
        for i in range(fish_length):
            time.sleep(0.004)
            bar()
    print(banner)


def configure():
    global config
    parser = argparse.ArgumentParser(description="Execute to conditionally copy remote FTP contents locally, then "
                                                 "auto-enumerate the retrieved content for sensitive information. "
                                                 "The goal is to expedite CTF enumeration.")
    parser.add_argument("--ip", required=True, help="The remote host IP address")
    parser.add_argument("--port", required=True, help="The remote host FTP port")
    parsed_args = parser.parse_args()
    config.ip = parsed_args.ip
    config.port = parsed_args.port


if __name__ == '__main__':
    configure()
    show_banner()
