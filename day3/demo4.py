import threading
import time

g_num = 0

def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("--test1---g_num=%d"%g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("--test2--g_num=%d"%g_num)

mutex = threading.Lock()
p1 = threading.Thread(target=test1,args=(1000000,))
p1.start()

p2 = threading.Thread(target=test2,args=(1000000,))
p2.start()

while len(threading.enumerate()) !=1:
    time.sleep(1)
print("2个线程对同一个全局变量之后的最终结果是：%s" %g_num)

a = "/b/10/10344/27003362.html"
print(a[12:])