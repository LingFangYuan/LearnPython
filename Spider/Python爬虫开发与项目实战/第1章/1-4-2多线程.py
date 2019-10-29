# # 把一个函数传入并创建Thread实例，然后调用start方法开始执行
# import random
# import time
# import threading


# def thread_run(urls):
#     print('Current %s is running...' % threading.current_thread().name)
#     for url in urls:
#         print('%s ---->>> %s' % (threading.current_thread().name, url))
#         time.sleep(random.random())
#     print('%s ended.' % threading.current_thread().name)


# if __name__ == '__main__':
#     print('%s is running...' % threading.current_thread().name)
#     t1 = threading.Thread(target=thread_run, name='Thread_1',
#                           args=(['url_1', 'url_2', 'url_3'],))
#     t2 = threading.Thread(target=thread_run, name='Thread_2',
#                           args=(['url_4', 'url_5', 'url_6'],))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('%s ended.' % threading.current_thread().name)


# # 从threading.Thread继承创建线程类。
# import random
# import threading
# import time


# class myThread(threading.Thread):

#     def __init__(self, name, urls):
#         super().__init__(name=name)
#         self.urls = urls

#     def run(self):
#         print('Current %s is running...' % threading.current_thread().name)
#         for url in self.urls:
#             print('%s ---->>> %s' % (threading.current_thread().name, url))
#             time.sleep(random.random())
#         print('%s ended.' % threading.current_thread().name)

# if __name__ == '__main__':
#     print('%s is running...' % threading.current_thread().name)
#     t1 = myThread(name='Thread_1', urls=['url_1', 'url_2', 'url_3'])
#     t2 = myThread(name='Thread_2', urls=['url_4', 'url_5', 'url_6'])
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('%s ended.' % threading.current_thread().name)


import threading

mylock = threading.RLock()
num = 0

class myThread(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('%s locked, Number: %d' % (threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print('%s released. Number: %d' % (threading.current_thread().name, num))
                break
            num += 1
            print('%s releaseed, Number: %d' % (threading.current_thread().name, num))
            mylock.release()


if __name__ == '__main__':
    t1 = myThread('Thread_1')
    t2 = myThread('Thread_2')
    t1.start()
    t2.start()
