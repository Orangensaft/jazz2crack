from sys import argv

if len(argv)!=2:
    print("Usage: python removePW.py FILENAME")
    exit(0)

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
    return str(out)[2:-1]

#Overwriting the bytes with null.
#->Map can be opened with empty password
def removePW(file,offset=184):
    fh = open(file, "r+b")
    fh.seek(offset)
    fh.write(b'\x00'b'\x00'b'\x00')
    fh.close()

print("Stored bytes: "+getRange(argv[1]))
removePW(argv[1])
print("Password removed")
