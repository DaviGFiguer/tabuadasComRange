num1 = int(input())
num2 = int(input())

if(num1 > num2):
    print('Nenhuma tabuada no intervalo!')

else:
    numAtual = num1

    tabuada = 1

    while numAtual <= num2:

        for tabuada in range(1, 11):
            resultado = numAtual*tabuada

            print(f'{numAtual} x {tabuada} = {resultado}')

            tabuada += 1

        print('----------')
        numAtual += 1
