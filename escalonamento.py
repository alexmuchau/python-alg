eq1 = []
eq2 = []
eq3 = []

eq1 = [int(input("x1: "))]
eq1 += [int(input("y1: "))]
eq1 += [int(input("z1: "))]
eq1 += [int(input("resultado: "))]

eq2 = [int(input("x2: "))]
eq2 += [int(input("y2: "))]
eq2 += [int(input("z2: "))]
eq2 += [int(input("resultado: "))]

eq3 = [int(input("x3: "))]
eq3 += [int(input("y3: "))]
eq3 += [int(input("z3: "))]
eq3 += [int(input("resultado: "))]

print("")
print("MATRIZ COM TODOS OS VALORES")
print(eq1)
print(eq2)
print(eq3)


# Primeiro zero
firstNumToZero = -(eq2[0]/eq1[0])
firstZeroX1 = firstNumToZero*eq1[0]
firstZeroY1 = firstNumToZero*eq1[1]
firstZeroZ1 = firstNumToZero*eq1[2]
firstZeroW1 = firstNumToZero*eq1[3]

eq2[0] = firstZeroX1 + eq2[0]
eq2[1] = firstZeroY1 + eq2[1]
eq2[2] = firstZeroZ1 + eq2[2]
eq2[3] = firstZeroW1 + eq2[3]

print("")
print("ZERANDO O PRIMEIRO ZERO")
print(eq1)
print(eq2)
print(eq3)

# Segundo zero
secondNumToZero = -(eq3[0]/eq1[0])
secondZeroX1 = secondNumToZero*eq1[0]
secondZeroY1 = secondNumToZero*eq1[1]
secondZeroZ1 = secondNumToZero*eq1[2]
secondZeroW1 = secondNumToZero*eq1[3]

eq3[0] = secondZeroX1 + eq3[0]
eq3[1] = secondZeroY1 + eq3[1]
eq3[2] = secondZeroZ1 + eq3[2]
eq3[3] = secondZeroW1 + eq3[3]

print("")
print("ZERANDO O SEGUNDO ZERO")
print(eq1)
print(eq2)
print(eq3)

# Terceiro Zero
thirdNumToZero = -(eq3[1]/eq2[1])
thirdZeroY2 = thirdNumToZero*eq2[1]
thirdZeroZ2 = thirdNumToZero*eq2[2]
thirdZeroW2 = thirdNumToZero*eq2[3]

eq3[1] = thirdZeroY2 + eq3[1]
eq3[2] = thirdZeroZ2 + eq3[2]
eq3[3] = thirdZeroW2 + eq3[3]

print("")
print("ZERANDO O TERCEIRO ZERO")
print(eq1)
print(eq2)
print(eq3)

# Descobrindo os valores

z = eq3[3]/eq3[2]
y = (eq2[3] - (eq2[2]*z))/eq2[1]
x = (eq1[3] - ((eq1[2]*z) + (eq1[1]*y)))/eq1[0]

print("")
print("OS VALORES DAS VARIÁVEIS :")
print("X: {}".format(x))
print("Y: {}".format(y))
print("Z: {}".format(z))
