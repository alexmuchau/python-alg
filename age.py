idades = []
maiorIdade = []
mais25 = []
somaIdade = 0
maiorIdadeLength = 0

pessoas = int(input("quantas pessoas serao entrevistadas? "))

for pessoa in range(pessoas):
  idade = int(input('qual a idade da pessoa {}?'.format(pessoa + 1)))
  idades += [idade]
  
  somaIdade += idade
  
  if pessoa == 0:
    maiorIdade = [[pessoa, idade]]
  else:
    if maiorIdadeLength > 1:
      for i in range(1):
        if idade > maiorIdade[i][1] :
          maiorIdade = [[pessoa, idade]]
        else:
          if idade == maiorIdade[i][1]:
            maiorIdade += [[pessoa, idade]]
    else:
      if idade > maiorIdade[0][1] :
        maiorIdade = [[pessoa, idade]]
      else:
        if idade == maiorIdade[0][1]:
          maiorIdade += [[pessoa, idade]]
        
  if idade >= 25:
    mais25 += [pessoa]
  
  maiorIdadeLength = len(maiorIdade)
  

mediaIdade = somaIdade/pessoas

print("AS IDADES LIDAS FORAM:")
print(idades)
print("")

print("AS IDADES COM MAIS DE 25 ANOS FORAM:")
print(mais25)
print("")

print("A(S) MAIOR(ES) IDADE(S) FORAM:")
for qtd in range(maiorIdadeLength):
  print("A pessoa {} com a idade {}".format(maiorIdade[qtd][0] + 1, maiorIdade[qtd][1]))  
print("")

print("A MEDIA DAS IDADES FOI:")
print(mediaIdade)

    

  