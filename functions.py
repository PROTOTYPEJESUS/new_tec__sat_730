




#US-001/create_register

user = []


def user_register():
        id = int(input("Agregue su id"))
        user.append(id)
        name = input("Agregue su nombre")
        user.append(name)
        last_name = input("Agregue su apellido")
        user.append(last_name)
        email = input("Agregue su email")
        user.append(email)
        password = input("Cree una contraseña de 8 caracteres entre numeros")
        user.append(password)
        print("Usuario creado exitosamente")
        print(user)