# 练习案例：发工资


import random
# 员工编号1-10
employee = 1
# 账户余额
salary_sum=10000
for employee in range(1,21):
    i = random.randint(1, 10) # 员工绩效随机生成（1-10）
    if salary_sum>0:
        if i>=5:
            salary_sum -= 1000
            print(f"员工{employee}绩效分为{i}，发工资1000元，账户余额{salary_sum}元。")
        else:
            print(f"员工{employee}绩效分为{i},低于5，不发工资。")
            continue
    else:
        print("工资发完了，下个月领取吧。")
        break
