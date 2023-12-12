from multiprocessing import Process
import time
import random
 
 
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
 
    def run(self):
        print("我的名字是%s" % self.name)
 
 
if __name__ == '__main__':
    p = MyProcess('张三')
    print("开始")
    p.start()
    print(p.is_alive())
    p.terminate()
    p.join()
    # time.sleep(2)
    print("结束")
    print(p.is_alive())