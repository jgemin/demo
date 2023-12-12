#*****如何在没有回答的情况下直接杀死当前线程并返回值*****#
import multiprocessing
from multiprocessing import Process, Event
import time
from api import gpt_35_api_stream
"""
def b(n, queue):
    for _ in range(n):
        i = 0
        i += 1
    queue.put(n)

def a(n):

    queue = multiprocessing.Queue()
    process_b = Process(target=b, args=(n,queue,))
    process_b.start()

    try:
        # 设置函数 b() 的超时时间为5秒
        timeout_seconds = 1
        process_b.join(timeout=timeout_seconds)


        # 如果超时，终止 b() 进程
        if process_b.is_alive():
            print("a() execution timed out. Terminating process_b...")
            output = 0.0
            process_b.terminate()
            process_b.join()  # 等待进程 b() 结束
        else:
            output = queue.get()

        return output
    
    except Exception as err:
        print("adandkan")
"""
def a(messages):

    queue = multiprocessing.Queue()
    process_b = Process(target=gpt_35_api_stream, args=(queue,messages,))
    process_b.start()

    try:
        # 设置函数 b() 的超时时间为5秒
        timeout_seconds = 0.4
        process_b.join(timeout=timeout_seconds)


        # 如果超时，终止 b() 进程
        if process_b.is_alive():
            print("api function execution timed out. Terminating process_b...")
            output = '5.0'
            process_b.terminate()
            process_b.join()  # 等待进程 b() 结束
        else:
            output = queue.get()

        return output
    
    except Exception as err:
        print("adandkan")

if __name__ == "__main__":
    print("Start!!!!")
    for i in range(3):
        print(f"epoch: {i}")
        for _ in range(10):
            messages = [{"role": "user", "content": "Where is the capital of Guangdong Province ？"}]
            x = a(messages)
            print(x)