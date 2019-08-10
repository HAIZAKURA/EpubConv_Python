# logger 記錄檔模組
import logging
import logging.config
import sys
import time
import os


class Logger(object):
    """Logger

    Logger level:
        CRITICAL    50
        ERROR	    40
        WARNING	    30
        INFO	    20
        DEBUG	    10
        NOTSET	     0
    """

    # def __init__(self, name='logger', level=logging.DEBUG):
    # logging.basicConfig(format='%(asctime)s %(levelname)s :\n%(message)s',
    #                    level=level, datefmt='%Y-%m-%d %H:%M:%S', filename='DBAPI.log', filemode='w')

    def __init__(self, name='logger', filehandler='INFO', streamhandler='INFO', workpath=None):
        """Logger

        Keyword Arguments:
            name {str} -- [name of logging] (default: {'logger'})
        """

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s : %(message)s')
        if not workpath:
            workpath = os.path.abspath(os.path.join(sys.argv[0], os.path.pardir))
        
        # log 檔案 handler
        file_handler = logging.FileHandler(
            f'{workpath}/epubconv.log', 'w', encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(getattr(logging, filehandler.upper()))

        # command handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(getattr(logging, streamhandler.upper()))
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def debug(self, function, msg):
        """ logging debug level

        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        message = f" * function: {function}, * msg: {msg}"
        self.logger.debug(message)

    def info(self, function, msg):
        """ logging info level

        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        message = f" * function: {function}, * msg: {msg}"
        self.logger.info(message)

    def warning(self, function, msg):
        """ logging warning level

        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        message = f" * function: {function}, * msg: {msg}"
        self.logger.warning(message)

    def error(self, function, msg):
        """ logging error level

        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        message = f" * function: {function}, * msg: {msg}"
        self.logger.error(message)
