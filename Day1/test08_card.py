card = [{'name': '闵欢', 'age': '18', 'addr': '江苏', 'QQ': '534431'},
        {'name': '李怀', 'age': '20', 'addr': '上海', 'QQ': '341341'},
        {'name': '王五', 'age': '30', 'addr': '达到', 'QQ': '1321'}]


def print_menu():
    # 1.打印功能提示
    print('=' * 50)
    print('名片管理系统V0.01')
    print('1.添加一个新的名片')
    print('2.删除一个新的名片')
    print('3.修改一个新的名片')
    print('4.查询一个新的名片')
    print('5.查询全部名片')
    print('6.退出系统')


def insert():
    #插入新名片
    new_name = input('请输入姓名:')
    new_age = input('请输入年龄:')
    new_addr = input('请输入地址:')
    new_QQ = input('请输入QQ:')
    # 定义一个字典
    new_infor = {'name': new_name, 'age': new_age, 'addr': new_addr, 'QQ': new_QQ}
    card.append(new_infor)
    print(card)

def delUser(username):
    for i in card:
        if i['name'] == username:
            card.remove(i)
            break
    else:
        print('查无此人')

def select(username):
    for i in card:
        if i['name'] == username:
            print('%s\t%s\t%s\t%s\t' % (i['name'], i['age'], i['addr'], i['QQ']))
            break
    else:
        print('查无此人')

def selectAll():
    print('%s\t%s\t%s\t%s\t' % ('姓名', '年龄', '地址', 'QQ'))
    for i in card:
        print('%s\t%s\t%s\t%s\t' % (i['name'], i['age'], i['addr'], i['QQ']))

def update(username):
    for i in card:
        if i['name'] == username:
            print('你想修改的人信息如下')
            print('%s\t%s\t%s\t%s\t' % ('姓名', '年龄', '地址', 'QQ'))
            print('%s\t%s\t%s\t%s\t' % (i['name'], i['age'], i['addr'], i['QQ']))
            key = input('请问你想修改什么信息：姓名 or 年龄 or 地址 or QQ：')
            if key == '姓名':
                new_value = input('请问你想修改为什么')
                i['name'] = new_value
            elif key == '年龄':
                new_value = input('请问你想修改为什么')
                i['age'] = new_value
            elif key == '地址':
                new_value = input('请问你想修改为什么')
                i['addr'] = new_value
            elif key == 'QQ':
                new_value = input('请问你想修改为什么')
                i['QQ'] = new_value
            else:
                print('没有你要修改的对应信息')
            break
    else:
        print('查无此人')

def mian():
    print_menu()
    while True:
        num = int(input('请输入对应的操作序号：'))
        # 3.根据用户的数据执行对应功能
        if num == 1:
            insert()
        elif num == 2:
            username= input('请输入要删除的名字:')
            delUser(username)
        elif num == 3:
            username = input('请输入要修改的名字:')
            update(username)
        elif num == 4:
            username = input('请输入要删除的名字:')
            delUser(username)
        elif num == 5:
            selectAll()
        elif num == 6:
            break
        else:
            print('输入有误，请重新输入')

mian()
