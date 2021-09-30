from Crypto.PublicKey import RSA
from Crypto.Util.number import *
 
def crt(list_a, list_m):
    for i in range(len(list_m)):
        for j in range(len(list_m)):
            if GCD(list_m[i], list_m[j])!= 1 and i!=j:
                return None
    M = 1
    for i in list_m:
        M *= i
    list_b = [M/i for i in list_m]
    assert len(list_b) == len(list_m)
    list_b_inv = [inverse(list_b[i], list_m[i]) for i in range(len(list_m))]
    x = 0
    for i in range(len(list_m)):
        x += list_a[i]*list_b[i]*list_b_inv[i]
    return x % M
 
key1 = RSA.importKey(open("publickey1.pem").read())
key2 = RSA.importKey(open("publickey2.pem").read())
N1 = key1.n
e1 = key1.e
N2 = key2.n
e2 = key2.e
 
ct1 = bytes_to_long(open("ciphertext1.txt").read())
ct2 = bytes_to_long(open("ciphertext2.txt").read())
 
q1 = 3807106592404975601125033090180503344264174569255897409284423052897092445417674962362221548320775037781978870632221456368716628390293018864172214774714465531462065303179649214122810035176785416262624632995978331814185099550531145861149188438984893130980572838590794755709091002422200644150512364254454557260789
assert N1 % q1 == 0
p1 = N1 / q1
 
q2 = 2751296681586435626720222057380271100763911689072786354291138095461126286215853115732617512578076591584325152559069002543980487680247274388725342124525719292925128397536955722536120578433729304047954769670529111876899791612062118642496846657307745240072073877747762856779534078553583788593091249350529237188097
assert N2 % q2 == 0
p2 = N2 / q2
 
assert GCD(e1, (p1-1)) == 1
assert GCD(e2, (p2-1)) == 1
 
d1 = inverse(e1, (p1-1))
d2 = inverse(e2, (p2-1))
print "d1: ", d1
print "d2: ", d2
a1 = pow(ct1, d1, p1)
a2 = pow(ct2, d2, p2)
print long_to_bytes(crt([a1, a2], [p1, p2]))
