# import json
# d = dict({'nmae':'feier','age':18})
# json_str = json.dumps(d)
# print(json_str, type(json_str))
#
# fan_json_str = json.loads(json_str)
# print(fan_json_str, type(fan_json_str))
# help(json.dump)

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score

    }
if __name__ == '__main__':
    std = Student('feier',18,100)
    # res=student2dict(std)
    # print(res)
    json_str=json.dumps(std,default=student2dict)
    # print(json_str,type(json_str))
    help(json.dumps)