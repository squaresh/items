from pyquery import PyQuery as pq  ##导入这个模块

with open("D:/pycharm/projects/learn/study/txt/data.html", "r") as f: ##打开

    contents = f.read()  ##读

    doc = pq(contents)  ##使用函数

    text = doc("th").text()  ###要提取的标签以txt提取
    print(text)
    text = doc("tr").html()  ##以html提取
    print("\n".join(text.split()))