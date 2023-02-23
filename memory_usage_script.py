""" Works only on linux systems"""
import resource
import requests
from requests.exceptions import ConnectionError
import time


def memory_manager(memory_limit_in_bytes, url=None):
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > memory_limit_in_bytes:
        data = {'key': 'alarm',
                'value': f'Memory usage exceeded the limit!({resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} KB)'}
        if not url:
            print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        try:
            response = requests.post(url, json=data)
            print('Alarm message sent!')
            return response.status_code
        except ConnectionError:
            print('failed to send alarm message')
            return 'Connection refused'

    mem_current = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Current memory usage: {mem_current} KB")
    return mem_current


def run_script(memory_limit, url):
    while True:
        print('starting script')
        memory_manager(memory_limit, url)
        time.sleep(10)


if __name__ == "__main__":
    memory_limit = 20000  # 
    url = 'http://localhost:8080/api/create'
    run_script(memory_limit, url)
