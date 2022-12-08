x=7
y=6

if x==y:
    print("Mesmo Valor")
elif x>y: # Else if
    print("x é maior que y")
else:
    print(f"Não sei resolver {x} e {y}")

carteira = int(input("Quanto eu tenho? "))
produto = int(input("Quanto eu custa? "))
preciso = input("Preciso mesmo disso [s/n]?")

if carteira >= produto and preciso=="s":
    print("Comprei")
else:
    print("Não comprei")
