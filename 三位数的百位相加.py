while 1:
    shu=input("请输入三位数:")
    shu=int(shu)
    if(shu>=100 and shu<=999 ):
        shug=shu%10
        shus=int(shu/10%10)
        shub=int(shu/100)
        print('三位数百位十位个位相加='+str(shug+shus+shub))
    else:
        print("错误")  