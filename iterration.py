# list2 = [1,2,3,6,7]
# new_list = iter(list2)
# # print(next(new_list))
# # for i in new_list:
# #     print(i)
# print(list(new_list))
# for i in new_list:
#     yiled
class Stuedent():
    name = ''
    age = 10
    def __init__(self,name,age):
        name = name
        age = age
    def print_file(self):
        print('name:' + self.name)
        print("ang:" + str(self.age))
stu = Stuedent('xiao',28)
stu.print_file()
print(stu.__dict__)
print(Stuedent.__dict__)
