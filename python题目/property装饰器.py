class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def paly(self):
        if self._age <= 16:
            print('%s正在看儿童动漫' % self._name)
        else:
            print('%s正在看日本动漫' % self._name)

if __name__ == '__main__':
    per = Person('feier', 18)
    per.paly()
    per.age = 16
    per.paly()
    per.name='naoer'
    

