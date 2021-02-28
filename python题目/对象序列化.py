# import pickle
#
#
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# if __name__ == '__main__':
#     per1 = Person('feier', 19)
#     per2 = Person('baoer', 5)
#     per3 = Person('me', 25)
# list1 = [per1, per2, per3]
# with open('person.txt', 'wb') as f:
#     # for i in list1:
#     f.write(pickle.dumps(list1))
# with open('person.txt', 'rb') as f2:
#     list2 = pickle.loads(f2.read())
#     # print(res, type(res), dir(res))
#     print(list2, type(list2))
#     print(list2[1].name)
#
import json


class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


def obj2dict(obj):
    return {
        'name': obj.name,
        'age': obj.age,
        'sex': obj.sex
    }


def dict2obj(dict1):
    return Student(dict1['name'], dict1['age'], dict1['sex'])


if __name__ == '__main__':
    stu1 = Student('feier', 18, 'girl')
    with open('demo2.txt', 'w') as f3:
        res = json.dumps(stu1, default=obj2dict)
        print(res, type(res))
        f3.write(res)
    with open('demo2.txt', "r") as f:
        res = f.read()
        stu2 = json.loads(res, object_hook=dict2obj)
        print(res, type(res))
        print(stu2, type(stu2))
        dict1 = json.loads(res)
        su = dict2obj(dict1)
        print(su)
