def mpbe(o,p,mp):
    return o*3600+p*60+mp

'''o = int(input())
p = int(input())
mp = int(input())

print(mpbe(o,p,mp))'''

f= open("hivas.txt", "rt")

orak = {}

for sor in f:
    sor = sor.strip().split(" ")
    if sor[0] in orak:
        orak[sor[0]] += 1
    else:
        orak[sor[0]] = 1


print("3. Feladat")
for k,v in orak.items():
    print(f"{k} ora {v} hivas")