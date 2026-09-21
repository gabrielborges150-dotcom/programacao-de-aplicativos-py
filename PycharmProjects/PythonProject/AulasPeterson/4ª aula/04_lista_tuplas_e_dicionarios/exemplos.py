#Listas, Tuplas e Dicionários

#1. Listas

#Listas são utilizadas para armazenar vários valores dentro de uma unica variavel
nomes = ["Ana" ,  "Carlos" , "João" , "Maria"]
print(nomes)

#2. Acessando elementos na lista

print(nomes[0])
print(nomes[1])

# Podemos acessar o ultimo elementos usando -1
print(nomes[-1])

# 3. Alterando elementos

nomes[0] = "Pedro"
print(nomes)

# 4. Adicionando Elementos
#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

# insert() adiciona um elemento em uma posição

nomes.insert(1 , "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() remove o um elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)