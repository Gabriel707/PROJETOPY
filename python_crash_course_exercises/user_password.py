right_user = 'admaster'
right_password = 'admin123*'


def user_and_password_checker(username, password):
    username = input("Insira seu usuario: ")
    password = input("Insira a sua senha: ")

    if username == right_user and password == right_password:
        print(f"Username correto: {
              right_user} \n Senha correta: {right_password}")

    elif username != right_user and password == right_password:
        print(f"Almost there, password matched: {right_password}")


user_and_password_checker('admin', 'admin123*')
