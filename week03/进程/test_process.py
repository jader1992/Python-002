from multiprocessing import Process


#  参数
# multiprocessing.Process(self, group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

# - group: 分组,实际上很少使用
# - target: 表示调用对象，你可以传入方法的名字
# - name: 别名，相当于给进程取一个名字
# - args: 表示被调用对象的位置参数元组,比如target是函数a,他有两个参数m, n,那么args就传入（m,n）
# - kwargs:  表示被调用的字典


def f(name):
    print(f"hello {name}")


def m(param):
    print(param)


if __name__ == '__main__':
    p = Process(target=f, args=('world',))  # 启动一个子进程
    p.start()  # 子进程启动
    p.join(2) # 父进程要等待子进程 结束

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
