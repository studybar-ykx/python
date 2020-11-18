#coding=gbk
#Author :  xddy1008@gmail.com
#Type of crypting being done
ENCRYPT =    0x00
DECRYPT =    0x01

# Permutation and translation tables for DES
# 密钥置换
__pc1 = [56, 48, 40, 32, 24, 16,  8,
        0, 57, 49, 41, 33, 25, 17,
        9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36, 28,
        20, 12,  4, 27, 19, 11,  3
            ]

# number left rotations of pc1
# 每轮循环左移位数
__left_rotations = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
    ]

# permuted choice key (table 2)
# 压缩置换
__pc2 = [
    13, 16, 10, 23,  0,  4,
     2, 27, 14,  5, 20,  9,
    22, 18, 11,  3, 25,  7,
    15,  6, 26, 19, 12,  1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
    ]

# initial permutation IP
# 初始置换IP
__ip = [57, 49, 41, 33, 25, 17, 9,  1,
        59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8,  0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
    ]

# Expansion table for turning 32 bit blocks into 48 bits
# 扩展变换
__expansion_table = [
    31,  0,  1,  2,  3,  4,
     3,  4,  5,  6,  7,  8,
     7,  8,  9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31,  0
        ]

# The (in)famous S-boxes
# S 盒
__sbox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]


# 32-bit permutation function P used on the output of the S-boxes
# P-盒置换
__p = [
    15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17, 30, 9, 1, 7,
    23,13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10,
    3, 24
    ]

# final permutation IP^-1
# 末尾置换IP^-1
__fp = [
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25,
    32,  0, 40,  8, 48, 16, 56, 24
    ]
def __String_to_BitList(data):
    """Turn the string data,into a list of bits"""
    data = [ord(c) for c in data] #转换成十进制数
    sl = len(data)*8
    pos = 0
    result = [0]*sl #共有 sl 位
    for ch in data:
        i = 7
        while i>=0:
            if ch & (1<<i) != 0:
                result[pos] = 1
            else :
                result[pos] = 0
            pos += 1
            i -= 1
    return result
