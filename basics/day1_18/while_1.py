# i=0
# while i<10:
#     print("好喜欢你~知不知道~")
#     i+=1

# sum=0
# i=1
# while i<=100:
#     sum+=i
#     i+=1
# print(f"1到100累加的结果是：{sum}")


# import random
# num = random.randint(1,100)
# i=1
# guess_=int(input("请输入要猜的数字："))
# while guess_ !=num:
#     if guess_>num:
#         print("猜大了。")
#     else:
#         print("猜小了。")
#     i+=1
#     guess_ = int(input("请输入要猜的数字："))
# print(f"恭喜你猜对啦！\n你一共猜了{i}次，正确答案就是：{guess_}")


import random
num = random.randint(1,100)
count=0
flag=True
while flag:
    guess_num = int(input("请输入要猜的数字："))
    count+=1
    if guess_num == num:
        print("恭喜你，猜中啦！")
        flag=False
    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")
print("你一共猜了%d次" % count)
