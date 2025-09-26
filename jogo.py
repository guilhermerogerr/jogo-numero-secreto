import random
nsecreto = random.randint(0,1001)
n = ()
tentativa = 0
pontos = 1000

print("🎯 Bem-vindo ao Jogo do Número Secreto!")
print("💡 Descubra o número secreto e tente manter sua pontuação alta!")
print("⚠️ Cada tentativa errada reduz 50 pontos. Boa sorte! 🍀\n")


while (nsecreto != n):
    n = int(input('Dígite um número: '))
    tentativa += 1
    pontos -= 50

    if pontos == 0:
        print(f"💀 Você perdeu! O número secreto era {nsecreto}")
        break

    elif pontos > 0:
        if nsecreto > n:
            print(f'🔺O número secreto é maior que {n}')
        elif nsecreto < n:
            print(f'🔻O número secreto é menor que {n}')
        print(f'📌 Essa é a sua {tentativa}ª tentativa\n')

if nsecreto == n:
    print(f'🎉 Parabéns você acertou na {tentativa}ª tentativa, o número secreto era {nsecreto}.')
    print(f'⭐ Pontuação final: {pontos} ⭐')