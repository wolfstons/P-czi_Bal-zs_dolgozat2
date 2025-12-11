from Pogyasz import Poggyasz
def beolvasas():
    meret_lista=[]
    lista=open("Csomag.txt","r",encoding="utf-8")
    lista.readline
    lista_elsonelkul_sorokba=lista.readlines
    lista.close
    i=0
    while i<len(lista_elsonelkul_sorokba):
            sor=lista_elsonelkul_sorokba[i].strip().split("#")
            Poggyasz=(int(sor[0]),sor[1],int(sor[2]),sor[3])
            meret_lista.append(Poggyasz)
            i+=1
    print("III/A,B:")
    print(f"\tA poggyászok száma: {len(meret_lista)}")

def max_tomeg(meret_lista):
      if meret_lista[i]==51:
            