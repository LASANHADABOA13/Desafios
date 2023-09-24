from time import sleep

print("tempo de descanso")

for i in range (45, 0, -1):
    sleep(1)
    print("tempo restante: ", i, "segundos")

print("seu tempo de descanso acabou")