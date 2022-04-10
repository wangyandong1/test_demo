dict_demo = {}
print(dict_demo,type(dict_demo))
dict_demo['莫南'] = 20
dict_demo['神像'] = 20000000
print(dict_demo,type(dict_demo))
print('莫南' in dict_demo)
dict_demo1 = {}
for k,v in dict_demo.items():
    dict_demo1[k] = v
    print(k,v)
print("dict_demo1的值:",dict_demo1)
