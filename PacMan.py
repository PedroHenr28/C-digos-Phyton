from random import randrange
def criarMatriz():
        matrizJogo = []
        for i in range(25):
            columsIni = []
            for j in range(50):
                columsIni += ['-']
            matrizJogo += [columsIni]
        return matrizJogo

def printarMatriz(matrizJogo):
    matrizToPrint = ''
    for line in matrizJogo:
        for position in line:
            matrizToPrint += position
        matrizToPrint += '\n'
    print(matrizToPrint, end = '\n')

def posicionaPersonagem(Y,X,personagem,matrizJogo):
    matrizJogo[Y][X] = personagem

def movimentaPacMan(Y,X,matrizJogo):
    move = 'none'
    NewY = Y
    NewX = X
    while [NewY,NewX] == [Y,X]:
        move = input()
        if move == '8':
            if Y != 0:
                NewY = Y - 1
            else:
                printarMatriz(matrizJogo)
                move = input()
        elif move == '2':
            if Y != 24:
                NewY = Y + 1
            else:
                printarMatriz(matrizJogo)
                move = input()
        elif move == '6':
            if X != 49:
                NewX = X + 1
            else:
                printarMatriz(matrizJogo)
                move = input()
        elif move == '4':
            if X != 0:
                NewX = X - 1
            else:
                printarMatriz(matrizJogo)
                move = input()
        else:
            printarMatriz(matrizJogo)
    return [NewY,NewX]

def movimentaFantasmas(Y,X):
    move = 'none'
    NewY = Y
    NewX = X
    while [NewY,NewX] == [Y,X]:
        move = str(randrange(2,10,2))
        if move == '8':
            if Y != 0:
                NewY = Y - 1
        elif move == '2':
            if Y != 24:
                NewY = Y + 1
        elif move == '6':
            if X != 49:
                NewX = X + 1
        elif move == '4':
            if X != 0:
                NewX = X - 1
        return [NewY,NewX]
    
    
def main():
    #|----------------------------------------------------------------------- JOGO PACMAN ------------------------------------------------------------------------|
    #ESTADO INICIAL DO JOGO:
    FMorreu = False
    GMorreu = False
    EMorreu = False
    rodada = 0
    while FMorreu == False or GMorreu == False or EMorreu == False:
        #CRIAR A MATRIZ DO JOGO:
            
        matrizJogo = criarMatriz()
        
        #==================  POSICIONAMENTO DOS PERSONAGENS ==================:
        #POSIÇÃO PACMAN:
        personagem = 'P'
        if rodada == 0:
            YP = 24
            XP = 0
            
        posicionaPersonagem(YP,XP,personagem,matrizJogo)

        #POSIÇÃO FANTASMAS:

        if rodada == 0:
            YF,XF,YG,XG,YE,XE = 12,22,12,24,12,26
            
        #FANTASMA1
        personagem = 'F'
        if not FMorreu:
            posicionaPersonagem(YF,XF,personagem,matrizJogo)
        
        #FANTASMA2
        personagem = 'G'
        if not GMorreu:
            posicionaPersonagem(YG,XG,personagem,matrizJogo)
        
        #FANTASMA3
        personagem = 'E'
        if not EMorreu:
            posicionaPersonagem(YE,XE,personagem,matrizJogo)

        #PRINTAR A MATRIZ DO JOGO:
        printarMatriz(matrizJogo)

        #=================  MOVIMENTO DOS PERSONAGENS  ====================:

        #MOVIMENTO PACMAN:
        personagem = 'P'
        move = 'none'
        NewCoordinates = movimentaPacMan(YP,XP,matrizJogo)
        YP = NewCoordinates[0]
        XP = NewCoordinates[1]

        #MOVIMENTO FANTASMAS:
        #FANTASMA1
        personagem = 'F'
        NewCoordinates = movimentaFantasmas(YF,XF)
        YF = NewCoordinates[0]
        XF = NewCoordinates[1]
        
        #FANTASMA2
        personagem = 'G'
        NewCoordinates = movimentaFantasmas(YG,XG)
        YG = NewCoordinates[0]
        XG = NewCoordinates[1]
        
        #FANTASMA3
        personagem = 'E'
        NewCoordinates = movimentaFantasmas(YE,XE)
        YE = NewCoordinates[0]
        XE = NewCoordinates[1]

        #======================= VERIFICAÇÃO: O PERSONAGEM  ESTÁ VIVO? ==========================

        if FMorreu == False:
            if YP == YF and XP == XF:
                FMorreu = True
        if GMorreu == False:
            if YP == YG and XP == XG:
                GMorreu = True
        if EMorreu == False:
            if YP == YE and XP == XE:
                EMorreu = True
                
        rodada += 1

    matrizJogo = criarMatriz()
    posicionaPersonagem(YP,XP,'P',matrizJogo)
    printarMatriz(matrizJogo)        
    print('Parabéns! Você ganhou.')
    SouN = input('Deseja iniciar uma nova partida? (Sim ou não)')
    while FMorreu == True:
        if SouN == 'Sim' or SouN == 'sim':
            main()
        elif SouN == 'Não' or SouN == 'não':
            exit()
        else:
            SouN = input('Não entendi... Deseja iniciar uma nova partida? (Sim ou não)\n')
main()
