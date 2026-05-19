#fibonacci- sum of two previous numbers
def fib(n):
    if n==0:
        return 0
    elif n==1 or n ==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter a number "))
ans=fib(n)
print("The fibonacci of {} is {}".format(n,ans))

#printing the fibonacci sequence
for i in range(0,n+1):
    print(fib(i))