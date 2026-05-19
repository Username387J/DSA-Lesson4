#a recursive function is a function that calls itself in its own function definition
def factorial(n):
    #base case or stop case
    if n==1 or n==0:
        return 1
    #recursive case
    else:
        return n*factorial(n-1)
n=int(input("Enter a number "))
ans=factorial(n)
print("The factorial of {} is {}".format(n,ans))
