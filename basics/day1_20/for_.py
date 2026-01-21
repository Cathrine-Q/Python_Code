# # 遍历字符串
# name="peimo"
# for i in name:
#     # 将name的内容挨个取出赋予i，就可以在循环体内对i进行处理
#     print(i)
#

# name="what are you doing"
# count=0
# for i in name:
#     if i == 'a':
#         count += 1
# print(f"被统计的字符串中有{count}个a")

# for x in range(10):
#     print(x)
#
# for y in range(5,11):
#     print(y)
#
# for z in range(10,101,15):
#     print(z)

# 练习案例：有几个偶数

# num=50
# count=0
# for i in range(1,num+1):
#     if i%2==0:
#         count=count+1
# print(count)

# for循环的嵌套案例：打印九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
