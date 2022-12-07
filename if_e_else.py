num1 = int(input("Digite um número: "))

if num1 > 10:
    print(num1, " é maior que 10")
    if num1 < 15:
        print(num1, " é maior que 10 e menor que 15")
    else:
        if num1 < 50:
            print(num1, " é menor que 50")
            if num1 > 30:
                print(num1, " é maior que 30")
            else:
                print(num1, " é menor que 50 e menor ou igual que 30")
        else:
            print(num1, " é maior que 50")
            if num1 < 100:
                print(num1, " é menor que 100")
                if num1 > 70:
                    print(num1, " é maior que 70")
                else:
                    print(num1, " é maior que 70 e menor que 100")
            else:
                print(num1, " é maior que 100")
else:
    if num1 > 5:
        print(num1, " é maior que 5")
        if num1 == 7:
            print(num1, " é igual a 7")
    else:
        print(num1, " é menor que 5")
