def schoole(schoole_name,mojor,number,*args,score_line= 60,**kwargs):
    '''
    学校招生需要的数据
    :param schoole_name:
    :param mojor:
    :param number:
    :param args:
    :param score_line:
    :param kwargs:
    :return:
    '''
    print('大学名称',schoole_name)
    print('专业',mojor)
    print('招生分数线',score_line)
    list_name = []
    list_score = []
    list_pass = []
    list_pass_name = []
    for k,v in kwargs.items():
        global list_score,list_pass,list_pass_name,list_name
        print('key的值：',k)
        print('value的值：',v)
        list_name.append(k)
        list_score.append(v)
        if v > score_line:
            print('key的值：',k)
            print('value的值：',v)
            list_pass.append(v)
            list_pass_name.append(k)
    print('招生人数',number)
    print('招生老师名单',args)
    print('报考考生及其高考成绩',kwargs)
    print('报考人数',len(list_name))
    print('达线人数',len(list_pass))
    print('录入名单',list_pass_name)
    print('录取人数',len(list_name))
schoole('上海大学','计算机','30','小明','小王','小张',网名 = 66,大张伟 = 59)

print(schoole.__doc__)


dict = {'网名': 66, '大张伟': 59}
print(dict.items())
