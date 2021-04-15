#!/usr/bin/env python
# -*- coding=utf-8 -*-

import logging

# 创建一个logging的实例logger
logger = logging.getLogger('Richard')
# 设定全局日志级别为DEBUG
logger.setLevel(logging.INFO)
# 创建一个屏幕的handler，并且设定级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 创建一个日志文件的handler，并且设定级别为DEBUG
fh = logging.FileHandler("access.log")
fh.setLevel(logging.CRITICAL)
# 设置日志的格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)
# 'application' code
logger.debug("debug message")
logger.info("info message")
# logger.warn("warn message")
logger.error("error message")
logger.critical("crititcal message")
