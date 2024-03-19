idade_user = int(input("Qual sua idade? "))

if idade_user >= 0 and idade_user <= 12:
    print("Criança")
elif idade_user >= 13 and idade_user <= 18:
    print("Adolescente")
elif idade_user > 18:
    print("Adulto")
