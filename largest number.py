# if,,elif,,else statement
# create a program for grade input wit the following
#    80-100 -A
#   60-79 -B
#    50-69  -C
#    30-49  -D
#    Below 30-  fail
#    negative and above 100- invalid input





num=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
num4=int(input("enter the fouth number"))

if num > num2 and num > num3:
    print(num,"is greater")
elif num2 > num and num2 > num3:
    print(num2,"is greater")
elif num3 > num and  num3 > num2:
    print(num3,"is greater")
elif num4 > num and num4 > num3:
    print(num4,"is greate")
else:
    print("invalid error")