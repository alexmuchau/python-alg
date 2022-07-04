# 1,1,2,3,5

atual = 1
antigo = 1

print(atual)
print(antigo)

for i in range(15):
    atual = atual + antigo
    antigo = atual - antigo
    print(atual)
