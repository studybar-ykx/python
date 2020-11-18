import numpy as np
key = input('key=')
s = input('s=')
key_list=list(key)
s_list=list(s)
max=0
for i in range(len(key)):
    key_list[i]=int(key_list[i])-1
    if key_list[i]>max:
        max=key_list[i]
# print(key_list)
max=max+1
# print(max)
# row=len(s)//max
s_list_array=np.asarray(s_list)
# print(s_list_array)
s_list_array=s_list_array.reshape(-1,max)
# print(s_list_array)
encode_array=s_list_array[:,key_list]
encode_list=encode_array.tolist()
# print(encode_list)
encode_str=''
for i in range(len(s)//max):
    for j in range(max):
        encode_str=encode_str+encode_list[i][j]
print(encode_str)