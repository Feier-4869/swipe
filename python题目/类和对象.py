class StudenT(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sthdy(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能让看《熊出没》' % self.name)
        else:
            print('%s正在观看日本动漫' % self.name)

if __name__ == '__main__':
    stu = StudenT('feier', 18)
    stu.sthdy('python')
    stu.watch_movie()
