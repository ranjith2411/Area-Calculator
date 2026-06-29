import math
print("--------------------------------------")
print("           Area Calculator 📐            ")
print("--------------------------------------")

print('\n1) Triangle')
print('\n2) Rectangle')
print('\n3) square')
print('\n4) circle')
print('\n5) Quit')
side = 0
length = 0
width = 0
radius = 0
height = 0

shape = int(input('Enter a shape:  '))

if shape == 1:
    base = int(input("Enter the base:  "))
    height = int(input("Enter the height:  "))
    area = (height*base)/2
    print(area)
elif shape == 2:
    length = int(input("Enter the length:  "))
    width = int(input("Enter the width:  "))
    area = length*width
    print(area)
elif shape == 3:
    side = int(input("Enter the side:  "))
    area = side**2
    print(area)
elif shape == 4:
    radius = float(input("Enter the radius:  "))
    area = 3.14*radius**2
    print(area)
elif shape == 5:
    print("quit")
else:
    print('Invalid choice')
