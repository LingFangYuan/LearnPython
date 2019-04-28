'''
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''

from multiprocessing import Pool
import os, time, random

