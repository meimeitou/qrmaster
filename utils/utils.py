import logging
from config import Config
#custom logger

class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(
            self,
            filename,
            level='info',
            fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    ):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  #日志格式
        self.logger.setLevel(self.level_relations.get(level))  #日志级别
        sh = logging.StreamHandler()  #屏幕输出
        sh.setFormatter(format_str)  #显示的格式
        self.logger.addHandler(sh)  #把对象加到logger里

logger = Logger('all.log', level='debug' if Config.DEBUG else 'info').logger
