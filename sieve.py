def sieve(x):
    prime = [True for i in range(x+1)]
    prime[0]=False
    prime[1]=False
    p=2
    count=0
    while ((p*p)<=x):
        if (prime[p]==True):
            for i in range(p*2,x+1,p):
                prime[i]=False
        p+=1
    for p in range(x+1):
        if prime[p]==True:
            print(p)
            count+=1
    print('There are ',count,' prime numbers in this range.')
x = int(input('Enter an integer greater than 1: '))
sieve(x)