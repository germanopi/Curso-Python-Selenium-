x = int(input("Escolha um numero para decrescer   ")) # Recebe uma string como resposta e converte para inteiro
y = int(input("Escolha um numero de parada    "))
while x>=0:
    print(x)
    x-=1
    if x==y:
        print(f"Entrou no Break, não vai printar {y}")
        break # sai do While
else:
    x-=1

palavra="Python"
for letra in palavra: # Para cada elemento da interação, os elementos são (P,y,t,h,o,n)
    print(letra) # imprima o elemento

palavra="Python"
for posição, letra in enumerate(palavra): # Para cada elemento da interação enumerada
    print(posição, letra) # imprima o numero e o elemento

frase = "Eduardo saiu de casa".split()
for palavra in frase: # Os elementos são (Eduardo,saiu,de,casa)
    if palavra=="Eduardo":
        print("Eduardo")
    else:
        print("Não Eduardo")

for valor in range(10): # Executa 10 vezes
 print(valor)
 valor+=1
