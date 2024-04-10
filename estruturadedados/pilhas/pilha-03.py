# 3) Dada a seguinte sequência de push em uma pilha, crie um 
# programa em C que elimine o maior e o menor número.

# pilha.push(30);
# pilha.push(10);
# pilha.push(20);
# pilha.push(50);
# pilha.push(40);

def retirarMaior (pilha):
    pilha.remove(max(pilha))

def retirarMenor (pilha):
    pilha.remove(min(pilha))

pilha = [30, 10, 20, 50, 40]
print(pilha)
retirarMaior(pilha)
retirarMenor(pilha)
print(pilha)

