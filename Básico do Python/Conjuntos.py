x={1,2,3}
y={3,4,5}

# Metodos

x.union(y) # {1,2,3,4,5} retorna um novo conjunto unindo
x.update(y) # {1,2,3,4,5} atualiza o conjunto x colocando y dentro
x.difference(y) # {1,2}
x.discard(1) # {2,3}
x.intersection(y) # {3}
x.pop() # pode tirar qualquer elemento do conjunto

lista = [1,1,1,1,1,1,2,2,3,4,5,6,7,8,89,9,10]
set(lista) # converte a lista em conjunto {}, removendo repetição
list(lista) # converte  em lista []
tuple(lista) # converte em tupla ()
