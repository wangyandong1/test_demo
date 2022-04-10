def multi_values(*args):
    print(args)
    return args
tuple1 = multi_values(1,1,2,3,4)
print(tuple1)
list_date = [1,2,32,3,6]
multi_values(*list_date)

def multi_value(**kwargs):
    print(kwargs)
    return kwargs
dict = {'性别':'男'}
multi_value(**dict)

result = lambda x : x*2
print(result(8))
a = 1
b = 2
result2 = 'a大于b' if a > b else 'a小于b'
print(result2)
exam_result = {'张无忌':88,'赵敏':77,'蝙蝠侠':99,'超人':10000,'无名':55,'小明':38}
exam_result2 = sorted(exam_result.items(),key = lambda d : d[1],reverse = False)
print(exam_result2,type(exam_result2))
dict = {}
for i in exam_result2:
    dict[i[0]] = i[1]
print(dict,type(dict))



