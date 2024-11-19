from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
def crt(remainders, moduli):
    M = 1
    for mod in moduli:
        M *= mod
    #计算解x
    x = 0
    for (r, m) in zip(remainders, moduli):
        Mi = M // m
        Mi_inv = pow(Mi, -1, m)#计算Mi的逆元满足(Mi*Mi_inv)%m==1
        x += r * Mi * Mi_inv
    x = x % M#确保结果在[0, M)范围内
    return x, M
def rsa_encrypt(plaintext, e, N):
    ciphertext = pow(plaintext, e, N)#加密plaintext^e mod N
    return ciphertext
def rsa_crt_decrypt(ciphertext, p, q, d):
    # 计算私钥指数模(p-1)和模(q-1)
    dp = d % (p - 1)#私钥指数模 (p-1)
    dq = d % (q - 1)#私钥指数模 (q-1)
    #计算q模p的逆元
    q_inv = pow(q, -1, p)#q在模p下的逆元
    # 分别计算模 p 和模 q 的解
    m1 = pow(ciphertext, dp, p)#c^dp mod p
    m2 = pow(ciphertext, dq, q)#c^dq mod q
    #使用CRT组合结果
    h = (q_inv * (m1 - m2)) % p
    plaintext = (m2 + h * q) % (p * q)
    return plaintext
p = 10610173916367595998556206350665388968860027580003556965556066866029960110017927920144468799855477197348343112099616277472177543644623723834829766436099487
q = 9381879564064062982811321724706432111354852219742374521641981276846166625247616480455790701307284725355323219666588927864961810043676907638939520065262141
e = 65537
d = 69375217053132246433923872050461071707905061219620690812401940103809152343279388196190463256226264471413333977402302080375135837904965916163905925900051233856231956948683629052895522893048343091769614919615717748196724161283693713337127737153907116725226278450928953265802003539187542056238134638877432144473
text=input("输入要加密的")
text = text.encode('utf-8')#需要转换成字节,以便接下来转换成long
text=bytes_to_long(text)
print(text)
encrypted_text=rsa_encrypt(text,e,p*q)
decrypted_message = rsa_crt_decrypt(encrypted_text, p, q, d)
print(decrypted_message)
plain_text=long_to_bytes(decrypted_message)
plain_text=plain_text.decode('utf-8')
print("解密后的明文:",plain_text)
