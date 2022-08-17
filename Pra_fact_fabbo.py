def fabonacci( n):
    print('fabonacci:')
    if n==0 :
        print(0)
    elif n<2:
        print(0)
        print(1)
    else :
        print(0)
        print(1)
        a = 0
        b=1
        c=1
        while c<n :
            print(c)
            a=b
            b=c
            c=a+b
def factorial(n):
    print('Factorial : ')
    c=1
    for i in range(1,n+1,1):
        c+=c*i
    return c

print("Enter the Number :")
n = int(input())
if(n<10):
    fabonacci(n)
else:
    print(factorial(n))


        
