# Calculadora.py  (versão corrigida para os 3 bugs indicados)
import numpy as np

def adicao(x, y):
    # BUG 1 CORRIGIDO: retornar x + y (antes somava x duas vezes)
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return np.multiply(x, y)

def divisao(x, y):
    # BUG 2 CORRIGIDO: tratar divisão por zero
    if y == 0:
        # lançar erro controlado para que o chamador decida o que exibir
        raise ValueError("Divisão por zero")
    return x / y

def potencia(x, y):
    return np.power(x, y)

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Raiz quadrada de número negativo")
    return np.sqrt(x)

def fatorial(x):
    # implementação simples e segura (aceita int ou float inteiro)
    if not (isinstance(x, int) or (isinstance(x, float) and x.is_integer())):
        raise ValueError("Fatorial só definido para inteiros não-negativos")
    n = int(x)
    if n < 0:
        raise ValueError("Fatorial de número negativo")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def logaritmo_natural(x):
    if x <= 0:
        raise ValueError("Logaritmo só definido para x > 0")
    return np.log(x)

def logaritmo_base10(x):
    if x <= 0:
        raise ValueError("Logaritmo só definido para x > 0")
    return np.log10(x)

def seno(x_de_graus):
    # entrada em graus
    return np.sin(np.deg2rad(x_de_graus))

def cosseno(x_de_graus):
    return np.cos(np.deg2rad(x_de_graus))

def tangente(x_de_graus):
    # cuidado com cos ~= 0
    rad = np.deg2rad(x_de_graus)
    cos_val = np.cos(rad)
    if abs(cos_val) < 1e-12:
        raise ValueError("Tangente indefinida para este ângulo")
    return np.tan(rad)

# ----------------------------
# UTILITÁRIOS DE INPUT (BUG 03: validação robusta)
# ----------------------------
def input_float(prompt):
    while True:
        try:
            s = input(prompt)
            # permitir que usuário cancele com vazio (opcional)
            if s.strip() == "":
                print("Entrada vazia. Tente novamente.")
                continue
            return float(s)
        except ValueError:
            print("Entrada inválida: por favor digite um número válido.")

def input_int(prompt):
    while True:
        try:
            s = input(prompt)
            if s.strip() == "":
                print("Entrada vazia. Tente novamente.")
                continue
            return int(s)
        except ValueError:
            print("Entrada inválida: por favor digite um inteiro válido.")

# ----------------------------
# Fluxo interativo (mantén-lo simples)
# ----------------------------
def menu():
    print("\nBem-vindo à Calculadora")
    print("0. Sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Logaritmo Natural (ln)")
    print("9. Logaritmo Base 10")
    print("10. Seno (graus)")
    print("11. Cosseno (graus)")
    print("12. Tangente (graus)")

def calculadora_cientifica():
    while True:
        menu()
        escolha = input("Digite o número da operação: ").strip()
        if escolha == '0':
            print("Encerrando.")
            break

        try:
            if escolha in ['1','2','3','4','5']:
                x = input_float("Digite o primeiro número: ")
                y = input_float("Digite o segundo número: ")

                if escolha == '1':
                    print("Resultado:", adicao(x, y))
                elif escolha == '2':
                    print("Resultado:", subtracao(x, y))
                elif escolha == '3':
                    print("Resultado:", multiplicacao(x, y))
                elif escolha == '4':
                    # divisao pode levantar ValueError em y==0
                    try:
                        print("Resultado:", divisao(x, y))
                    except ValueError as e:
                        print("Erro:", e)
                elif escolha == '5':
                    print("Resultado:", potencia(x, y))

            elif escolha == '6':
                x = input_float("Digite o número: ")
                try:
                    print("Resultado:", raiz_quadrada(x))
                except ValueError as e:
                    print("Erro:", e)

            elif escolha == '7':
                x = input_float("Digite o inteiro não-negativo: ")
                try:
                    print("Resultado:", fatorial(x))
                except ValueError as e:
                    print("Erro:", e)

            elif escolha == '8':
                x = input_float("Digite o número (>0): ")
                try:
                    print("Resultado:", logaritmo_natural(x))
                except ValueError as e:
                    print("Erro:", e)

            elif escolha == '9':
                x = input_float("Digite o número (>0): ")
                try:
                    print("Resultado:", logaritmo_base10(x))
                except ValueError as e:
                    print("Erro:", e)

            elif escolha == '10':
                x = input_float("Digite o ângulo (graus): ")
                print("Resultado:", seno(x))

            elif escolha == '11':
                x = input_float("Digite o ângulo (graus): ")
                print("Resultado:", cosseno(x))

            elif escolha == '12':
                x = input_float("Digite o ângulo (graus): ")
                try:
                    print("Resultado:", tangente(x))
                except ValueError as e:
                    print("Erro:", e)

            else:
                print("Opção inválida. Tente novamente.")

        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Encerrando.")
            break

if __name__ == "__main__":
    calculadora_cientifica()
