import random

def sorozat():
    szamsorozat=[]
    for i in range(0,12,1):
        szam=random.randint(-10,1000)
        szamsorozat.append(szam)
    print("II/A,B,C:")
    print(f"\t{szamsorozat[i]}",end="$")
    for i in range(0,10,1):
        print(f"{szamsorozat[i]}",end="$")
    print(f"{szamsorozat[i]}",end="\n")
    return szamsorozat

def paratlanok_szama(szamsorozat):
    paratlanok_szama=0
    i=0
    while i<len(szamsorozat):
        i+=1
        valtozo=szamsorozat[i]/2
        if szamsorozat[i]/2==1:
            paratlanok_szama+=1
    return paratlanok_szama


def konzol_kiir(paratlanok_szama):
    print("II/D,E:")
    print(f"\tA páratlanok száma: {paratlanok_szama}")


def fajlba_kiir():
    f=open("eredmeny.txt","w",encoding="UTF-8")
    f.write
    
    
    
