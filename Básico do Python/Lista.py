Lista = [1,1.14,"germano",[1,2,3],(1,2)]

minha_lista_de_compras = ["Sabão","Sabonete","Arroz",1,[1,2,3]]
minha_lista_de_compras[0] # Sabão
minha_lista_de_compras[1] # Sabonete
minha_lista_de_compras[2] # Arroz
minha_lista_de_compras[-1] # ultimo elemento da lista
minha_lista_de_compras[-1][-1] # ultimo elemento do ultimo elemento da lista
print("germano"[-3]) # letra a

for coisa in minha_lista_de_compras:
    print(coisa)

# Slice

n=[0,1,2,3,4,5,6,7,8,9]
n[0] # primeiro indice
n[6:] # a partir do 6 indice da lista
n[:6] # antes do 6 indice da lista
n[:-1] # todos exceto o ultimo
n[::-1] # todos os elementos invertidos
n[::2] # do inicio pulando 2
n[2:10:3] # do indice 2 ao 10 pulando 3

# matriz
matriz = [[0,1,2],[3,4,5],[7,8,9]]
matriz_3d=[[[1,2,3]],[[1,2,3]]]
print(matriz[0][1:]) # primeiro elemento, do indice 1 ao final
print(matriz_3d[0][0][0]) # o primeiro elemento: que é [[1,2,3]] do primeiro elemento: que é [1,2,3], do primeiro elemento: [1]

# Metodos

x=[1,2,3]
x.append(4) # coloca 4 na ultima posição da lista FILA
x.insert(4,0) # coloca 0 na posição 4             LISTA
x.count(2) # conta quantos 2 aparece na lista
x.remove(2) # remove o valor 2
x.pop(2) # tiro o elemento de indice 2
x.pop() # tira o ultimo elemento da lista         PILHA
x.reverse() # inverte a lista

compras=[]
resposta=" "

while resposta !="acabou": # Enquanto não digitar acabou, pergunta e insere novo item na lista de compra
    resposta=input("O que temos que comprar?   ")
    if resposta != "acabou":
        compras.append(resposta)
print(compras)
