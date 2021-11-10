###############################################################
##
#  by sordidlist
##
###############################################################

import argparse

from config import Configuration

config = Configuration(ip="10.10.10.10", port=0)


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
