
from multiprocessing import Process

def f(name):
    print(f"hello {name}")

def m(param):
    print(param)

if __name__ == '__main__':
    p = Process(target=f, args=('world',)) #启动一个子进程
    p.start() #子进程启动
    # p.join() #父进程要等待子进程结束

    m('ceshi')


# join([timeout])
# 如果可选参数 timeout 是 None （默认值），则该方法将阻塞，
# 直到调用 join() 方法的进程终止。如果 timeout 是一个正数，
# 它最多会阻塞 timeout 秒。
# 请注意，如果进程终止或方法超时，则该方法返回 None 。
# 检查进程的 exitcode 以确定它是否终止。
# 一个进程可以合并多次。
# 进程无法并入自身，因为这会导致死锁。
# 尝试在启动进程之前合并进程是错误的。