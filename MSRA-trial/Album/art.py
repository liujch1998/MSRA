from PIL import Image
import numpy as np

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def transform(M, Array, rgb):
    A = []
    for i in Array:
        tmp = []
        for j in i:
            tmp.append(j[rgb])
        A.append(tmp)
    AA = np.array(A)
    Ainv = np.dot(np.dot(M, AA), np.transpose(M))
    #Ainv = np.dot(M,AA)
    return Ainv
    
def printf(M):
    print('{')
    for i in M:
        print('{')
        for j in i:
            print(j)
            print(',')
        print('\b')
        print('}')
    print('}')


for tt in range (1,51,1):
    im = Image.open ("pic.bmp")
    size = (1000,1000)
    im = im.resize(size)

    pix = []
    for i in range (0,size[1],1):
        tmp = []
        for j in range (0,size[0],1):
            tmp.append (im.getpixel((j,i)))
        pix.append (tmp)
    
    #print(pix)

    randMatrix = np.random.random(size)
    for i in range(1,size[0]+1,1):
        for j in range(1,size[1]+1,1):
            randMatrix[i-1][j-1] = np.power((i+j)%1000+1,tt/50.0)
    RandMatrix = []
    for i in randMatrix:
        tmp = []
        for j in i:
            tmp.append(j)
        RandMatrix.append(tmp)
    normRandMatrix = []
    for i in randMatrix:
        tmp = []
        summ = 0.0
        for j in i:
            summ += j
        for j in i:
            tmp.append(j/summ)
        normRandMatrix.append(tmp)
    
    r = transform(normRandMatrix, pix, 0)
    g = transform(normRandMatrix, pix, 1)
    b = transform(normRandMatrix, pix, 2)

    pix = []
    for i in range (0,size[1],1):
        tmp = []
        for j in range (0,size[0],1):
            tmp.append((int(r[i][j]), int(g[i][j]), int(b[i][j])))
        pix.append(tmp)
    
    #print(pix)
    
    pixx = []
    for i in pix:
        for j in i:
            pixx.append(j)

    im.putdata(pixx)
    #im.show()

    invNormRandMatrix = np.linalg.inv (normRandMatrix)
    rr = transform(invNormRandMatrix, pix, 0)
    gg = transform(invNormRandMatrix, pix, 1)
    bb = transform(invNormRandMatrix, pix, 2)

    if size[0] <= 100:
        #print(RandMatrix)
        #print(normRandMatrix)
        print(invNormRandMatrix)

    pix = []
    for i in range (0,size[1],1):
        tmp = []
        for j in range (0,size[0],1):
            tmp.append((int(rr[i][j]), int(gg[i][j]), int(bb[i][j])))
        pix.append(tmp)
    
    #print(pix)
    
    pixx = []
    for i in pix:
        for j in i:
            pixx.append(j)

    im.putdata(pixx)
    #im.show()
    im.save("art_"+str(tt)+".bmp")
