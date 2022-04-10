import pickle
#pickle  可以理解为持久化
a = 1.588
#写入pickle持久化，就是保存，只能用于少数据的存储，每次写入会把上次的数据覆盖
with open('test_plk/test.plk','wb') as w:
    pickle.dump(a,w)


#读取pickle持久化
with open('test_plk/test.plk','rb') as r:
    data = pickle.load(r)
    print(data)
