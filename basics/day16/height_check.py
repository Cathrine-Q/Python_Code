# 猜猜心里数字

num = 30

if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你第一次就猜对了！")
elif int(input("猜错了，请输入第二次猜想的数字：")) == num:
    print("恭喜你猜对了!")
elif int(input("猜错了，请输入第三次猜想的数字：")) == num:
    print("恭喜你猜对了!")
else :
    print(f"Sorry,全猜错啦，我想的是{num}.")
