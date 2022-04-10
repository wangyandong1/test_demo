# r = open('txts\教师.txt',mode = 'r+',encoding='utf-8')
# # print(r.tell())
# # count = r.read(5)    ##从文件指针所在的位置开始读3个字节
# # print(count)
# # print(r.tell())
# # print(r.seek(1))       #是按照字节定光标的位置
# # print(r.tell())       #告诉你光标的位置
# # values = r.read()
# # #value = r.write('张拉，23')
# # print(values,type(values))
# # values = r.readline()
# for value in r:
#     print(value.strip('\n'))
#
# r.close()
with open('txts\教师.txt',mode = 'r+',encoding='utf-8') as obj:
    print(obj.read())