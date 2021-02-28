
def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
            # print(fs_list)
        for number in range(1, 1000):
            if is_prime:
                if number < 10:
                    fs_list[0].write(str(number) + '\n')
                elif number < 100:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

import math
# def is_prime(n):
    # assert n > 0
    # for factor in range(2, int(math.sqrt(n) + 1)):
    #     if n % factor == 0:
    #         return  False
    #     return True if n != 1 else False

def is_prime(n):
    for i in range(2, n):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count == 2:
             print(i)
if __name__ == '__main__':
    main()