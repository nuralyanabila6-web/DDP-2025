def kubus(sisi):
    return 6*sisi*sisi

def balok(p,l,t):
    return 2*(p*l + p*t + l*t)

def prisma(la,ka,t):
    return 2*la + ka*t

def tabung(r,t):
    return 2*3.14*r*(r+t)

def kerucut(r,s):
    return 3.14*r*(r+s)

#print(kerucut(3,9))
#print (tabung(3,6))
#print(prisma(3,3,3))
#print(balok(3,3,3))
#print(kubus(3))