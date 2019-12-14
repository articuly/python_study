# coding:utf-8
import logging
import logging.handlers

# 创建一个日志器/记录器
logger = logging.getLogger('logger')

# 创建两个处理器
handler1 = logging.StreamHandler()  # 将日志消息发送到Stream，如标准输出
handler2 = logging.FileHandler(filename='./test.log')  # 将日志消息发送到文件

# 设置日志器处理的日志信息的最低级别
logger.setLevel(logging.DEBUG)
# 设置处理器的日志消息的最低级别
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)

# 输出格式
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

# 设置日志器所使用的处理器
logger.addHandler(handler1)
logger.addHandler(handler2)

# 注意，这里使用自定义的logger的输出方法，不使用原来logging.debug()
logger.debug('this is a debug message.')
logger.info('this is a info message.')
logger.warning('this is a warning message.')
logger.error('this is a error message.')
logger.critical('this is a critical message.')
