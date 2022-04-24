
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def isDivisible(divisor, num):
    if num%divisor==0:
        return True
    else:
        return False

def factorsOf(num):
    factors = []
    for i in range(1,num):
        if isDivisible(i,num):
            factors.append(i)
    return factors

def primeFactorsOf(num):
    factors = []
    for i in range(1,num):
        if isPrime(i) and isDivisible(i,num):
            factors.append(i)
    return factors

def primesUpTo(num):
    primes = []
    for i in range(1,num):
        if isPrime(i):
            primes.append(i)
    return primes

def gCF(num1, num2):
    factors1 = factorsOf(num1)
    factors2 = factorsOf(num2)
    commonFactors = []
    for i in factors1:
        if i in factors2:
            commonFactors.append(i)
    return commonFactors

def lCM(num1, num2):
    factors1 = factorsOf(num1)
    factors2 = factorsOf(num2)
    commonFactors = []
    for i in factors1:
        if i in factors2:
            commonFactors.append(i)
    return int(commonFactors[-1])

print('Welcome to the number suite')
inp=input("1. Check to see if an integer is a Prime number."
+ "\n" + "2. Check to see if one integer is divisible by another."
+ "\n" + "3. List all the factors of an integer."
+ "\n" + "4. List all the Prime factors of an integer."
+ "\n" + "5. List Prime numbers up to a given point."
+ "\n" + "6. Find the GCF of a set of integers."
+ "\n" + "7. Find the LCM of a set of integers."
+ "\n" + "0. Exit program.")

while(int(inp)>0):
    if inp==1:
        inp=input("Enter a number to check if it is a prime number: ")
        if isPrime(int(inp)):
            print(inp + " is a prime number.")
        else:
            print(inp + " is not a prime number.")
    elif inp==2:
        inp1=input("Enter the first number: ")
        inp2=input("Enter the second number: ")
        if isDivisible(int(inp1),int(inp2)):
            print(inp1 + " is divisible by " + inp2)
        else:
            print(inp1 + " is not divisible by " + inp2)
    elif inp==3:
        inp=input("Enter a number to find its factors: ")
        print(factorsOf(int(inp)))
    elif inp==4: 
        inp=input("Enter a number to find its prime factors: ")
        print(primeFactorsOf(int(inp)))
    elif inp==5:
        inp=input("Enter a number to find all primes up to it: ")
        print(primesUpTo(int(inp)))
    elif inp==6:
        inp1=input("Enter the first number: ")
        inp2=input("Enter the second number: ")
        print(gCF(int(inp1),int(inp2)))
    elif inp==7:
        inp1=input("Enter the first number: ")
        inp2=input("Enter the second number: ")
        print(lCM(int(inp1),int(inp2)))