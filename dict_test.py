import json
#  #创建一个字典
# info = {"姓名":"大张伟","年龄":39,"性别":"男"}
# #字典表基本操作
# #增加数据
# info['公司'] = '上海传媒有限公司'
# print(info)
# #修改数据
# info['年龄'] = 38
# print(info)
# #查询
# print(info['公司'])
# print(info.get('婚姻状况'))
# print(info)
# print(len(info))
# print(type(info))

#基于列表创建字典表
lists = ['年龄','性别','身高','爱好']
#new_dict  = dict.fromkeys(lists,可以设置值，否则认为None)
new_dict  = dict.fromkeys(lists,20)
#基于键查询包含关系
print(new_dict)
print('年龄' in new_dict)
print(new_dict.keys(),new_dict.values())
# for k,v in new_dict.items():
#     print(k,v)

lists.append('学历')
lists.insert(2,'穿衣打扮')
print(lists)
join_lists = ','.join(lists)
print(join_lists)
print(lists[0])