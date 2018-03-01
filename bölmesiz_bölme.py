def ilk(sayi,bölünecek,sayac):
    sayac+=1
    if sayac*bölünecek==sayi:
        return sayac
    elif sayac*bölünecek>sayi:
        return ondalıklı(sayi,bölünecek,sayac)
    else:
        return ilk(sayi,bölünecek,sayac)
def ondalıklı(sayi,bölünecek,sayac):
    sayac+=0.1
    sayac2+=1
    if sayac2==0.9:
        if sayac*bölünecek==sayi:
            return sayac
        else:
            return sayac
    else:
        if sayac*bölünecek==sayi:
            return sayac
        else:
            return ondalıklı(sayi,bölünecek,sayac)
sayi=float(input("Bir sayi girin"))
bölünecek=float(input("Kaça bölünecek"))
sayac=0.0
print(ilk(sayi,bölünecek,sayac,sayac2))