import math # ei tohiks olla tarnik (*) ega "form"
print("Ruudu karakteristikud")
a=input('Sisesta ruudu külje pikkus => ')
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) # seal on ainult üks (") kuid peaks olema kaks.
di=a*math.sqr(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") # kahekordselt ) lõpus 
b=input("Sisesta ristküliku 1. külje pikkus => ")
c=input("Sisesta ristküliku 2. külje pikkus => ")
S=b*c
print("Ristküliku pindala", S) # seal oli (') sõna pindala kõrval ja ristkuliku pindalal ei olnud (")
P=2(b+c)
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di)) # unustati ) lõppu 
print()
print("Ringi karakteristikud")
r=input("Sisesta ringi raadiusi pikkus => ") # ei olnud pandud (") ja ) oli lõpus
d=2*r # enne oli "2r" kuid peaks olema "2*r".
print("Ringi läbimõõt", d) # ei olnud koma
S=pi()*r*2
print("Ringi pindala", round(S))
C=2*pi()*r # sama asi nagu enne, 2pi kuid peaks olema 2*pi
print("Ringjoone pikkus", round(C)) # peab olema ) lõpus
