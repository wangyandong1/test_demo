#变量练习
'''date = 100
str_date = str(date)
float_date = float(date)
print(str_date,float_date)'''
#列表list练习
list_date1 = [123123123]
list_date = [1,2,'网名',1.22]
list_date.append('添加')
list_date.insert(2,"2后面添加")
print(list_date)
list_date1.extend(list_date)
print(list_date1)
#排序
list_sort = [2,3,1,0,900,100]
list_sort.sort()
list_sort.sort(reverse=True)
print(list_sort)
print(list_sort.count(900))
print(len(list_sort))
print(1 in list_sort)
print(list_sort,list_sort[0:6:3])
list_str_dat = ['2020','10','22']
print('.'.join(list_str_dat))
