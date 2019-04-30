'''
    多进程和多线程最大的不用在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享，所有，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容改乱了。
'''

import time, threading


# 假定这是你的引号存款
balance = 0
# 创建锁
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()
        

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)