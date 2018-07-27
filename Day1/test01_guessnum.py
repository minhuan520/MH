import random

age = random.randint(0, 100)
print(age)
num = int(input('猜下随机生成的数字：'))
n = 1
while n <= 3:
    if num == age:
        print('恭喜你猜对了')
    else:
        if num > age:
            print('比你猜的小')
        else:
            print('比你猜的大')
    num = int(input('根据提示继续猜：'))
    n += 1
else:
    print('你已猜错3次了，没有机会了')
