import shelve,os
#创建一个shelve持久化对象，注意这个是一种结构化的，可以对结构化数据就行修改
shv = shelve.open(r'test_plk/OSStask.db')
shv['a'] = [1,2,3]
shv['b'] = [3,2,1]
shv.sync()
shv.close()

#对shelve内的对象进行修改和添加
s1 = shelve.open('test_plk/OSStask.db',writeback=True)    #进行修改必须加上writeback=True
for x,y in s1.items():
    print(x,y)
s1.close()