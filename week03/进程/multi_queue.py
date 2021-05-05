from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue(maxsize=10)
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    print(q.get())  # [42, None, 'hello']
    while not q.empty():
        print(q.get())
