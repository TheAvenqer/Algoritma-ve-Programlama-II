def bol(bolunen, bolen):
  if bolunen == 0:
    return 0
  if bolen <= bolunen:
    print(bolunen,bolen)
    return 1 + bol(bolunen-bolen, bolen)
  else:
    print(bolunen, bolen)
    return 0.1 * (1+bol(bolunen*10-bolen, bolen))
sayi=float(input("Bir sayi girin"))
bölünecek=float(input("Kaça bölünecek"))
sayac=0.0
print(bol(sayi,bölünecek))
