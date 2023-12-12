import multiprocessing
import time
from api import gpt_35_api_stream 
import random
import re

# bar
def bar(queue,k):
    j=0
    for i in range(k):
        j+=1
    queue.put(j)

def control_running_time(messages):
        queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=gpt_35_api_stream, args=(queue,messages,))
        p.start()
        
        # Wait for N seconds or until process finishes
        p.join(50)

        # If thread is still active
        if p.is_alive():
            print ("running... let's kill it...")
            output = str(random.randint(0,10))
            # Terminate - may not work if process is stuck for good
            p.terminate()
            # OR Kill - will work for sure, no chance for process to finish nicely however
            # p.kill()

            
        else:
            output = queue.get()
            print("成功返回！")

        return output

    # print(len(queue))
        

if __name__ == '__main__':

    a_batch = []
    for _ in range(10):
        messages = [{"role": "user", "content": "Here are two English sentences, one is 'Steve Jobs is a great worker in apple company, and he works as the CEO of it', and the other is 'Steve Jobs is the CEO of Apple company', please judge the similarity value between them, the similarity value ranges from 0 to 10, 0 means the most different, and 10 means the most similar, please give me the similarity value"}]

        m = control_running_time(messages)
        
        a = []
        a = re.findall("\d+\.?\d*", m)
        # 提取浮点数加入到列表
        a = list(map(float, a))
        # 判断列表是否为空，若为空则再次api请求，否则返回列表内的浮点数的值
        if len(a) == 0:
             a = 0
        a_batch.append(a[0])

    print(a_batch)
        
        