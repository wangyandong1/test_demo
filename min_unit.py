date = lambda x : x**3
print(date(2))


date = [1,2,3,4,5]
new_date = list(map(lambda n : n+2,date))
print(new_date)

from functools import reduce
date = [1,2,3,4,5]
res = reduce(lambda x,y: x+y,date)
print(res)
list1 = [6,7,2,1,3]
list_xl = sorted(list1,reverse = True)
print(list_xl)

lists = ['年龄','性别','身高','爱好']
new_dict = dict.fromkeys(lists,20)
print(new_dict)

dict2 = {'年龄': 20, '多大': 21, '身高': 170, '爱好':211 }
new_dict2 = sorted(dict2.items(),key = lambda x:x[1],reverse = True)
print(dict(new_dict2))

dict_date = [(2,6,7,1),(6,8,1),(8,9,6,2),(2,6,8,9)]
new_dict_date = sorted(dict_date,key=lambda x:(x[0],x[1]),reverse = True)
print(new_dict_date)
import time
print(time.time())
