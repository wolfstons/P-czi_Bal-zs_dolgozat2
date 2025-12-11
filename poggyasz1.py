from Pogyasz import Pogyasz
def beolvasas():
    poggyasz_lista=[]
    file=open("Csomag.txt","r",encoding="utf-8")
    file.readline()
    file_elsonelkul_sorokba=file.readlines()
    file.close()
    i=0
    while i<len(file_elsonelkul_sorokba):
            sor=file_elsonelkul_sorokba[i].strip().split("#")
            poggyasz=Pogyasz(int(sor[0]),int(sor[1]),int(sor[2]),int(sor[3]))
            poggyasz_lista.append(poggyasz)
            i+=1
    print("III/A,B:")
    print(f"\tA poggyászok száma: {len(poggyasz_lista)}")
    return poggyasz_lista
def pogyasz_kiir(poggyasz_lista):
    i=0
    db=0
    suly=0
    while i<len(poggyasz_lista):
        if (poggyasz_lista[i].szelesseg)==51:
             db+=1
             suly+=poggyasz_lista[i].tomeg
        i+=1 
    print("III/C:")
    atlag=suly/db
    atlag2=atlag*1000
    print(f"\tAz 51 cm-es poggyászok átlag tömeg értéke: {atlag2} g")


def magassag(poggyasz_lista):
    print("III/D:")
    i=0
    max_magassag=poggyasz_lista[0].magassag
    while i<len(poggyasz_lista):
        if poggyasz_lista[i].magassag>max_magassag:
            max_magassag=poggyasz_lista[i].magassag
            mentett_i=i
        i+=1
    print(f"\tA legnagyobb magasságú poggyász mérete: {poggyasz_lista[mentett_i].magassag}x{poggyasz_lista[mentett_i].szelesseg}x{poggyasz_lista[mentett_i].melyseg}cm, tömege: {poggyasz_lista[mentett_i].tomeg}kg")
    return max_magassag