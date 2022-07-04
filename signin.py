usuarios = [["aleques", "vitor", "123"], ["vitor", "123"] ,["diogo", "13323"]]

usuario = str(input("Entre com o usuario: "))
senha = input("Entre com a senha: ")
usuarioLogado = [usuario, senha]

isExist = usuarios.count(usuarioLogado)

print(isExist)

if isExist == 0:
  userNameExist = 0
  for i in range(3):
    userNameExist = userNameExist + usuarios[i].count(usuario)

  if userNameExist >= 1:
    print("Usuário existente! Porem senha errada")
  else:
    resp = int(input("Usuário inexistente, deseja criar uma conta? Digite 1"))
    if resp == 1:
      newUsername = input("Qual será o nome do usuário?")
      newPass = input("Qual será a senha do usuário {}" .format(newUsername))
      newUser = [newUsername, newPass]
      usuarios.insert(0 ,newUser)
      print(usuarios)   
else:
  print("Logado")

