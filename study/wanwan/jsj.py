class jsj:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def jiaf(self):
        return self.a+self.b
    def jianfa(self):
        return self.a-self.b
    def chef(self):
        return  self.a*self.b
    def chuf(self):
        return self.a/self.b
def pd_nuber(nmber1):
    while 1==1:
        nmber2=nmber1.isdigit()
        if nmber2:
            nmber3=int(nmber1)
            return nmber3
        else:
            nmber1=input('输入有误请重新输入:')
if __name__=='__main__':
    one=pd_nuber(input('请输入数字:'))
select =input('请输入算法:')
if __name__=='__main__':
    two=pd_nuber(input('请输入数字:'))
sili=jsj(one,two)
if select == '-':
    print(sili.jianfa())
elif select == '+':
    print(sili.jiaf())
elif select =='/':
    print(sili.chuf())
elif select =='*':
    print(sili.chef())
else:
    print('抱歉目前只支持简单加减乘除')