# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2023/6/6 15:21
# @Function: ElGamal Digital Signature using SHA-256

"""
Key Generation
1. Select a large random prime p and a generator α of Z∗p.
2. Generate a random integer x such that 1≤x≤p−2. 
3. Compute y = α**x mod p.
4. A’s public key is (p, α, y).
5. A’s private key is x.

Signature Generation
A generates a signature for a message m (0 ≤ m < p−1) as follows:
1. Generate a random integer k such that 1≤k≤p−2 and gcd(k,p−1)=1.
2. Compute r = α**k mod p.
3. Compute k**−1 mod (p − 1).
4. Compute s=k**−1(m−xr)mod(p−1). 
5. A’s signature for m is the pair (r, s),

Signature Verification
A signature (r, s) produced by A can be verified as follows:
1. Verify that 1 ≤ r ≤ (p−1); if not return False.
2. Compute v1 = (y**r)(r**s) mod p. 
3. Compute v2 = α**m mod p. 
4. Return v1 = v2.

"""
import Crypto.Util.number as num
from Crypto.Hash import SHA256
import random
import pair


def egKey(s):
    p, a, execution_time = pair.pair(s)
    x = random.randint(1, p - 2)
    y = pow(a, x, p)
    return p, a, x, y, execution_time


""" 
Signature Generation 
"""


def egGen(p, a, x, m):
    h = SHA256.new()
    h.update(m)
    m = int(h.hexdigest(), 35)

    while 1:
        k = random.randint(1, p - 2)
        if num.GCD(k, p - 1) == 1:
            break
    r = pow(a, k, p)
    t = num.inverse(k, p - 1)
    s = t * (m - x * r) % (p - 1)
    return r, s


""" 
Signature Verification 
"""


def egVer(p, a, y, r, s, m):
    h = SHA256.new()
    h.update(m)
    m = int(h.hexdigest(), 35)

    if r < 1 or r > p - 1:
        return False
    v1 = pow(y, r, p) % p * pow(r, s, p) % p
    v2 = pow(a, m, p)
    return v1 == v2


if __name__ == "__main__":
    message = input("enter your message: ")
    binary_message = message.encode('utf-8')

    # 将字节字符串转换为十六进制 再转换为整数存入文件中
    hex_message = binary_message.hex()
    int_message = int(hex_message, 16)
    with open("plain.txt", "w") as out:
        out.write(str(int_message))
    out.close()
    print("plain: ", int_message)
    print("stored into plain.txt\n")

    print("start initialization: \n")

    prime, alpha, private, public, time = egKey(1024)
    print("prime: %s\n"
          "alpha: %s\n"
          "private key: %s\n"
          "public key: %s\n" % (prime, alpha, private, public))

    print("Initialization execution time: ", time, "seconds\n")

    with open("prime.txt", "w") as p:
        p.write(str(prime))
    with open("alpha.txt", "w") as p:
        p.write(str(alpha))
    with open("private.txt", "w") as p:
        p.write(str(private))
    with open("public.txt", "w") as p:
        p.write(str(public))

    print("start verification: \n")
    rr, ss = egGen(prime, alpha, private, binary_message)
    print("(r, s) = (%s, %s)\n" % (rr, ss))
    isValid = egVer(prime, alpha, public, rr, ss, binary_message)
    print("Valid Signature: ", isValid)
