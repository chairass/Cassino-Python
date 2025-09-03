import random
import time
import keyboard

simbolos = ['🎃', '🤑', '🐯', '🍀', '💎']
resultado = ["","",""] 
saldo = 100


def jogar():
    # girar roleta
    for i in range(3):
        resul = [random.choice(simbolos) for _ in range(3)] 
        print(resul[0] + ' | ' + resul[1] + ' | ' + resul[2])
        time.sleep(0.2)
        if keyboard.is_pressed('q'):
            print("\nJogo encerrado. Obrigado por jogar!")
            exit()

    for i in range(3):
        resultado[i] = random.choice(simbolos)
        

def calcular_ganho():
    aposta = int(input("Digite o valor da sua aposta (entre 0 e 100): "))
    if 1 <= aposta <= 1000:
        
        return aposta
    else:
        print("O valor informado é inválido.")
        exit()

if __name__ == "__main__":
    aposta = calcular_ganho()
    jogar()
    print(' | '.join(resultado))
    if resultado[0] == resultado[1] == resultado[2]:
        ganho = aposta * 10
        print(f'Parabéns! Você ganhou {ganho}!')
    else:
        print('Que pena! Você perdeu sua aposta.')
        ganho = aposta - 5
        5
        print(f'Seu saldo final é: {ganho}')