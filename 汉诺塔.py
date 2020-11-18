import time
def move(n,a,b,c,):
    if n ==1:
        print(a,'-->',c)
        #递归起始情况
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
while 1:
    start = time.clock()
    n=int(input('请输入层数：'))
    move(n,'a','b','c')
    end = time.clock()
    print('程序运行时间为%s毫秒'%(end-start))