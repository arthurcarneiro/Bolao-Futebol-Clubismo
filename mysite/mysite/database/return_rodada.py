from mysite.database.return_pts import return_pts
#from return_pts import return_pts  
def return_rodada(jogos, resultados_pessoa,gabarito):
    pontuacao = 0
    
    #resultados = [[int(x) for x in a] for a in [k.split('x') for k in resultados_pessoa[3:3+len(gabarito)]]]
    resultados = [[-1,-1] if a == [''] else [int(x) for x in a] for a in [k.split('x') 
    for k in resultados_pessoa[3:3+len(gabarito)]]]
    ''' recebe valores dos resultados de um participante em uma lista contendo, nome, email e resultados
    valor é convertido para uma lista contendo somente os x resultados de cada jogo em listas, com total x de jogos. 
    cada resultado é armazenado em uma lista contendo 2 inteiros.'''

    resultados_gabarito = [[-1,-1] if a == ['-'] else [int(x) for x in a] for a in [k.split('x') for k in gabarito]]
    ''' 'resultados_gabarito' recebe valores de gabarito que possui resultados corretos dos jogos em uma lista 
     e o placar é convertido para  inteiros uma lista contendo x placares de cada jogo em listas, com comprimento de x jogos. 
    cada resultado é armazenado em uma lista contendo 2 inteiros, que é a quantidade de gols marcados por cada time.'''

    
    pontuacao = [return_pts(resultados[i],resultados_gabarito[i]) for i in range(0,len(resultados))]

    rodada = list(zip(jogos, resultados_pessoa[3:], gabarito, pontuacao))

    return rodada, sum(pontuacao)
