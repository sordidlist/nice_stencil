from fabulous import color
from pwn import log
import sys


class Configuration:
    ip = ""
    port = 0

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.validate()

    def validate(self):
        log.info(self.to_string())

    def to_string(self):
        config_string = "{}\n  Remote Host\t{}\n  Remote Port\t{}\n " \
            .format(color.bold("Configuration:"),
                    color.yellow(self.ip),
                    color.yellow(self.port))
        return config_string
