# -*- coding: utf-8 -*-
dosya=open("/home/theavenqer/Masaüstü/b.txt","r+")
sayac=0
while sayac<100:
    a=str(sayac)
    dosya.writelines(a)
    dosya.writelines("\n")
    sayac+=1
dosya.close()
dosya=open("/home/theavenqer/Masaüstü/b.txt","r")
print(dosya.read())
