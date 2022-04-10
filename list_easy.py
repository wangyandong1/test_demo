list = [x+2 for x in range(1000) if x%2 != 0]
print(list)
list2 = [x for x in range(100) if x%2 == 0]
dict = {x:y for x,y in zip(list,list2)}
print(dict)