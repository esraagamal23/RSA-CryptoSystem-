import math
from random import randint
from numpy import sqrt 
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)
#######################################
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)



def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n # we don’t want −ve integers
    return b
##################################
def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod

def ConvertToInt( message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res
#####################################

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


#question1
def Encrypt(m, n, e):
    m=ConvertToInt(m) 
    c=PowMod(m,e,n) 
    return c
#############################

def Decrypt(c, p, q, e):
    euler=(p-1)*(q-1)
    d=InvertModulo(e,euler) 
    n=p*q
    m=PowMod(c,d,n) 
    m=ConvertToStr(m)
    return m
chiper_message=Encrypt("attack", 1000000007*1000000009,23917)
print(Decrypt(chiper_message, 1000000007,1000000009,23917))
#question2
def DecipherSimple(c, n, e, potential_messages):
        decipheredtext=''
        for i in potential_messages:
            
            if  Encrypt(i,n,e)==c:
                decipheredtext=i
        return decipheredtext
modulo = 101
exponent = 12  
ciphertext = Encrypt("attack", modulo, exponent)    
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))   
# get a missing prime number
def get_prime_number(i,j,n):
    
    for i in range(i,j):
        if(n%i==0):
            return i
    return 0     
##question3
def DecipherSmallPrime(c, n, e):
    p=get_prime_number(2,1000000,n) 
    decipheredtext=Decrypt(c,p,n//p,e)
    return decipheredtext
modulo = 101 *18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(DecipherSmallPrime(ciphertext, modulo, exponent))
#question4
def DecipherSmallDiff(c, n, e):
    p=get_prime_number(int(sqrt(n)-5000),int(sqrt(n)),n)
    decipheredtext=Decrypt(c,p,n//p,e)
    return decipheredtext

p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(message)
#question5
def DecipherCommonDivisor(c1, n1, e1, c2, n2, e2):
        p=GCD(n1,n2)
        first_decipheredtext= Decrypt(c1,p,n1//p,e1) 
        second_decipheredtext=Decrypt(c2,p,n2//p,e2)
        return first_decipheredtext, second_decipheredtext

p = 101
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
q2 = 1000000007
first_modulo = p * q1
second_modulo = p * q2
first_exponent = 239
second_exponent = 17
first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
print(DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent))

#question6
def DecipherHastad(c1, n1, c2, n2, e):
    N1=(n1*n2)//n1
    N2=(n1*n2)//n2

    x1=InvertModulo(N1,n1)  
    x2=InvertModulo(N2,n2)
    c_square=(c1*N1*x1+c2*N2*x2)%(n1*n2)
  
    c=int(round(sqrt(float(c_square))))
    broadcast_message=ConvertToStr(c) 
   # m1= int(round(sqrt(float(c1))))
    #m2= int(round(sqrt(float(c2))))
    #if(m1==m2):
     #   broadcast_message=ConvertToStr(m1) 
    return broadcast_message

p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
e = 2
ciphertext1 = Encrypt("attack", n1, e)
ciphertext2 = Encrypt("attack", n2, e)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2, e)
print(message)