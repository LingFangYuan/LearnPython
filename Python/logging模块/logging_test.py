import logging
from logging.handlers import RotatingFileHandler


# logging.basicConfig(level=logging.DEBUG,
#                     # filename='log.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# 获取记录器
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)  # 设置日志等级
# 创建日志格式器
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建文件处理器
handler = logging.FileHandler('./log/log.log')
handler.setLevel(logging.WARNING)  # 设置日志等级
handler.setFormatter(formatter)  # 设置日志格式
# 创建流处理器
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)  # 设置日志等级
console.setFormatter(formatter)  # 设置日志格式
# # 回滚日志处理器
# r_handler = RotatingFileHandler('./log/log.log', maxBytes=1*1024, backupCount=3)
# r_handler.setLevel(logging.INFO)
# r_handler.setFormatter(formatter)
# 将处理器添加到记录器
logger.addHandler(handler)
logger.addHandler(console)
# logger.addHandler(r_handler)

# 输出日志
logger.info('Start pring log')
logger.debug('Do someting')
logger.warning('Something maybe fail.')
logger.info('Finish')

try:
    open('sdfs.txt', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logger.error('Fail to open sdfs.txt from logger.error', exc_info=True)

logger.info('Finish')
