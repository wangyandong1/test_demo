import time
'''
 for循环
'''
# for i in range(10):
#     time.sleep(1)
#     print("holle,word")

i = 0
n = 3
while i < n :
    cishu = n - i
    print("您有{}次机会猜一位球星的名字！!!".format(cishu))
    name = input(" 请输入球星名字：")
    if name == 'zhangsan':
        print("恭喜你猜对了")
    else :
        print("很抱歉，你猜错了！！！")
        i = i + 1
print("您的机会已经用完，抱歉！！！")

