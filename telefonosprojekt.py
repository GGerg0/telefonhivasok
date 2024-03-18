def mpbe(o,p,mp):
    return int(o*3600+p*60+mp)

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

print(f"4. feladat\nA leghosszabb ideig vonalban levo hivo {leghosszabb[0]}. sorban szerepel,\na hivas hossza: {leghosszabb[1]} masodperc\n")

bemenet = input("5. feladat\nAdjon meg egy időpontot! (ora perc masodperc) ").split(" ")
bemenet = mpbe(int(bemenet[0]),int(bemenet[1]),int(bemenet[2]))

sorszam = []

varakozo = 0

for hivasok in range(len(adatok)):
    start = mpbe(int(adatok[hivasok][0]),int(adatok[hivasok][1]),int(adatok[hivasok][2]))
    end = mpbe(int(adatok[hivasok][3]),int(adatok[hivasok][4]),int(adatok[hivasok][5]))
    if bemenet < end:
        if bemenet > start:
            varakozo += 1
            sorszam.append(hivasok)
            
print(f'A varakozok szama: {varakozo-1} a beszelo a {sorszam[0]+1}. hivo.\n')
            
sorszam = 0
varakozas = 0
elozo = 0
for hivasok in range(len(adatok)):
    start = mpbe(int(adatok[hivasok][0]),int(adatok[hivasok][1]),int(adatok[hivasok][2]))
    end = mpbe(int(adatok[hivasok][3]),int(adatok[hivasok][4]),int(adatok[hivasok][5]))
    
    if int(adatok[hivasok][0]) < 12:
        if end > elozo:
            sorszam = hivasok+1
            varakozas = elozo - start
            elozo = end
            
print(f"6. feladat\nAz utolso telefonalo adatai a(z) {sorszam}. sorban vannak, {varakozas} masodpercig vart.")

stat = open("sikeres.txt","wt")

sorszam = 0
elozo = 0
befejezes = [8,0,0]
index = 0
for hivasok in range(len(adatok)):
    start = mpbe(int(adatok[hivasok][0]),int(adatok[hivasok][1]),int(adatok[hivasok][2]))
    end = mpbe(int(adatok[hivasok][3]),int(adatok[hivasok][4]),int(adatok[hivasok][5]))
    
    if int(adatok[hivasok][3]) >= 8 and int(adatok[hivasok][0]) < 12:
        
        if end > elozo:
            stat.write(f"{hivasok+1} ")
            for i in range(len(befejezes)):
                stat.write(f'{befejezes[i]} ')
            befejezes = [adatok[hivasok][3],adatok[hivasok][4],adatok[hivasok][5]]
            for i in range(len(befejezes)):
                stat.write(f"{befejezes[i]} ")
            stat.write("\n")
            elozo = end
            