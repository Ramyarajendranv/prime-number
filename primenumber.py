
#prime number list
n=int(input("Enter the number:"))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
           break
    else:
        print(i)

