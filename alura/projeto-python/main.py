# # EXERCIO 1

# print('Bem vindo ao python!')

# print('Vamos estudar!')

# print('Oi meu nome e\n Pedro!')

# EXERCIO 2 - JOGO DE ADVINHACAO // for

# import os
# import random

# repetir = 0
# tentativa = 0
# jogada = 5

# for x in range(1, jogada):
    
#     os.system('clear')

#     print('******************************')
#     print('*    JOGO DE ADVINHACAO      *')
#     print('******************************')

#     # numero secreto gerado automaticamente com a biblioteca random
#     gerar_numero = random.randint(1, 10)
#     numero_secreto = gerar_numero

#     # entrada do usuario
#     numero_jogador = int(input('Digite um numero: '))

#     if numero_jogador == numero_secreto:
#         print('ACERTOU!')
#         print('TENTATIVAS: ', tentativa)
        
#     else:
#         print('ERROU!')
#         print('O NUMERO CORRETO E: ', numero_secreto)
#         tentativa += 1
        
#     repetir = int(input('1 - SAIR | 0 - CONTINUAR: '))
    
#     # EXERCIO DE ADVINHACAO / while
    
# import os
# import random

# repetir = 0
# tentativa = 0

# while repetir == 0:
    
#     os.system('clear')

#     print('******************************')
#     print('*    JOGO DE ADVINHACAO      *')
#     print('******************************')

#     # numero secreto gerado automaticamente com a biblioteca random
#     gerar_numero = random.randint(1, 10)
#     numero_secreto = gerar_numero

#     # entrada do usuario
#     numero_jogador = int(input('Digite um numero: '))

#     if numero_jogador == numero_secreto:
#         print('ACERTOU!')
#         print('TENTATIVAS: ', tentativa)
            
#     else:
#         print('ERROU!')
#         print('O NUMERO CORRETO E: ', numero_secreto)
#         tentativa += 1
            
#     repetir = int(input('1 - SAIR | 0 - CONTINUAR: '))