#!/usr/bin/env python3

"""
Demo syslog & console loggers
"""

import logging
import logging.handlers

from pythonjsonlogger import jsonlogger

_STREAM_FORMAT = '%(asctime)s %(message)s'

def configure_logging():
    """
    Configure console and syslog loggers
    """

    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter(_STREAM_FORMAT)
    stream_handler.setFormatter(stream_formatter)

    syslog_formatter = jsonlogger.JsonFormatter()
    syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
    syslog_handler.ident = 'bash_logging '
    syslog_handler.setFormatter(syslog_formatter)

    root = logging.getLogger()

    root.setLevel(logging.DEBUG)
    root.addHandler(stream_handler)
    root.addHandler(syslog_handler)


def main():
    """
    The entry point
    """
    configure_logging()
    logging.info('Sample message')


if __name__ == '__main__':
    main()
