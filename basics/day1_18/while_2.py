# while循环的嵌套

# 嵌套循环案例：打印九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        #j*i=
        print(f"{j}*{i}={j*i}\t",end='') #\t制表符对齐，end=''不换行
        j=j+1
    i=i+1
    print() # 输出一个空内容，起到换行的作用


