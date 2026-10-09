#RSA algorithm:
import random
import math
def check_prime(Num):
    for i in range(2,Num):
        if Num%i==0:
            print("Not a prime number")
            return False
    else:
        isPrime=True
        print("It's a prime number")
        return True

primelist=[]
for i in range(1,10000):
    if check_prime(i)==True:
        primelist.append(i)
        
print(primelist)
p=primelist[random.randint(0,len(primelist)-1)]
q=primelist[random.randint(0,len(primelist)-1)]

if p!=q:
    #Creates N, using the products of P and Q.
    n=p*q
    print("n=",n)
    t=(p-1)*(q-1)
    for i in range(2,t):
        if math.gcd(i,t)==1:
            e=i
            break
    print("e=",e)
    j=0
    while (e*j)%t!=1:
        j+=1
    print("d=",j)
    message=int(input("Enter the message to be encrypted: "))
    c=(message**e)%n
    print("Encrypted message:",c)
    m=(c**j)%n
    print("Decrypted message:",m)
else:
    print("p and q should not be equal, please rerun the program")
