import random

root = random.randint(0, 2)
print(root)
a = '恭喜你，你赢了'
b = '不好意思，你输了'
player = int(input('请输入 0 剪刀 1石头 2布：'))
while player == root:
    print('打平了，决战到天亮')
    player = int(input('请输入 0 剪刀 1石头 2布：'))
else:
    if player == 0 and root == 1:
        print(b)
    elif player == 0 and root == 2:
        print(a)
    elif player == 1 and root == 0:
        print(a)
    elif player == 1 and root == 2:
        print(b)
    elif player == 2 and root == 0:
        print(b)
    else:
        print(a)
