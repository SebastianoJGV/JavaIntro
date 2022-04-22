inp = input('enter num')
primes=[]
prime=False
i = 1
while i < int(inp):
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
        else:
            prime=True
    if prime:
        primes.append(i)
    i+=1
print(primes)
