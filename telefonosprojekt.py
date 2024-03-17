def mpbe(o,p,mp):
    return int(o*3600+p*60+mp)

'''o = int(input())
p = int(input())
mp = int(input())

print(mpbe(o,p,mp))'''

f= open("hivas.txt", "rt")

orak = {}
adatok = []

for sor in f:
    sor = sor.strip().split(" ")
    adatok.append(sor)
    if sor[0] in orak:
        orak[sor[0]] += 1
    else:
        orak[sor[0]] = 1


print("3. Feladat")
for k,v in orak.items():
    print(f"{k} ora {v} hivas")

leghosszabb = [0,0]
for hivasok in range (len(adatok)):
    masodperc = mpbe(int(adatok[hivasok][3]),int(adatok[hivasok][4]),int(adatok[hivasok][5])) - mpbe(int(adatok[hivasok][0]),int(adatok[hivasok][1]),int(adatok[hivasok][2]))
    if leghosszabb[1] < masodperc:
        leghosszabb = hivasok+1,masodperc

print(f"A leghosszabb ideig vonalban levo hivo {leghosszabb[0]}. sorban szerepel,\n a hivas hossza: {leghosszabb[1]} masodperc")