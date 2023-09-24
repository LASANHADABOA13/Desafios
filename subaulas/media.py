m1 = int(input("digite a primeira nota: "))
m2 = int(input("digite a segunda nota: "))
m3 = int(input("digite a terceira nota: "))

media = (m1+m2+m3) / 3

print(media)

if media <= 4:
    print("reprovado")
elif media < 7:
    print("Recuperação")
else:
    print("Aprovado")