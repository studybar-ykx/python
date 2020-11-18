key = 'cipher'
temp = key
s = 'cbihgbdmvprjcbupzv'
s_len = len(s)
key_len = len(key)
circle = s_len // key_len
for i in range(0, circle - 1):
    key = key + temp
s_list = list(s)
key_list = list(key)
for i in range(s_len):
    s_list[i] = ord(s_list[i])
    key_list[i] = ord(key_list[i])
    s_list[i] -= key_list[i]
    if s_list[i] < 0:
        s_list[i] += 26
    s_list[i] = chr(s_list[i] + 97)
# print(s_list)
decoder_s = ''
decoder_s = decoder_s.join(s_list)
print(decoder_s)