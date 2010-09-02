# -*- coding: utf-8 -*-
"""
    logbook
    ~~~~~~~

    Simple logging library that aims to support desktop, command line
    and web applications alike.

    :copyright: (c) 2010 by Armin Ronacher, Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

from logbook.base import LogRecord, Logger, LoggerGroup, NestedSetup, \
     Processor, get_level_name, lookup_level, CRITICAL, ERROR, WARNING, \
     NOTICE, INFO, DEBUG, NOTSET
from logbook.handlers import Handler, StreamHandler, FileHandler, \
     StderrHandler, RotatingFileHandler, TimedRotatingFileHandler, \
     TestHandler, MailHandler, SyslogHandler, NullHandler, \
     NTEventLogHandler, create_syshandler, StringFormatter


# create an anonymous default logger and provide all important
# methods of that logger as global functions
_default_logger = Logger('default')
debug = _default_logger.debug
info = _default_logger.info
warn = _default_logger.warn
warning = _default_logger.warning
notice = _default_logger.notice
error = _default_logger.error
exception = _default_logger.exception
catch_exceptions = _default_logger.catch_exceptions
critical = _default_logger.critical
log = _default_logger.log
del _default_logger


# install a default global handler
default_handler = StderrHandler()
default_handler.push_application()
