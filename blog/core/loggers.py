# loggers.py
import os
import logging
import colorlog
import logging.handlers
import types
import collections

LOG_SUCCESS = 100
LOG_NOTICE = logging.CRITICAL
LOG_ERROR = logging.ERROR
LOG_WARNING = logging.WARN
LOG_INFO = logging.INFO
LOG_DEBUG = logging.DEBUG

logger_map = collections.defaultdict(dict)


def get_log_method(level_name):
    def log(self, message, *args, **kwargs):
        if self.isEnabledFor(level_name):
            self._log(level_name, message, args, **kwargs)

    return log


class APILogger(logging.Logger):

    def __init__(self):
        name = "API"
        level = LOG_INFO
        super(APILogger, self).__init__(name, level=level)


class DBLogger(logging.Logger):

    def __init__(self):
        name = "DB"
        level = LOG_INFO
        super(DBLogger, self).__init__(name, level=level)


class MultipleLineColorFormatter(colorlog.ColoredFormatter):

    def format(self, record: logging.LogRecord) -> str:
        original_msg = record.msg
        if isinstance(record.msg, str):
            output = ""
            for line in record.msg.splitlines():
                record.msg = line
                output += f"{super().format(record)}\n"
            record.msg = original_msg
            record.message = output
            return output
        return super().format(record)


def get_logger(logger: logging.Logger):
    current_pid = os.getpid()
    logger_type = f"blog-{logger.name}".lower()
    logger_process = f"{current_pid}".lower()
    log_dir = "/tmp/blog/logs"
    log_file = f"{logger_type}.{logger_process}.log"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if logger_process in logger_map[logger_type]:
        return logger_map[logger_map][logger_process]

    formatter = MultipleLineColorFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(asctime)s %(pathname_log_color)s%(pathname)s->%(lineno)d %(message_log_color)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'bold_purple',
            'NOTICE': 'bold_cyan,bg_yellow',
            'WARNING': 'bold_yellow,bg_red',
            'ERROR': 'bold_yellow,bg_red',
            'CRITICAL': 'bold_red,bg_white',
            'SUCCESS': 'bold_white,bg_green',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'bold_white',
                'INFO': 'white',
                'NOTICE': 'bold_white',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_white',
                'CRITICAL': 'bold_red',
                'SUCCESS': 'bold_green',
            },
            "pathname": {
                'DEBUG': 'cyan',
                'INFO': 'cyan',
                'NOTICE': 'cyan',
                'WARNING': 'cyan,bg_red',
                'ERROR': 'bold_yellow,bg_red',
                'CRITICAL': 'cyan',
                'SUCCESS': 'yellow',
            }
        },
        style='%'
    )

    # file handler
    file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(log_dir, log_file),
        mode="a",
        maxBytes=1 * 1024 * 1024,
        backupCount=5,  # 5 backups at most
        encoding=None,
        delay=False
    )
    file_handler.setFormatter(formatter)
    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.success = types.MethodType(get_log_method(LOG_SUCCESS), logger)
    logger.notice = types.MethodType(get_log_method(LOG_NOTICE), logger)

    logger.success(f"Logging service starting...")
    logger_map[logger_type][logger_process] = logger
    return logger


api_logger = get_logger(APILogger())
db_logger = get_logger(DBLogger())
