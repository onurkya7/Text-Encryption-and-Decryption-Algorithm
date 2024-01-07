chars = "abcçdefgğhıijklmnoöprsştuüvyz"
chars2 = "5930872416"
chars3 = "0123456789"
space = "~½|`"

sayi = [str(chars2.index(i)) + str(chars2.index(j)) for i in chars2 for j in chars2]

b = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
k = "!%+=)?(/&*_-><.;#[}:,é$]{'£€@"

giris = input("Enter the text to be decrypted:\n")
dizi = []
depo = []
depo2 = []
sayac = 0

for i, char in enumerate(giris):
    if char in b:
        ozel = k[(b.index(char) - 3) % 29]
        dizi.append(ozel)

    elif char in chars:
        z = b[(chars.index(char) + 5) % 29]
        dizi.append(z)

    elif char in space:
        dizi.append(" ")

    elif i % 2 == 0 and char.isdigit():
        y = chars3[chars2.index(char)]
        sayac = int(str(depo2[0]) + str(y)) if depo2 else int(str(y))
        depo2.append(y)

    elif i % 2 == 0 and char in k:
        n = chars[(k.index(char) - sayac) % 29]
        depo.append(n)
        dizi.append(n)
        depo2 = []

print("\n" + ''.join(dizi))
