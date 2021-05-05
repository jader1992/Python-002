from multiprocessing import Process, Queue
import os, time


def write(q):
    print("启动write子进程: %s" % os.getpid())
    for i in ["A", "B", "C", "D"]:
        q.put(i)
        time.sleep(1)
    print("结束write子进程: %s" % os.getpid())


def read(q):
    print("启动wread子进程: %s" % os.getpid())
    while True:
        value = q.get(True)
        print(value)
    print("结束wread子进程: %s" % os.getpid())


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()  # 等待写入再结束
    pr.terminate()  # 发送结束信号
    print("父进程结束")
