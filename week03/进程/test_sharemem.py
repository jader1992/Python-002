from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.14
    for i in a:
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd'表示双精度浮点数，'ℹ'表示有符号整数
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num)