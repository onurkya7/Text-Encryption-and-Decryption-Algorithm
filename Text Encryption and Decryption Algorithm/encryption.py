import random

chars = "!%+=)?(/&*_-><.;#[}:,é$]{'£€@"
chars2 = "5930872416"
space = "~½|`"
b = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
k = "abcçdefgğhıijklmnoöprsştuüvyz"

sayi = [str(chars2.index(i)) + str(chars2.index(j)) for i in chars2 for j in chars2]

def encrypt_char(char, index):
    if char in k:
        m = chars[(k.index(char) + depo.get(char, 0)) % 29]
        sayac = sayi[depo.get(char, 0)]
        return [str(chars2[int(q)]) + random.choice(chars) for q in str(sayac)] + [m, random.choice(chars2)]
    elif char == " ":
        return [random.choice(space) + random.choice(chars2)]
    elif char in b:
        buyuk = k[b.index(char) - 5]
        return [buyuk, random.choice(chars2)]
    elif char in chars:
        ozel = b[chars.index(char) + 3]
        return [ozel, random.choice(chars2)]
    return []

giris = input("Enter the text to be encrypted:\n")
dizi = []
depo = {}

for char in giris:
    dizi.extend(encrypt_char(char, giris.count(char)))
    depo[char] = depo.get(char, 0) + 1

print("\n" + ''.join(dizi))
