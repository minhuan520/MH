score = int(input('请输入你的分数：'))
if score >100 or score<0:
    print('请输入正确的分数')
elif score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=60:
    print('C')
else:
    print('D')
