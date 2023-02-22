""" Works only on linux systems"""
import resource
import requests


def memory_manager(memory_limit_in_bytes, url=None):
    resource.setrlimit(resource.RLIMIT_AS, (memory_limit_in_bytes, memory_limit_in_bytes))

    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > memory_limit_in_bytes:
        data = {'message': 'Memory usage exceeded the limit!'}
        if not url:
            print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        response = requests.post(url, data=data)
        return response.text
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    mem_current = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Initial memory usage: {mem_init} KB")
    print(f"Current memory usage: {mem_current} KB")
    

if __name__ == "__main__":
    memory_limit = 100 * 1024 * 1024  # 100 Mb
    memory_manager(memory_limit)
