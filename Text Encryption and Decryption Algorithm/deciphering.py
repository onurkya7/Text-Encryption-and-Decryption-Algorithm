chars ="abcçdefgğhıijklmnoöprsştuüvyz"
chars2 ="5930872416"
chars3 ="0123456789"
space = "~½|`"

sayi = []
for i in chars2:
    for j in chars2:
        sayi.append(str(chars2.index(i)) + str(chars2.index(j)))

b="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
k="!%+=)?(/&*_-><.;#[}:,é$]{'£€@"

giris = input("Deşifre olacak metni giriniz: \n")
dizi=[]
depo=[]
depo2=[]

for i in range(len(giris)):
    
    if (giris[i] in b):
      for a in b:
          if (a == giris[i]):
             ozel = k[(b.index(giris[i]) - 3) % 29]
             dizi.append(ozel)
             
    if (giris[i] in chars):
      for a in chars:
          if (a == giris[i]):
             z = b[(chars.index(giris[i]) + 5) % 29]
             dizi.append(z)    
    
    elif (giris[i] in space):
        dizi.append(" ")
    
    elif (i % 2 == 0):
        if (giris[i].isdigit()):
            if not depo2:
              x = chars3[chars2.index(giris[i])]
              depo2.append(x)
            else:
              y = chars3[chars2.index(giris[i])]
              if x == "0":
                sayac = int(str(y))
              else:
                sayac = int(str(depo2[0]) + str(y))    
        else:
             for j in k:
                if (giris[i] == j):
                   if (depo.count(chars[(k.index(j) - sayac)%29]) == sayac):
                      n = chars[(k.index(j) - sayac)%29]
                      depo.append(n)
                      dizi.append(n)
                      depo2=[]
            
                   else:
                      n = chars[k.index(j)]
                      depo.append(n)
                      dizi.append(n)
              
print("\n" + ''.join(dizi))