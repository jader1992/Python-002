from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

# 返回两个连接对象 Pipe()表示管道的两端
# 每个连接对象都有send()和recv()方法
# 请注意，如果两个进程何时连接
# 管道中的数据可能会损坏，当然同时使用管道的不同端进程不存在损害的风险
