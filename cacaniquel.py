import random
import time

simbolos = ['🎃', '🤑', '🐯', '🍀', '💎']
saldo = 100

def jogar():
    print("\nGirando...")
    for _ in range(15):
        animacao = [random.choice(simbolos) for _ in range(3)]
        print(f"\r{' | '.join(animacao)}", end="", flush=True)
        time.sleep(0.1)

    print("\n" + "=" * 15)

    resultado = [random.choice(simbolos) for _ in range(3)]
    print(f"{' | '.join(resultado)}")
    print("=" * 15)

    return resultado

def fazer_aposta():
    while True:
        try:
            aposta = int(input(f"Seu saldo atual é de ${saldo}. Digite o valor da sua aposta: "))
            if aposta > saldo:
                print("Você não tem saldo suficiente para esta aposta. Tente novamente.")
            elif aposta <= 0:
                print("A aposta deve ser um valor positivo. Tente novamente.")
            else:
                return aposta
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def main():
    """The main game loop."""
    global saldo
    print("Bem-vindo à Roleta de Símbolos!")
    
    while True:
        if saldo <= 0:
            print("Seu saldo acabou. Fim de jogo!")
            break

        aposta = fazer_aposta()
        saldo -= aposta
        
        resultado = jogar()
        
        # Check for a win
        if resultado[0] == resultado[1] == resultado[2]:
            ganho = aposta * 10
            saldo += ganho
            print(f"🎉 Parabéns! Você acertou! Você ganhou ${ganho}!")
        else:
            print("😞 Que pena! Você perdeu esta rodada.")
        
        print(f"Seu saldo final é: ${saldo}\n")
        
        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()