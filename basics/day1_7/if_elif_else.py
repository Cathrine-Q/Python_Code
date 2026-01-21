# 实战案例——猜数字
# import random
# num = random.randint(1,10)
# num1=int(input("请输入你第一次猜的数字："))
# if num1!=num:
#     print("猜错了哦。")
#     if num1>num:
#         print("提示：猜大了。")
#     else:
#         print("提示：猜小了。")
# # 第一次未猜中
#     num2=int(input("请输入你第二次猜的数字："))
#     if num2 != num:
#         print("猜错了哦。")
#         if num2 > num:
#             print("提示：猜大了。")
#         else:
#             print("提示：猜小了。")
#     else:
#         print("恭喜你，猜对啦！")
# # 第二次未猜中
#     num3=int(input("请输入你第三次猜的数字："))
#     if num3!=num:
#         if num3>num:
#             print("提示：猜大了。")
#         else:
#             print("提示：猜小了。")
#     else:
#         print("恭喜你，终于猜对啦！")
# else:
#     print("恭喜你，第一次就猜对了呢！")

import random
num = random.randint(1,10)
num1 = int(input("请输入第一次猜的数字："))
if num1 ==num: #注意是==而不是=
    print("恭喜你，第一次就猜对啦！")
else:
    print("猜错了。")
    if num1 > num:
        print("提示：猜大了。")
    else:
        print("提示：猜小了。")
# 第二次猜
    num2 =int(input("请输入第二次猜的数字："))
    if num2 == num:
        print("恭喜你，猜对啦！")
    else:
        print("又猜错了。")
        if num2 > num:
            print("提示：猜大了。")
        else:
            print("提示：猜小了。")
# 第三次猜
        num3 = int(input("请输入第三次猜的数字："))
        if num3 == num:
            print("恭喜你，终于猜对啦！")
        else:
            print("三次机会用完了，很遗憾，你没有猜中。")
            print(f"正确答案是：{num}")