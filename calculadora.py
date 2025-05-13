def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {add(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtract(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiply(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculator()