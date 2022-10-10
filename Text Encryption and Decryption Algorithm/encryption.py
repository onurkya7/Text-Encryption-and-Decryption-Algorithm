import random

chars = "!%+=)?(/&*_-><.;#[}:,é$]{'£€@"
chars2 = "5930872416"

sayi = []
for i in chars2:
    for j in chars2:
        sayi.append(str(chars2.index(i)) + str(chars2.index(j)))

space = "~½|`"

b = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
k = "abcçdefgğhıijklmnoöprsştuüvyz"

giris = input("Şifrelenecek metni giriniz: \n")
dizi = []
depo = []

for i in giris:
    if(i in k):
        for j in k:
            if (i == j):
                if (i in depo):
                    sayac = sayi[depo.count(i)]
                    m = chars[(k.index(j) + depo.count(i)) % 29]
                    for q in str(sayac):
                       dizi.append(str(chars2[int(q)]))
                       dizi.append(random.choice(chars))
                    dizi.append(m)
                    dizi.append(random.choice(chars2))
                    depo.append(i)
                else:
                    m = chars[k.index(j)]
                    dizi.append(str(5))
                    dizi.append(random.choice(chars))
                    dizi.append(str(5))
                    dizi.append(random.choice(chars))
                    dizi.append(m)
                    dizi.append(random.choice(chars2))
                    depo.append(i)
    elif(i == " "):
        bosluk = random.choice(space) + random.choice(chars2)
        dizi.append(bosluk)

    elif(i in b):
        for h in b:
            if(i == h):
                buyuk = k[b.index(i) - 5]
                dizi.append(buyuk)
                dizi.append(random.choice(chars2))
                
    elif(i in chars):
        for h in chars:
            if(i == h):
                ozel = b[chars.index(i) + 3]
                dizi.append(ozel)
                dizi.append(random.choice(chars2))


print("\n" + ''.join(dizi))
