#Grupo 3 (Pedro Henrique Rabaça, Luis Felipe Santos Diniz e Pedro Amorim de Oliveira)
def  printarMatriz(matriz):
    '''Função que dada uma matriz, printa a matriz como está em um visual mais agradável
    e de fácil entendimento para o usuário.
    List --> None.'''
    for linha in matriz:
        s = ' '
        print('\t','\t',s.join(linha), end = '\n')
    print('')

def tamanhoCorreto (coordenada):
    '''Função que analisa o tamanho da string da coordenada de entrada e avalia se está correta (= 5), se sim, retorna True,
    se não ,retorna False.
    Str --> Bool'''
    return len(coordenada) == 5
         

def coordenadaCorreta (coordenada):
    '''Função que, dada uma string coordenada no formato \'[x,y]\' como entrada, analisa se x e y são valores válidos (entre 0 e 2)
    e, também, se está esteticamente válida (x e y entre colchetes e separados por vírgula). Se tudo estiver correto, retorna True,
    se não, retorna False.
    Str --> Bool'''
    if tamanhoCorreto (coordenada):
        x = int(coordenada[1])
        y = int(coordenada[3])
        return not( x != 0 and x != 1 and x != 2 or y != 0 and y != 1 and y != 2 or coordenada[0] != '[' or coordenada[2] != ',' or coordenada[4] != ']')
    return False

def posiçãoCorreta (matriz, coordenada):
    '''Função que recebe X ou O, uma matriz do jogo da velha e uma coordenada no formato \'[x,y]\', respectivamente, e verifica se a posição informada já
    está ocupada por X ou O. Se não, retorna True, se sim ,retorna False.
    List, Str --> Bool'''
    if coordenadaCorreta (coordenada):
        x = int(coordenada[1])
        y = int(coordenada[3])
        return matriz[x][y] == '-'
    return False

def informaçãoCorreta (matriz, STRCoordenada, jogador):
    '''Função que recebe uma matriz, uma coordenada tipo string e um jogador. Ela verifica se a coordenada é válida, se não for,
    pede uma nova coordenada ao usuário, até que ela seja válida. Então, quando for correta, a função retorna essa coordenada.
    List, Str, Str --> Str.'''
    okays = []
    while okays != ['ok','ok','ok']:
        okays = []
        #Avaliação 1: O tamanho da string coordenada está correta?
        if tamanhoCorreto (STRCoordenada): 
            okays += ['ok']
            
        #Avaliação 2: A coordenada é numérica e esteticamente válida?
        if coordenadaCorreta(STRCoordenada):
            okays += ['ok']
            
        #Avaliação 3: A coordenada informada já está ocupada?
        if posiçãoCorreta (matriz, STRCoordenada):
            okays += ['ok']
        if okays != ['ok','ok','ok']:
            STRCoordenada = input('Posição inválida - {} escolha uma posição no formato [x,y]:\n'.format(jogador))
    return STRCoordenada

def linhaCompleta (XouO, matriz):
    '''Função que recebe 'X' ou 'O' como primeiro parâmetro e uma matriz, como segundo. Então, analisa se há alguma linha completa com uma
    dessas duas letras, se sim, parabeniza o jogador correspondente pela vitória (X --> Jogador1 e O --> Jogador2) e pergunta se deseja iniciar
    uma nova partida, caso sim, reinicia o jogo, se não, encerra ele.
    Str, List --> None'''
    jogador = ''
    if XouO == 'X':
        jogador = 'Jogador 1'
    elif XouO == 'O':
        jogador = 'Jogador 2'
    for linha in matriz:
            if linha == 3*[XouO]:
                resposta = input('{} venceu o jogo. Deseja iniciar uma nova partida?\n'.format(jogador))
                reiniciaOuEncerra(resposta)

def matrizTransposta (matriz):
    '''Função que dada uma matriz como entrada, troca suas colunas por suas linhas e retorna a nova matriz obtida.
    List --> List'''
    Conjunto = matriz[0] + matriz[1] + matriz[2]
    NovaLinha1 = Conjunto[::3]
    NovaLinha2 = Conjunto[1::3]
    NovaLinha3 = Conjunto[2::3]
    NovaMatriz = [NovaLinha1] + [NovaLinha2] + [NovaLinha3]
    return NovaMatriz

