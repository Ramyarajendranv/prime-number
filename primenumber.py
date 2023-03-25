#prime number
'''n=int(input("Enter the number:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print("prime number")
else:
    print("not prime number")'''

#prime number list
n=int(input("Enter the number:"))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
           break
    else:
        print(i)

