import json
personal_info = ['王艳东',32]
personal_info.append('上海东正金融股份有限公司')
print(personal_info)
personal_info.insert(1,'33')
personal_info.append('本科')
personal_info.insert(3,'测试工程师')
print(personal_info)
personal_info[1] = 32
print(personal_info)
personal_info.pop()
print(personal_info)
#删除值，删除找到的值
personal_info.remove(32)
personal_info.remove(32)
print(personal_info)
# personal_info.clear()
# print(personal_info)
list = [1,2,1,5,8,2,1,666,99999,555,999]
#排序，正序
list.sort()
print(list)
#倒叙
list.sort(reverse=True)
print(list)
#元素统计
print(list.count(1))
print(len(list))

print('%%'.join(personal_info))
# del personal_info
# print(personal_info)
#
#
#
list2 = ['aaa.jpg','bbbbbb.pdf','jkkk.word']
# for list in list2:
#     print(list.split('.')[0])
list3 = []
for list1 in list2:
    # print(list1)
    list3.append(list1.split('.')[0])
print(list3)

# # 列表的几个小功能max、min、sum函数
# num = [1,2,3,5,6,7]
# print(max(num))
# print(min(num))
# print(sum(num))
#
# levels = [
#     ['软件测试初级','软件测试中级','软件测试高级'],
#     ['开发初级','高级开发组长','开发经理'],
#     ['初级','中级','高级','领导']
# ]
# for level in levels:
#     print(level)
#     for i in level:
#         print(i)

classmates = [
    ['张小斐','女',32,'湖北'],
    ['贾玲','女',38,'北京'],
    ['沈腾','男',39,'沈阳'],
    ['迪丽热巴','女',22,'大连'],
    ['王艳东','男',32,'河南']
]
# men_count = []
# for men in classmates:
#     if men[2] > 30:
#         men_count.append(men)
# print(men_count,end = '\r\n')
# print(len(men_count))

# men_count = []
# for men in classmates:
#     men_count.append(men[3])
# print(men_count)
# print(max(men_count))
# print(min(men_count))