def colunaCompleta (XouO, matriz):
    '''Função que recebe 'X' ou 'O' como primeiro parâmetro e uma matriz, como segundo. Então, analisa se há alguma coluna completa com uma
    dessas duas letras, se sim, parabeniza o jogador correspondente pela vitória (X --> Jogador1 e O --> Jogador2) e pergunta se deseja iniciar
    uma nova partida, caso sim, reinicia o jogo, se não, encerra ele.
    Str, List --> None'''
    NovaMatriz = matrizTransposta (matriz)
    linhaCompleta (XouO, NovaMatriz)

def diagonalCompleta (XouO, matriz):
    '''Função que recebe 'X' ou 'O' como primeiro parâmetro e uma matriz, como segundo. Então, analisa se há alguma diagonal completa com uma
    dessas duas letras, se sim, parabeniza o jogador correspondente pela vitória (X --> Jogador1 e O --> Jogador2) e pergunta se deseja iniciar
    uma nova partida, caso sim, reinicia o jogo, se não, encerra ele.
    Str, List --> None'''
    jogador = ''
    if XouO == 'X':
        jogador = 'Jogador 1'
    elif XouO == 'O':
        jogador = 'Jogador 2'
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == XouO or matriz[0][2] == matriz[1][1] == matriz[2][0] == XouO:
        resposta = input('{} venceu o jogo. Deseja iniciar uma nova partida?\n'.format(jogador))
        reiniciaOuEncerra(resposta)
    

def reiniciaOuEncerra(resposta):
    '''Função que recebe uma string, se essa for 'S', o jogo da velha é reiniciado, se for 'N', o jogo é encerrado, e se for algo
    diferente dos dois é solicitada uma nova resposta ao usuário até estar correta. Não há valor de retorno.
    Str --> None'''
    while resposta != 'S' and resposta != 'N':
        resposta = input('Não entendi. Deseja iniciar uma nova partida?\n')
    if resposta == 'S':
        main()
    elif resposta == 'N':
        exit()
    
    

def main():
    #INFORMAR AS REGRAS E O OBJETIVO DO JOGO DA VELHA AOS USUÁRIOS:
    print('--------------------------------- JOGO DA VELHA --------------------------------------\n\nRegras do jogo:\n--> Número de jogadores: 2\n--> O primeiro jogador a completar uma linha, coluna ou diagonal com X ou O ganha o jogo.\n--> Caso ninguém consiga realizar esse feito, ocorre um empate.\n--> As coordenadas do jogo da velha obedece as coordenadas de uma matriz 3x3, ou seja, vai de 0 a 2 para a linha e para a coluna \'[x,y]\'.\n\n')

    #CRIAÇÃO DA MATRIZ:
        
    matriz = [['-','-','-'],['-','-','-'],['-','-','-']]
    printarMatriz(matriz)

    jogadasJ1 = 0
    for TotJogadasJ1 in range(5):

        #-------------------------------------------CICLO DO JOGO-------------------------------------------------------:

        #MOSTRAR A MATRIZ E PEDIR INFORMAÇÕES AO JOGADOR 1:
                
        STRCoordenadaJ1 = input('Jogador 1 - escolha uma posição no formato [x,y]:\n')
        jogadasJ1 += 1
        
        #--------------------AVALIAÇÃO DA INFORMAÇÃO J1-------------------------------:            
        XouO = 'X'
        jogador = 'Jogador 1'
                        
        STRCoordenadaJ1 = informaçãoCorreta (matriz, STRCoordenadaJ1, jogador)
            
        x = int(STRCoordenadaJ1[1])
        y = int(STRCoordenadaJ1[3])

        #---------------------------------------------------------------------------

        #Alteração da matriz do jogo da velha, mostrando-a ao usuário:
                
        matriz[x][y] = 'X'
        printarMatriz(matriz)

        #----------------------------1a AVALIAÇÃO DO JOGO------------------------------:
        #--------> JOGADOR 1 GANHOU (X) ?
        XouO = 'X'
                
        #AVALIAÇÃO DAS LINHAS:

        linhaCompleta (XouO, matriz)

        #AVALIAÇÃO DAS COLUNAS:

        colunaCompleta (XouO, matriz)

        #AVALIAÇÃO DAS DIAGONAIS:

        diagonalCompleta (XouO, matriz)

        #-------------------------------------------------------------------------------

        #MOSTRAR A MATRIZ ATUALIZADA E PEDIR INFORMAÇÃO AO JOGADOR 2:
        if jogadasJ1 < 5:
            STRCoordenadaJ2 = input('Jogador 2 - escolha uma posição no formato [x,y]:\n')

            #--------------------AVALIAÇÃO DA INFORMAÇÃO J2-------------------------------:            
            XouO = 'O'
            jogador = 'Jogador 2'
                            
            STRCoordenadaJ2 = informaçãoCorreta (matriz, STRCoordenadaJ2, jogador)

            x = int(STRCoordenadaJ2[1])
            y = int(STRCoordenadaJ2[3])
            #-------------------------------------------------------------------------------

            #Alteração da matriz do jogo da velha, mostrando-a ao usuário:
                    
            matriz[x][y] = 'O'
            printarMatriz(matriz)

            #----------------------------2a AVALIAÇÃO DO JOGO------------------------------

            #--------> JOGADOR 2 GANHOU (O) ?
            XouO = 'O'
                    
            #AVALIAÇÃO DAS LINHAS:
                    
            linhaCompleta (XouO, matriz)

            #AVALIAÇÃO DAS COLUNAS:
                                    
            colunaCompleta (XouO, matriz)

            #AVALIAÇÃO DAS DIAGONAIS:

            diagonalCompleta (XouO, matriz)

            #--------------------------------------------------------------------------------

        #Comunicar que deu empate e perguntar ao usuário se quer encerrar ou reiniciar o jogo:

    resposta = input('Empate. Deseja iniciar uma nova partida?\n')
    reiniciaOuEncerra(resposta)
    
