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

def calcular_area_do_treiangulo(largura, comprimento):
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

def exibir_dia_da_semana_if(numero):
    print('Execução com if')
    if numero== 1:
        print('O dia é segunda')
    elif numero == 2:
        print('O dia é terça')
    elif numero == 3:
        print('O dia é quarta')
    elif numero == 4:
        print('O dia é quinta')
    elif numero == 5:
        print('O dia sexta')
    elif numero == 6:
        print('O dia é sábado')
    elif numero == 7:
        print('O dia é domingo')
    else:
        print('Número de dia inválido. Digite um número de 1 a 7')

'''
def  exibir_dia_da_semana_match(numero):
    print('Execução com match')
    match numero:
        case 1:
            print('O dia é segunda')
        case 2:
            print('O dia é terça')
        case 3:
            print('O dia é quarta')
        case 4:
            print('O dia é quinta')
        case 5:
            print('O dia é sexta')
        case 6:
            print('O dia é sábado')
        case 7:
            print('O dia é domingo')
            
            
'''


def brincar_de_para_ou_continua():
    resposta = 'C' # C aqui significa que continua

    #while resposta == 'C' or resposta == 'c':
    while resposta.upper() == 'C':
        resposta = input('Digite C para continuar ou qualquer outro caracter para parar')

    print('Você decidiu parar com a brincadeira')



# estrutura de identificação / execucão do script
if __name__ == '__main__':
    print_hi('Vinicius')

    # chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retângulo é de {resultado}m²')

    # chamar a função de cálculo do quadrado
    resultado = calculara_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado}m²')

    # chamar a função de cálculo da área do triângulo
    resultado = calcular_area_do_treiangulo(6,7)
    print(f'A área do triângulo é de {resultado}m²')

    # executar uma contagem progressiva
    contagem_progressiva(11)

    # exibir o nome do candidato várias vezes
    apoiar_candidato('bolsonaro', 100)

    # brincar de plim
    brincar_de_plim(100)

    # exemplo de dia da semana com if - elif - else
    # exibir_dia_da_semana_if(3)

    # exemplo de dia da semana com march - case
    # exibir_dia_da_semana_match(5)

    #exemplo com while - para ou continua
    brincar_de_para_ou_continua()



