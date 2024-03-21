a=input("请输入0到10的数字")
s=list(a)
sum=0
for i in range(0,len(s),1):
    t=int(s[i])
    sum=sum+t
print(sum)