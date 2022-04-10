import re
tex = '''
万门大学学员：宁宁大
万门大学学员：证正小
万门大学学员：培培中
'''
pattern  = r'：(.+)'
res  = re.findall(pattern,tex)
print(res)