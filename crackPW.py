"""
Tool for bruteforcing the passwords in j2l Map-Files
"""
from sys import argv
from binascii import crc32
from itertools import combinations_with_replacement as combinations

#Charsets
lower = "abcdefghijklmnopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"

#The pseudo-hash used in the maps
def toHash(string):
    b = bytes(string,"utf-8")
    h = hex(crc32(b))
    return h[4:]

#Cracking the password up to length 11
def crack(bhash,ch=upp):
    i = 1
    while i < 12:
        print("Trying length "+str(i))
        for c in combinations(ch,i):
            cur = "".join(c)
            h = toHash(cur)
            if h==bhash:
                return cur
        i+=1
    return ""

#Reading out bytes from offset s to offset t
#->Used for getting the password in the mapfile
def getRange(file,s=184,t=188):
    x = open(file,"rb")
    pos = 0
    byte = x.read(1)
    out = b""
    while byte!=b"":
        pos+=1
        if s<pos<t:
            #print(str(pos)+": "+str(byte))
            out+=byte#out.append(byte)
        byte = x.read(1)
    x.close()
    out = str(out)[2:-1]
    out = out[2:4]+out[6:8]+out[10:12]
    return out
            
if len(argv)!=3:
    print("---------------------------------")
    print("Jazz2 password cracker for maps")
    print("---------------------------------")
    print("Usage: python crackPW.py FILE charset")
    print("Where Charset can be a combination of")
    print("u - Uppercase letters")
    print("l - Lowercase letters")
    print("n - Numbers")
    print("python crackPW.py FILE uln")
    print("Would use uppercase, lowercase and numeric chars.")
    exit(0)

toCrack = getRange(argv[1])
print("Trying to crack bytesequence")
print(toCrack)

charset = argv[2]
ch = []
if charset.count("u")>=1:
    ch.extend(upp)
if charset.count("l")>=1:
    ch.extend(lower)
if charset.count("n")>=1:
    ch.extend(nums)

ret=crack(toCrack,ch)
if ret!="":
    print("Gotcha!")
    print(ret)
else:
    print("No password found :( Try changing the used charset")
