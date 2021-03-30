def nmber(ss):
    try:
        use_nm=int(ss)
        return use_nm     ##如果调用两次递归循环返回给上一层（记住哪个函数调用它，它就返回给哪个函数）
    except:
        print('输入有误请重新输入')
        ss = input('请输入你猜测的数字:')
        bb=nmber(ss)
        return bb
print(nmber('12k'))