main()


#Testes:
#a ordem das entradas se alterna entre o jogador 1 e o jogador 2,começando sempre com o jogador 1
#possiveis vitorias do jogador 1 (x):
#[0,0]->[1,1]->[1,0]->[2,2]->[2,0]->vitoria do jogador 1
#[0,1]->[0,2]->[1,1]->[2,2]->[2,1]->vitoria do jogador 1
#[0,2]->[1,0]->[2,2]->[1,1]->[1,2]->vitoria do jogador 1
#[0,0]->[2,2]->[0,2]->[1,1]->[0,1]->vitoria do jogador 1
#[1,0]->[2,0]->[1,2]->[0,0]->[1,1]->vitoria do jogador 1
#[2,2]->[1,0]->[2,0]->[1,2]->[2,1]->vitoria do jogador 1
#[0,2]->[2,2]->[2,0]->[0,0]->[1,1]->vitoria do jogador 1
#[0,0]->[1,2]->[2,2]->[2,0]->[1,1]->vitoria do jogador 1
#possiveis vitorias do jogador 2 (O):
#[1,1]->[0,0]->[2,2]->[1,0]->[0,2]->[2,0]->vitoria do jogador 2
#[1,2]->[2,1]->[2,2]->[1,1]->[0,0]->[0,1]->vitoria do jogador 2
#[2,0]->[1,0]->[2,1]->[1,1]->[0,2]->[1,2]->vitoria do jogador 2
#[1,1]->[2,2]->[2,0]->[0,2]->[0,0]->[1,2]->vitoria do jogador 2
#[1,0]->[0,0]->[1,1]->[0,0]->[2,2]->[0,2]->vitoria do jogador 2
#[1,0]->[2,0]->[1,2]->[2,1]->[0,0]->[2,2]->vitoria do jogador 2
#[1,0]->[0,0]->[1,2]->[2,2]->[2,0]->[1,1]->vitoria do jogador 2
#[1,2]->[0,2]->[0,1]->[2,0]->[0,0]->[1,1]->vitoria do jogador 2
#possivel caso de empate:
#[0,0]->[1,1]->[2,2]->[2,1]->[0,1]->[0,2]->[2,0]->[1,0]->[1,2]--> Empate
#posições inválidas (será solicitada que o usuário digite novamente no formato correto):
#2,1
#2
#(1,2)
#[7,8]
#[1;2]
#1-1


    
