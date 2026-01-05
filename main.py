#1-misol
n = int(input("N sonini kiriting: "))

print("Tub sonlar:")
for son in range(2, n + 1):
    tub = True
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")

#2-misol
sonlar = list(map(int, input().split()))

eng_kop = sonlar[0]

for son in sonlar:
    if sonlar.count(son) > sonlar.count(eng_kop):
        eng_kop = son

print(eng_kop)


#3-misol
jumla = input("Jumlani kiriting: ")

sozlar_soni = len(jumla.split())

print("So'zlar soni:", sozlar_soni)


#4-misol
a = int(input("Parolni kiriting: "))

parol_generatori = len(a.split())

print("Parol generatori:", parol_generatori)


#5-misol
import random

loto = random.sample(range(1, 51), 6)
print("Sizning loto raqamlaringiz:", loto)
