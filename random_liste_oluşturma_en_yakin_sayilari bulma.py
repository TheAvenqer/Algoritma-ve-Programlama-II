import random
sayac=0
karma=[]
duz=[]
while sayac<100:
    a=random.random()
    karma.append(a)
    sayac+=1
sayac2=0
while sayac2<100:
    sayac3=0
    enb=karma[0]
    while sayac3<len(karma):
        konum=karma[sayac3]
        if konum>enb:
            enb=konum
        sayac3+=1
    duz.append(enb)
    karma.remove(enb)
    sayac2+=1
sayacbul=0
bas=duz[sayacbul]
son=duz[sayacbul+1]
sonuc=bas-son
while sayacbul<99:
    bas+=1
    son+=1
    bunemk=bas-son
    if sonuc>bunemk:
        bul=sayacbul
        bul2=sayacbul+1
        sonuc=bunemk
    sayacbul+=1
print("Birbirine en yakın 2 sayı bunlardır : ",duz[bul],"------",duz[bul2],sonuc)
