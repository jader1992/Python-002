
import os
import time

res = os.fork()
print(res)
print(f'res == {res}')

if res == 0:
    print(f"我是孩子进程，我的pid {os.getpid()} 我的父进程id是: {os.getppid()}")
else:
    print(f"我是父进程,我的pid是: {os.getpid()}")