# 1) Levando em consideração uma pilha inicialmente vazia e que as
# seguintes operações foram realizadas, responda:

# pop()
# push(p, 'a')
# push(p, 'c')
# top()
# size()
# push(p, 'g')
# pop()
# push(p, 'm')
# pop()
# top()
# pop()
# pop()
# empty()

pilha = []
# pilha.pop()
pilha.append('a')
pilha.append('c')
print(pilha[(len(pilha)-1)])
len(pilha)
pilha.append('g')
pilha.pop(len(pilha)-1)
pilha.append('m')
pilha.pop(len(pilha)-1)
print(pilha[(len(pilha)-1)])
pilha.pop(len(pilha)-1)
pilha.pop(len(pilha)-1)

def empty(pilha):
    if len(pilha) == 0:
        return 0
    else:
        return 1

print(empty(pilha)) # retorno do passo 13

# a) Qual o retorno do passo 1? 0 pois a lista está vazia
# b) Qual o retorno do passo 4? c pois o último elemento da pilha é c
# c) Qual o retorno do passo 5? 2 pois a pilha é composta de 2 elementos
# d) Qual o retorno do passo 10? c pois o último elemento da pilha é c
# e) Qual o retorno do passo 13? 0 pois a pilha está vazia


