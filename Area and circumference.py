#Napisz program, który wczyta od użytkownika wartość promienia okręgu, następnie wyliczy jego pole i obwód.
import math
promien = (float(input("Podaj promień okręgu: ")))
pole = math.pi * promien ** 2
obwód = 2 * math.pi * promien
średnica = 2 * promien
print(f"Pole okręgu o promieniu {promien} wynosi {pole:.2f}")
print(f"Obwód okręgu wynosi {obwód:.2f}")
print(f"Średnica okręgu wynosi {średnica:.2f}")