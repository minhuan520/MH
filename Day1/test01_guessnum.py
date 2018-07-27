import random

num = int(input('猜下随机生成的数字：'))
age = random.randint(0, 100)
while num != age:
    if num > age:
        print('比你猜的小')
    else:
        print('比你猜的大')
    num = int(input('根据提示继续猜：'))
else:
    print('恭喜你猜对了')
