def showdata (start,end):
    l = [1,2,3,4,'q',5]
    try:
        for i in range(start,end):
            print(l[i])
            print("我的数字:%d"%l[i])
    # except IndexError as e:
    #     print("错误提示：",e)
    except Exception as e:
        print("异常信息：",e)
    else:
        print("你运行成功了，真棒！")
showdata(0,8)
