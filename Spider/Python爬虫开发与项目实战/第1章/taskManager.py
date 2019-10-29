import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 任务个数
task_number = 10
# 第一步：建立task_queue和result_queue，用来存放任务和结果
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)
def get_task():
    return task_queue
def get_result():
    return result_queue

class Queuemanager(BaseManager):
    pass

def win_run():
    # 第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
    # 将Queue对象在网络中暴露
    Queuemanager.register('get_task_queue', callable=get_task)
    Queuemanager.register('get_result_queue', callable=get_result)

    # 第三步：绑定端口 8001，设置验证口令’ling‘。这个相当于对象的初始化
    manager = Queuemanager(address=('127.0.0.1', 8001), authkey=b'ling')

    # 第四步：启动管理，监听信息通道
    manager.start()
    try:
        # 第五步：通过管理实例的方法获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        # 第六步：添加任务
        for url in ['ImageUrl_' + str(i) for i in range(10)]:
           print('put task %s ...' % url)
           task.put(url)

        # 获取返回结果
        print('try get result ..')
        for i in range(10):
            print('result is %s' % result.get(timeout=10))
    except:
        print('Manager error')
    finally:
        # 关闭管理
        manager.shutdown()


if __name__ == '__main__':
    freeze_support()
    win_run()
