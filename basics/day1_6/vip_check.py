# if elif else语句的使用

# print("欢迎来到梦乐园。")
# height = int(input("请输入身高（cm）："))
# vip_level = int(input("请输入vip等级（1-5）："))
# day = int(input("今天是几号？"))
# if height <120:
#     print("身高小于120cm，可以免费。")
# elif  vip_level >=3:
#     print("vip等级大于3，可以免费游玩。")
# elif day == 1:
#     print("今天是1号，可以免费游玩。")
# else:
#     print("不好意思，条件都不满足，需要买票10元。")

# 简化版

print("欢迎来到梦乐园。")
if int(input("请输入身高（cm）：")) <120:
    print("身高小于120cm，可以免费。")
elif  int(input("请输入vip等级（1-5）：")) >=3:
    print("vip等级大于3，可以免费游玩。")
elif int(input("今天是几号？")) == 1:
    print("今天是1号，可以免费游玩。")
else:
    print("不好意思，条件都不满足，需要买票10元。")
