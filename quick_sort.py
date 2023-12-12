import random
import pandas as pd
import matplotlib.pyplot as plt
import time
import timeit

def compute_time(function, array): # 计算运行时间
    start_time = timeit.default_timer()
    final_array = function(array)
    end_time = timeit.default_timer()
    cost_time = end_time -start_time
    return cost_time, final_array

def deter_quicksort(array): # deter_quicksort 代表确定性快速排序
    if len(array) <= 1: # 若待排序数组长度为1，则不需要进行额外排序，当前顺序即为有序
        return array
    
    position = len(array) // 2 # 向下取整作为枢轴位置下标
    pivot = array[position]
    left = [] # 放置比枢轴小的元素
    right = [] # 放置比枢轴大的元素
    for a in array:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)

    return deter_quicksort(left) + [pivot] + deter_quicksort(right) # 此时将数组从中间枢轴元素分为左右两部分，分别递归执行
            
def random_quicksort(array): # random_quicksort 代表随机性快速排序
    if len(array) <= 1: # 若待排序数组长度为1，则不需要进行额外排序，当前顺序即为有序
        return array
    
    pivot = random.choice(array) # 使用random模块的choice函数随机选取array中的一个数作为枢轴
    for a in array:
        left = []
        right = []
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)

    return random_quicksort(left) + [pivot] + random_quicksort(right) # 此时将数组从中间枢轴元素分为左右两部分，分别递归执行

if __name__ == '__main__':
    # num_data = [100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    num_data = [x for x in range(10000,10000001,5000) if x < 1000000]


    total_result = [] # 定义确定排序在不同数据规模下的运行时间list
    deter_time = 0.0
    random_time = 0.0
    for num_data_size in num_data:
        array = [random.randint(1,1800) for _ in range(num_data_size)]
        
        start_time_1 = time.time()
        deter_final_array = deter_quicksort(array)
        end_time_1 = time.time()
        deter_quicksort_time_costed = end_time_1 -start_time_1
        deter_time += deter_quicksort_time_costed
        print(deter_time)

        start_time_2 = time.time()
        rand_final_array = random_quicksort(array)
        end_time_2 = time.time()
        random_quicksort_time_costed = end_time_2 -start_time_2
        random_time += random_quicksort_time_costed
        print(random_time)

        total_result.append((num_data_size, deter_quicksort_time_costed, random_quicksort_time_costed))
        
    df = pd.DataFrame(total_result, columns = ["num_data_size", "deter_quicksort_time_costed", "random_quicksort_time_costed"])
    df.to_csv("result_3_step5000.csv")
    plt.plot(df["num_data_size"], df["deter_quicksort_time_costed"], label = "The result of deterministic quicksorting algorithm")
    plt.plot(df["num_data_size"], df["random_quicksort_time_costed"], label = "The result of random quicksorting algorithm")
    plt.title("Epoch-3 Step-5000")
    plt.xlabel("Length of array")
    plt.ylabel("Time costed(seconds)")
    plt.legend()
    plt.show()
    plt.savefig("./Picture_exp_3_step5000")

