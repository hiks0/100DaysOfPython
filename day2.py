# a=input("enter number")
# sum=0

# for i in range(len(a)):
#     sum=sum+int(a[i])
    

# print(sum)


# BILL CALCULATOR

a=float(input("Enter the amount"))
b=float(input("Enter tip amount in percentage"))
c=int(input("Enter number of members"))

sum=a+(a*(b/100))
pay=sum/c
print(f"Each person should pay {round(pay,2)}")