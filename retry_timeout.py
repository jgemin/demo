import requests

def send_request_with_retry(api_url, headers, data, timeout_duration=30, max_retries=3):
    """
    发送API请求并在超时时自动重试。

    :param api_url: API的URL。
    :param headers: 请求头。
    :param data: 请求的数据。
    :param timeout_duration: 超时时间（默认30秒）。
    :param max_retries: 最大重试次数（默认3次）。
    :return: API响应或超时错误。
    """
    for attempt in range(max_retries):
        try:
            response = requests.post(api_url, headers=headers, json=data, timeout=timeout_duration)
            return response.json()
        except requests.exceptions.Timeout:
            print(f"请求超时，正在重试...（第{attempt + 1}次）")
        except requests.exceptions.RequestException as e:
            return f"请求发生错误：{e}"

    return "请求超时，所有重试均失败。"

# 使用示例
api_key = 'YOUR_API_KEY'
api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
headers = {'Authorization': f'Bearer {api_key}'}
data = {'prompt': 'Translate the following English text to French: Hello, how are you?', 'max_tokens': 60}

response = send_request_with_retry(api_url, headers, data)
print(response)