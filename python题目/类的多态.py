# 多态；指的是不同类型的变量进行相同的操作，
# 会根据对象类的不同而表现出不同的行为
# print(1 + 2)
# print('a' + "b")

class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('hello!：' + self.name)

class UserVip(User):
    def printUser(self):
        print('hello!尊敬的Vip用户：' + self.name)

class UserGeneral(User):
    def printUser(self):
        print('hello!尊敬的用户：' + self.name)


def printUserInfo(user):
    user.printUser()

if __name__ == '__main__':

    userVip = UserVip('feier')
    print(userVip)
    printUserInfo(userVip)
    userGeneral = UserGeneral('baoer')
    printUserInfo(userGeneral)


