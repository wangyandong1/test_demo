import time,random,datetime
import pickle
import os
import json
my_data = [
    'Sophia',
    'Emma',
    'Mia'
]
#简单说一下枚举
# for i,data in enumerate(my_data):
#     print(i,data)
def writeTEST():
    #非第一次写
    if os.path.exists('test_plk/counter.plk'):
        with open('test_plk/counter.plk','rb')as r:
            counter = pickle.load(r)
            print(counter)
        #写入数据，
        with open('txts/test.txt','a')as w:
            for i,data in enumerate(my_data[0:2]):
                time.sleep(random.uniform(0,1))
                w.write(str(i+counter)+' '+str(data)+' '+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'\n')
         #保存，当前总行数 为后面的计数做好准备
        with open('test_plk/counter.plk','wb')as w:
            with open('txts/counter.plk','rb')as r:
                print(r.readline())
                counter  = len(r.readline())
                pickle.dump(counter,w)
    #第一次写
    else:
         with open('txts/test.txt','a') as w:
             for i,data in enumerate(my_data[0:2]):
                 time.sleep(random.uniform(0,1))
                 w.write(str(i)+' '+str(data)+' '+str(
                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'\n')
         with open('test_plk/counter.plk','wb') as w:

             counter = len(my_data[0:2])
             pickle.dump(counter,w)

# writeTEST()
def readTxt():
    with open('txts/test.txt','r')  as r:
        for x in r.readlines():
            # print(x)
            print()
            print(x.strip().split(' '))
# readTxt()
#插入操作
def insert_data(pss,name):
    new = []
    with open('txts/test.txt','r+')  as r:
        for data in r.readline():
            print(data.strip())
            new.append(' '.join(data.strip().split(' ')[1:2]))
    print(new)
insert_data(1,2)