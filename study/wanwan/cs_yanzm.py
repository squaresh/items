import random
s='qwertyuiopQWERTYUIOP123456789'
# print(len(s)) #求字符串的长度
# random.randint(0,30)
def yanz():
    b='b'
    for i in range(4): #从0开始不包括4
        a=random.randint(0,len(s)-1) #从0开始包含最后一位
        b=b+s[a] #赋值
    return b
b=yanz()
print(b[1:5])
use_input=input('请输入验证码:')

while 1==1:

    if use_input.lower == b[1:5].lower:
        print('进入游戏')
        break
    else:
        b=yanz()
        print(b[1:5])
        use_input=input('输入验证码有误请重新输入:')
