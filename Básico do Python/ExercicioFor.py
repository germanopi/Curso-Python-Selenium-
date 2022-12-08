palavra = "abracadabra"

for letra in palavra:
        if letra =="a":
            print("a virou Germano")
        elif letra =="e":
            print("e virou Germano")
        elif letra =="i":
            print("i virou Germano")
        elif letra =="o":
            print("o virou Germano")
        elif letra =="u":
            print("u virou Germano")
        else:
            print(letra)

vogal="aeiou"
for letra in palavra:
    if letra in vogal:
        print("vogal virou Germano")
    else:
        print(letra)
