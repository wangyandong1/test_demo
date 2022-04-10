from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red.value)
print(Color.red.name)
print(Color['red'])
print(Color(2),'------------------------')
for color in Color:
    print(color)