def __BitList_to_String(data):
    """Turn the list of bits(data) into a string"""
    result = []
    pos = 0
    c = 0
    while pos < len(data):
        c += data[pos] << (7-( pos % 8)) #转换成十进制数
        if ( pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1
    return ''.join([chr(c) for c in result ])
def __BitList_to_HexString(data):
    result = []
    HEX = '0123456789ABCDEF'
    pos = 0
    c = 0
    while pos < len(data):
        c += data[pos] << (3 - (pos % 4))
        if( pos % 4 ==3):
            c = HEX[c]
            result.append(c)
            c = 0
        pos +=1
    return ''.join([x for x in result ])


def String_to_HexString(data):
    return __BitList_to_HexString(__String_to_BitList(data))


def BitString_to_String(data):
    bitlist = [ord(x)-48 for x in data]
    return __BitList_to_String(bitlist)

def String_to_BitString(data):
    bitlist = __String_to_BitList(data)
    return ''.join([chr(x+48) for x in bitlist])

def HexString_to_String(data):
    HEX = '0123456789ABCDEF'
    HexList = list(HEX)
    value = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    h_v = dict(zip(HexList,value))

    data = [h_v[x] for x in data ]

    sl = len(data)*8
    pos = 0
    result = [0]*sl #共有 sl 位
    for ch in data:
        i = 7
        while i>=0:
            if ch & (1<<i) != 0:
                result[pos] = 1
            else :
                result[pos] = 0

            pos += 1
            i -= 1
    ret = []
    i = 4
    while i <len(result):
        ret.append(result[i])
        ret.append(result[i+1])
        ret.append(result[i+2])
        ret.append(result[i+3])
        i += 4

    return  __BitList_to_String(ret)


def __permutata(table,block):
    """用指定的table置换block"""
    return list(map(lambda x: block[x],table))


def __create_sub_keys(K1,K2):
    """按照要求生成子密钥
        返回K[1]-K[16]
        去两个各为64比特的密钥K1,K2,在DES的第1到5轮使用K1密钥产生的子密钥，在第6到11
        轮使用K2密钥产生的子密钥，在第12到16轮使用K1密钥产生余下的子密钥。
        
    """
    subKey = []
    key1 = __permutata (__pc1,__String_to_BitList(K1)) #转换成56位
    key2 = __permutata (__pc1,__String_to_BitList(K2)) #转换成56位

    # 由K1 生成1到5轮的子密钥
    # 将key1分割左右各28位
    L1 = key1[:28]
    R1 = key1[28:]
    for i in range(5):
        j = 0
        # 轮循环
        while j <  __left_rotations[i]:
            L1.append(L1[0])
            del L1[0]

            R1.append(R1[0])
            del R1[0]
            j+=1
        #压缩置换生成子密钥
        subKey.append(__permutata(__pc2,L1+R1))

    # 由K2生成第6到11轮子密钥
    L2 = key2[:28]
    R2 = key2[28:]
    for i in range(5,11):
        j = 0
        while j < __left_rotations[i]:
            L2.append(L2[0])
            del L2[0]
            R2.append(R2[0])
            del R2[0]
            j+=1
        subKey.append(__permutata(__pc2, L2+R2))

    #由K1继续生成余下的子密钥
    for i in range(11,16):
        j = 0
        while j < __left_rotations[i]:
            L1.append(L1[0])
            del L1[0]
            R1.append(R1[0])
            del R1[0]
            j+=1
        subKey.append(__permutata(__pc2, L1+R1))

    return subKey
def __create_keys(K1):
    subKey = []
    key1 = __permutata (__pc1,__String_to_BitList(K1)) #转换成56位

    # 由K1 生成1到5轮的子密钥
    # 将key1分割左右各28位
    L1 = key1[:28]
    R1 = key1[28:]
    for i in range(16):
        j = 0
        # 轮循环
        while j <  __left_rotations[i]:
            L1.append(L1[0])
            del L1[0]

            R1.append(R1[0])
            del R1[0]
            j+=1
        #压缩置换生成子密钥
        subKey.append(__permutata(__pc2,L1+R1))
    return subKey


def __des_crypt(block,crypt_type,K1,K2):
    """加解密函数，block 是二进制块 64位  由crypt_type 指定"""
    # 初始IP置换
    block = __permutata(__ip, block)
    #分块
    L = block[:32]
    R = block[32:]
    if crypt_type == ENCRYPT:
        iteration = 0
        iteration_adjustment = 1
    else :
        iteration = 15
        iteration_adjustment = -1
    # 异或函数
    xorfun = lambda x,y:x^y
    # 生成子密钥
    if K2=='':
        Kn = __create_keys(K1)
        print('K2 is null')
    else:
       Kn = __create_sub_keys(K1, K2)
    # 进行16轮加密

    for i in range(16):
        tempR = R[:]  # Make a copy

        # 扩展置换
        R = __permutata(__expansion_table, R)

        # 与子密钥进行异或
        R = list(map(xorfun,R,Kn[iteration]))

        # 将R分割成 6 * 8
        B = [R[:6], R[6:12], R[12:18], R[18:24],
             R[24:30], R[30:36], R[36:42],R[42:]]

        # S盒代替 B[1] 到 B[8] 最终生成32位的Bn
        pos = 0
        Bn = [0]*32
        for j in range(8):
            m = (B[j][0] << 1) + B[j][5]  # 计算行
            n = (B[j][1]<<3) + (B[j][2]<<2) + (B[j][3]<<1) + (B[j][4])  # 计算列
            # 得到S-盒 j的置换值
            v = __sbox[j][(m<<4) + n] # m*16 + n
            #转换成二进制
            Bn[pos] = (v & 8) >> 3
            Bn[pos + 1] = (v & 4) >>2
            Bn[pos + 2] = (v & 2)>>1
            Bn[pos + 3] = v & 1
            pos += 4

        R = __permutata(__p, Bn)      # P - 盒代替
        R = list(map(xorfun,R,L))    # 与 L 异或
        L = tempR
        iteration += iteration_adjustment

    # 最后IP 置换
    return __permutata(__fp, R+L)

def des_Crypt(data,crypt_type,K1,K2):
    """ 加解密一段数据  ,默认采用PaddingPKCS5 填充方式"""
    if not data:
        return ''
    # 检查数据是否为64位的整数倍
    if len(data) % 8 !=0:
        if crypt_type == DECRYPT:
            raise ValueError("Invalid data length,data must be a "+
                " mutiple of 8 bytes \n" )
        else :                          #如果需要填充block使成为8字节的整数倍
            pad_len = 8 - (len(data) % 8)   # 计算需要填充的字节数pad_len
            data +=pad_len * chr(pad_len)   # 填充pad_len 的 chr(pad+len)

    result = []
    i = 0
    while i < len(data):
        block = __String_to_BitList(data[i:i+8])  # 8字节一块
        processed_block = __des_crypt(block, crypt_type, K1, K2)
        result.append(__BitList_to_String(processed_block))
        i +=8

    return ''.join(result)


def encrypt(data,K1,K2):
    """ 加密一段数据data 使用默认的填充方式 ：PKCS5 
    K1,K2 必须是8字节的"""

    if len(K1) != 8:
        raise ValueError("K1 不是 64 位的密钥!")
    if K2!='' and len(K2)!= 8:
        raise ValueError("K2 不是 64 位的密钥!")
    return des_Crypt(data, ENCRYPT, K1, K2)

def decrypt(data,K1,K2):
    if len(K1) != 8:
        raise ValueError("K1 不是 64 位的密钥!")
    if K2!='' and len(K2)!= 8:
        raise ValueError("K2 不是 64 位的密钥!")
    return des_Crypt(data, DECRYPT, K1, K2)




def test(data,K1,K2):
    result = []
    datal = __String_to_BitList(data)
    bitK1=String_to_BitString(K1)
    bit1=__String_to_BitList(K1)
    bitK2=String_to_BitString(K2)
    bit2 =__String_to_BitList(K2)

    result.append(u'当前明文为: '+data+'\r\n')
    result.append('K1: '+bitK1+'\r\n')
    result.append('K2: '+bitK2+'\r\n')

    result.append(u'修改明文从第1位到%d位,加密结果为：\r\n' % len(datal))
    ret = encrypt(data,K1,K2)
    last= String_to_BitString(ret)
    for i in range(1,len(datal)):
        count = 0
        datal[i]=((datal[i]+1)%2)
        dataw = __BitList_to_String(datal)
        ret = encrypt(dataw,K1,K2)
        retbit= String_to_BitString(ret)
        y = 0
        for x in retbit:
            if x!=last[y]:
                count +=1
            y +=1
        last = retbit
        ret = String_to_HexString(ret)
        result.append(ret+'--'+str(count)+'\r\n')
    result.append(u'依次修改K1的第1到64位，加密结果为：\r\n')
    for j in range(1,64):
        count = 0
        bit1[j] = ((bit1[j]+1)%2)
        key1 = __BitList_to_String(bit1)
        ret = encrypt(data,key1,K2)
        retbit= String_to_BitString(ret)
        y = 0
        for x in retbit:
            if x!=last[y]:
                count +=1
            y +=1
        last = retbit
        ret = String_to_HexString(ret)
        result.append(ret+'--'+str(count)+'\r\n')
    return result

print(test('hello','f3eda6dcf8b79dd65be0db8b1e7ba551','f3eda6dcf8b79dd65be0db8b1e7ba551'))