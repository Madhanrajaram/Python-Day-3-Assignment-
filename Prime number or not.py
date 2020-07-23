p =eval(input("Enter the number:"))
print(p)
if(p==1 or (p%2!=0 and p%3!=0)):
 print(f"{p} is a prime number")
else:
 print(f"{p} is not a prime number")