'''
1. 导入Tkinter包的所有内容
2. 从Frame派生一个Application类，这是所有Widget的父容器
3. 实例化Application，并启动消息循环
'''

from tkinter import *

class Application(Frame):
    '''
    pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
    在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
    '''
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        
app = Application()
app.master.title('Hello World') # 设置窗口标题
app.mainloop() # 主消息循环