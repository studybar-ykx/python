x=input('请输入单峰数组')
for i in range(1,len(x)):
    if x[i]>x[i-1] and x[i]>x[i+1]:
        print(x[i])
        break