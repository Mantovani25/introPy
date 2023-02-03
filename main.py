# 1 - Imports / Bibliotecas

# 2 - Classe

# 3 - Métodos e Funções
# def = definition = definição
def print_hi(name):
    print(f'Oi, {name}') # Depois do Python 3
    print('Oi, ' + name) # Antes do Python

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calculara_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento /2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de zero até o fim
        print(numero)         # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'. format(numero))


# estrutura de identificação / execucão do script
if __name__ == '__main__':


    resposta = 'C'

    while resposta.upper() != 'Z':

        print('#####################################')
        print('#                                   #')
        print('#    M E N U   D E   O P Ç Õ E S    #')
        print('#                                   #')
        print('#   1 - Olá Mundo                   #')
        print('#   2 - Área do Retâmgulo           #')
        print('#   3 - Área do Quadrado            #')
        print('#   4 - Área do Triângulo           #')
        print('#   5 - Contagem progressiva        #')
        print('#   6 - Apoiar Candidato            #')
        print('#   7 - Brincar de Plim             #')
        print('#                                   #')
        print('#    Z - Sair                       #')
        print('#                                   #')
        print('#####################################')

        resposta= input("Escola sua opção")
        print(f'A sua ecolha foi: {resposta}')

        if resposta .upper() != 'Z':
            if resposta == '1':
                print_hi('Vinicius')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f'A área do retângulo é de {resultado}m²')
            elif resposta == '3':
                resultado = calculara_area_do_quadrado(6)
                print(f'A área do quadrado é de {resultado}m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f'A área do triângulo é de{resultado}m²')
            elif resposta == '5':
                contagem_progressiva(10)
            elif resposta == '6':
                apoiar_candidato('bolsonaro', 13)
            elif resposta == '7':
                brincar_de_plim(7)
            else:
                print('Você digitou uma opção inválida. Escolha uma opção de 1 a 7')
        else:
            print('Você escolheu sair, Volte sempre!')








