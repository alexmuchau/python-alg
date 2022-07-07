#-------- array
users = [
  {"name": "aleques", "password": "123"}, 
  {"name": "vitor", "password": "123e"},
  {"name": "diogo", "password": "13323"}
]


#-------- functions
#--- after the verification, ask the user what he want.
def verification(_loggedIn: bool,):
  if _loggedIn == False:
    resp = 0
    while resp != 3:
      resp = int(input("Usuário inexistente. / 1 - REGISTRO / 2 - VOLTAR PARA LOGIN / 3 - SAIR /"))
      
      if resp == 1:
        registerWithNameVerification()
      else:
        if resp == 2:
          user = str(input("Entre com o user: "))
          login(user)
        else:
          if resp == 3:
            print("Saindo")
          else:
            print("Digite um numero valido")
              
  else:
    print("Logado")

#--- verification if user exists.
def functionUserNameExist(_username: str):
  for i in range(len(users)):
    userNameExist = users[i]["name"].count(_username)
    # print(userNameExist)
        
    if userNameExist == 1:
      return True
      # break
  return False

#--- sign in user.
def login(_username: str):
  usernameExist = functionUserNameExist(_username)
  
  if usernameExist == True:
    userPassword = input("Entre com a senha do user {}: ".format(_username))
    userLogado = {"name": _username, "password": userPassword}
      
    isExist = users.count(userLogado)
    
    cont = -1
    while isExist == 0:
      cont += 1
      if cont < 2:
        isExist = wrongPassLoop(_username)
      else:
        print("")
        print("Deseja tentar entrar em outra conta?")
        print("/ 1 - LOGIN EM OUTRA CONTA / 2 - REGISTRO DE CONTA / 3 - CONTINUAR TENTANDO /")
        resp = int(input(""))
        if resp == 1:
          print("")
          user = str(input("Entre com o user: "))
          loggedIn = login(user)
          verification(loggedIn)
        else:
          if resp == 2:
            registerWithNameVerification()
          else:
            if resp == 3:
              cont = -1
        
    return True
  else:
    return False

#--- put the user into a loop to try his password.
def wrongPassLoop(_username: str):
  print("")
  print("Senha errada para o user {}!!".format(_username))
  print("")
  userPassword = input("Entre com a senha do user {}: ".format(_username))
  userLogado = {"name": _username, "password": userPassword}
            
  userExist = users.count(userLogado)
  return userExist

#--- register with all the verification that needs.
def registerWithNameVerification():
  print("")
  newUsername = input("Qual será o nome do novo usuário? ")
  userNameExist = functionUserNameExist(newUsername)
        
  if userNameExist == True:
    loginRegister = 0
    while loginRegister != 3:
      print("")
      print("User ja existente. / 1 - LOGIN / 2 - VOLTAR PARA REGISTRO / 3 - SAIR /")
      loginRegister = int(input(""))
      if loginRegister == 1:
        wrongPassLoop()
        print("")
        print("Logado")
        return True
      else:
        if loginRegister == 2:
          isRegistered = register()
          if isRegistered == True:
            print("")
            print("Registrado")
            loginRegister = 3
            return True
  else:
    print("")
    newPass = input("Qual será a senha do usuário {}? " .format(newUsername))
    newUser = {"name": newUsername, "password": newPass}
    users.append(newUser)
    for i in range(len(users)):
      print("Username: {} with {} password".format(users[i]["name"], users[i]["password"]))
      
    return True

#--- basic register.
def register():
  print("")
  newUsername = input("Qual será o username do novo usuário?")
  userNameExist = functionUserNameExist(newUsername)
  if userNameExist == True:
    return False
  else:
    newPass = input("Qual será a senha do usuário {}? " .format(newUsername))
    newUser = {"name": newUsername ,"password": newPass}
    users.append(newUser)
    return True


#-------- home
resp = 0
while resp != 3:
  print("/ 1 - LOGIN / 2 - REGISTRO / 3 - SAIR /")
  resp = int(input(""))
  if resp == 1:
    user = str(input("Entre com o user: "))
    loggedIn = login(user)
    verification(loggedIn)
  else:
    if resp == 2:
      registerWithNameVerification()
    else:
      if resp == 3:
        print("Saindo")
      else:
        print("digite um numero valido")
  

