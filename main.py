###############################################################
##
#  by sordidlist
##
###############################################################

import argparse
import time

from alive_progress import alive_bar
from fabulous import color

import animate
import colors
from config import Configuration

title = color.bold(colors.bg_e7ef00(" A NICE TITLE "))
config = None


def show_banner():
    animate.flashing(title, end_state="on", repetitions=3, slowest_delay=1)
    fish_length = 400
    with alive_bar(fish_length, bar='fish', monitor=False, stats=False, elapsed=False, spinner=None) as bar:
        for i in range(fish_length):
            time.sleep(0.004)
            bar()


def configure():
    global config
    parser = argparse.ArgumentParser(description="Execute to conditionally copy remote FTP contents locally, then "
                                                 "auto-enumerate the retrieved content for sensitive information. "
                                                 "The goal is to expedite CTF enumeration.")
    parser.add_argument("--ip", required=True, help="The remote host IP address")
    parser.add_argument("--port", required=True, help="The remote host FTP port")
    parsed_args = parser.parse_args()
    config = Configuration(ip=parsed_args.ip, port=parsed_args.port)


if __name__ == '__main__':
    show_banner()
    configure()
