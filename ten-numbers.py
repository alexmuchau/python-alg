numPar = []
numImpar = []
numImparLength = 0
numParLength = 0

for numero in range(10):
  num = int(input("Qual o {} numero? ".format(numero + 1)))
  imparOuPar = num % 2
  
  if imparOuPar == 1:
    if numImparLength < 5:
      numImpar += [num]
      numImparLength = len(numImpar)
      print("Voce digitou um numero impar, contando com esse, voce ja adicionou {} numeros impares".format(numImparLength))
    else:
      print("Voce já digitou 5 números impares")
      while imparOuPar == 1:
        num = int(input("Digite um numero par,Qual o {} numero? ".format(numero + 1)))
        imparOuPar = num % 2
        
        numPar += [num]
        numParLength = len(numPar)
        print("Voce digitou um numero par, contando com esse, voce ja adicionou {} numeros pares".format(numParLength))
  else:
    if numParLength < 5:
      numPar += [num]
      numParLength = len(numPar)
      print("Voce digitou um numero par, contando com esse, voce ja adicionou {} numeros pares".format(numParLength))
    else:
      print("Voce já digitou 5 números impares")
      while imparOuPar == 2:
        num = int(input("Digite um numero impar, Qual o {} numero? ".format(numero + 1)))
        imparOuPar = num % 2
        
        numImpar += [num]
        numImparLength = len(numImpar)
        print("Voce digitou um numero impar, contando com esse, voce ja adicionou {} numeros impares".format(numImparLength))

print("")    
print("TODOS OS NUMEROS PARES SAO")
print(numPar)

print("")    
print("TODOS OS NUMEROS IMPARES SAO")
print(numImpar)

  