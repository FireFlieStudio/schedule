from channel import channel
import threading ,time

#创建channel对象 每次执行线程限制为10
c = channel(10)

#定义要执行的函数
def foo(v,c):
    print(v)
    time.sleep(1)
    c.pop()

#分配任务
for i in range(30):
    t = threading.Thread(target=foo,args=(i,c)).start()
    c.put()

#等待全部任务执行完成
c.wait()
print("Done")