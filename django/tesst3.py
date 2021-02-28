class Node(object):
    def __init__(self,sname):
        self.ichildren=[]
        self.sname=sname

    def __repr__(self):
        return " Node:{}".format(self.sname)

    def append(self,*args,**kwargs):
        self.ichildren.append(*args,**kwargs)

    def print_all_1(self):
        print(self)
        for ochild in self.ichildren:
            ochild.print_all_1()
    def print_all_2(self):
        def gen(o):
            iall=[o,]
            while iall:
                onext=iall.pop(o)
                iall.extend(onext.ichildren)
                yield onext
        for onode in gen(self):
            print(onode)
if __name__ == '__main__':
    oroot=Node('root')
    ochild1=Node('child1')
    ochild2=Node('child2')
    ochild3=Node('child3')
    ochild4=Node('child4')
    ochild5=Node('child5')
    ochild6=Node('child6')
    ochild7=Node('child7')
    ochild8=Node('child8')
    ochild9=Node('child9')
    ochild10=Node('child10')

    oroot.append(ochild1)
    oroot.append(ochild2)
    oroot.append(ochild3)

    ochild1.append(ochild4)
    ochild1.append(ochild5)
    ochild2.append(ochild6)
    ochild4.append(ochild7)
    ochild3.append(ochild8)
    ochild3.append(ochild9)
    ochild6.append(ochild10)


    print('---'*10)
    oroot.print_all_1()
    oroot.print_all_2()




