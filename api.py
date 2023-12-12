import openai
import time
# openai.log = "debug"
openai.api_key = "sk-AlCy6mob06CAWDSyiq6OyGYub4eLdA02JypYb8mTIvjMVzxn"
#openai.api_key = "sk-caEBdRMrzRgp00kprPP9u7MHlLcm9B2sDbidqXAYdYkQpXtT"
openai.api_base = "https://api.chatanywhere.com.cn/v1"
from timeout_decorator import timeout, TimeoutError
import functools
#from wrapt_timeout_decorator import timeout




# 非流式响应
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

def gpt_35_api_stream(queue, messages: list):
    """
    为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    completion = {'role': '', 'content': ''}
    for event in response:
        if event['choices'][0]['finish_reason'] == 'stop':
            #print(f'收到的完成数据: {completion}')
            break
        for delta_k, delta_v in event['choices'][0]['delta'].items():
            #print(f'流响应数据: {delta_k} = {delta_v}')
            completion[delta_k] += delta_v
    messages.append(completion)  # 直接在传入参数 messages 中追加消息
    
    queue.put(messages[1]["content"])


