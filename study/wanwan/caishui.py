import random
def nmber(ss):
    try:
        use_nm = int(ss)
        return use_nm
    except:
        print('输入有误请重新输入')
        ss = input('请输入你猜测的数字:')
        bb = nmber(ss)
        return bb
print('**'*10)
print('欢迎来到猜数游戏')
print('**'*10)
use=input('请输入你的用户名：')
k=random.randint(1,100)
a=int(k)
print('你现在还有{}颗币'.format(a))
print('温馨提示猜错一次扣除3个币')
if __name__ == '__main__':
    ss=input('请输入你猜测的数字:')
    use_nm=nmber(ss)
sj_nmber=int(random.randint(1,100))
while 1==1:
    if sj_nmber > use_nm:
        a -= 3
        if a <= 0:
            break
        if __name__ == '__main__':
            ss = input('你猜数的数字太小了请重新输入:')
            use_nm = nmber(ss)
        print('你现在还有{}个币'.format(a))
    elif sj_nmber < use_nm:
        a -= 3
        if a <= 0:
            break
        if __name__ == '__main__':
            ss = input('你猜数的数字太大了请重新输入:')
            use_nm = nmber(ss)
        print('你现在还有{}个币'.format(a))
    else:
        print('恭喜你猜对了')
        break