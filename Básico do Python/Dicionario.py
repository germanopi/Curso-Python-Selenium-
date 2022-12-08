dicionario = {
    "chave": "valor" , # diz que o indice para encontrar valor é chave
    "chave_2": ["valor_2","valor_3"]

}

dicionario["chave"]

pessoa = {
"nome": "Eduardo" ,
"idade": 26 ,
"telefones": {
    "residencial": 1234,
    "comercial": 4567,
    }
}
nome_idade["nome"] = "João" # Atribui novo nome para Eduardo

def imprime_relatorio(pessoa):
    return f"""

     Relatorio parcial

     {pessoa["nome"]},
     com idade {pessoa["idade"]},
     e telefone {pessoa["telefones"]}

     Está de férias

     """

imprime_relatorio(pessoa)

# Metodos

dicionario.popitem() # tira um elemento aleatorio
dicionario.keys() # retorna as chaves
dicionario.values() # retorna os valores
dicionario.setdefault("Carlos") # adiciona uma nova chave sem valor
