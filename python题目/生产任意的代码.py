import random
def generate_code(code_len=16):
    all_chars = '01233456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBN'
    last_pos = len((all_chars))-1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
# res = generate_code()
# print(res)

def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return '无'
#
# res = get_suffix('giujkjkkjloi778ooi')
# print(res)
def getSuffix(filename):
    pos = filename.rfind('.')
    if pos > 0:
        index = pos + 1
        return filename[index:]
    else:
        return 'nothing'


# res = getSuffix('feier.txt')
# print(res)

def getMaxList(l):
    l.sort()
    return '最大', l[-1], '第二大', l[-2]
# l1 = [5,7,8,0, 3, 8,9]
# res = getMaxList(l1)
# print(res)

def max2(x):
    m1, m2 = ([x[0], x[1]]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

# res = max2([0, 4, 6, 9, 5, 7, 10, 9, 7])
# print(res)
help(rfind)