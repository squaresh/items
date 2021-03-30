aa={'g': 22, 'b': 33}
bb={'g': 22, 'b': 33}
g=[]
g.append(aa)
g.append(bb)
print(g)
qq=[1,2,3,4,5]
ww=[5,6,7,8,9]
cc=[]
cc.append(qq)
cc.extend(ww)
print(cc)
import pandas as pd

data = [{'g': 22, 'b': 33}, {'g': 22, 'b': 33}]
df = pd.DataFrame(data)

print(df)