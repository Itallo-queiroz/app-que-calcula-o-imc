# inicia o loop
while True:
    nome = input('informe seu nome: ')
    peso = str(input('informe seu peso em kg: ')).replace(',', '.')
    altura = str(input('informe sua altura: ')).replace(',', '.')

    # converte
    peso = float(peso)
    altura = float(altura)

    # Calcule o imc
    imc = peso / (altura ** 2)

    # mostra o valor do imc
    print(f'IMC de {nome}: {imc:,.2f}. ')

    # diagnostico
    if imc <= 16:
        print(f'{nome} está muito abaixo do peso.')
        print('por favor procure um medico!')
    elif imc < 16.9:
        print(f'{nome} ainda está abaixo do peso.')
        print('procure um medico!')
    elif imc < 18.5:
        print(f'{nome} magreza leve.')
        print('procure um medico!')
    elif imc < 29.9:
        print(f'{nome} peso ideal.')
        print('Meus parabens!')
    elif imc < 29.9:
        print(f'{nome} sobre peso.')
        print('procure um medico ')
    elif imc < 34.9:
        print(f'{nome} obesidade grau I')
        print(' fazer uma cirugia!')

    # verificar se o usuario deseja continuar
    continuar = input('Deseja continuar (s/n)?').lower()

    # verifica a opção escolhida pelo usuario
    if continuar == 's':
        continue
    break  
