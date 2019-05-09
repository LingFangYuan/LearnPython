import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s -%(message)s')
#logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__) # 创建记录器
logger.setLevel(level=logging.INFO)  # 给记录器设置日志等级
handler = logging.FileHandler("./log/log.txt") # 创建文件处理器
handler.setLevel(logging.WARNING) # 给文件处理器设置日志等级
# 格式化消息
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter) # 给文件处理器设置格式化消息
logger.addHandler(handler)  # 把文件处理器添加到记录器

if __name__ == '__main__':
    try:
       10/0
    except ZeroDivisionError as e:
        print(str(e))
        print("ddddd")
        
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
    print("END")