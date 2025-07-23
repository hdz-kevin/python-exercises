""""
Preparando un Colacao:
    Comprobar si hay leche en la nevera, y colacao en la despensa.
    Si hay leche y colacao, preparar el colacao.
    Si no hay leche, avisar de que hay que comprar leche.
    Si no hay colacao, avisar de que hay que comprar colacao.
"""

print("=========  Colacao Preparation  ==========")
print("Abro la nevera")

milk = input("\n¿Hay leche? (S/N): ").strip().lower()
if milk != "s":
    print("\nDebemos comprar leche primero.")
    exit()

colacao = input("\n¿Hay colacao en la despensa? (S/N): ").strip().lower()
if (colacao != "s"):
    print("\nDebemos comprar colacao primero.")
    exit()

print("\nVertimos leche en el vaso...")
print("Agregamos colacao al vaso...")
print("Mezclando...")
print("\nDisfrutamos nuestro colacao :)")
