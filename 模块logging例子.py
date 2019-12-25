# coding:utf-8
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'LSL'}
logging.debug('debug log.', extra=d)
logging.info('info log.', extra=d)
logging.warning('warning log.', extra=d)
logging.error('error log.', extra=d)
logging.critical('critical log.', extra=d)
