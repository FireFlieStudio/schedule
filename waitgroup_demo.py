from waitgroup import waitgroup
import threading ,time

#创建waitgroup对象 每次执行线程限制为10
wg = waitgroup(10)

#定义要执行的函数
def foo(v,wg):
    print(v)
    time.sleep(1)
    wg.done()

#分配任务
for i in range(30):
    t = threading.Thread(target=foo,args=(i,wg)).start()
    wg.add()

#等待全部任务执行完成
wg.wait()
print("Done")