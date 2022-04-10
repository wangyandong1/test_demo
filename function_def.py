# def multi_values(num1,num2,*args):
#     print(num1,num2)
#     print(args)
#     # return args
# # values = multi_values([1,1,2,3])
# # print(values,type(values))
# list_date = [1,2,3,4,5,6]
# # multi_values(*list_date)
# multi_values(*list_date)
# # print(multi_values(*list_date))
# # print(multi_values(list_date))
def school(name,location,*args,date_founded = 2021,**kwargs):
    '''
    :param name: 学校名字
    :param location:
    :param args:
    :param date_founded:
    :param kwargs:
    :return:
    '''
    print('学校名字',name)
    print('学校地址',location)
    print('成立时间',date_founded)
    print('学员名单',args)
    print('课程与老师',kwargs)
school('万门大学','上海','gres','wangyd','dashen',date_founded=1988,正正= 'python基础',宁夫='Django')
help(school)


date = [3,5,6,7,8,2]
new_date = filter(lambda x:x>3,date)
print(list(new_date))

exam_result = {'张无忌':'88','赵敏':'77','蝙蝠侠':'99','超人':'100','无名':'55','小明':'38'}
exam_result = sorted(exam_result.items(),key = lambda d:d[1],reverse = True)
print(dict(exam_result))


