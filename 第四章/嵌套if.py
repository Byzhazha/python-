while(True):
    answer=input("您是会员吗？")
    if answer=="是":
        money=float(input("请输入您的花销："))
        if money >=200:
            print("金额为",money*0.8)
        elif 100<=money<200:
            print("金额为：",money*0.9)
    else:
        money=float(input("请输入您的花销："))
        if money>=200:
            print("金额为：",money*0.95)
        else :
            print("不打折",money)
