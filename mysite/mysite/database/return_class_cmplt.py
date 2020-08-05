'''Função que receberá os seguintes parâmetros:
boletins: dicionário com boletins com todos os jogos de cada participante e a pontuação obtida organizadas em dataframes individuais.
classificacao: dataframe de classificação a partir dos pontos, feito anteriormente na "main".

retorno classificacao_completa: classificação com todos os critérios de desempate especificados.
Obedecendo a seguinte regra: (mais acertos de 10 pontos, mais acertos de 7, 
menos acertos de  0, mais acertos de 5, mais 2).
'''
from pandas import concat, DataFrame
from numpy import array


#def return_class_cmplt(boletins,classificacao):
def return_class_cmplt(nomes_dict, classificacao):
    pontos_detalhados = [] #Lista que será formada a partir do laço 'for' que percorrerá o dicionário boletins.
    '''for key in boletins.keys():
        pontos_detalhados_temp = [boletins[key]['Pontos'].tolist().count(10),boletins[key]['Pontos'].tolist().count(7),boletins[key]['Pontos'].tolist().count(5),boletins[key]['Pontos'].tolist().count(2),boletins[key]['Pontos'].tolist().count(0)]
        pontos_detalhados.append(pontos_detalhados_temp)'''

    for k,v in nomes_dict.items():
        pontos_detalhados_temp = [k, v['Pontos'], v['Tabela']['Pontos'].tolist().count(10), v['Tabela']['Pontos'].tolist().count(7), v['Tabela']['Pontos'].tolist().count(5), v['Tabela']['Pontos'].tolist().count(2), v['Tabela']['Pontos'].tolist().count(0)]
        pontos_detalhados.append(pontos_detalhados_temp)
    
    
    
    #pontos_detalhados = array(pontos_detalhados)
    ''' O trecho acima percorre o dicionário boletins a partir do seu conteudo e conta cada ocorrencia de 
     Pontuações de 10,7,5,2 e 0 pontos. Posteriormente a lista pontos_detalhados é convertida em um array.'''
    
    Pontos_df = DataFrame(pontos_detalhados, columns=['Nome', 'Pontos Totais', '10 pontos', '7 pontos', '5 pontos', '2 pontos', '0 pontos'])
    '''Formado o dataframe Pontos_df com os pontos por participante organizado em colunas.'''
    
    #classificacao_completa = concat([classificacao,Pontos_df], axis=1)
    ''' O dataframe classificacao é concatenado com Pontos_df para formar a classificação completa
        Com todos os critérios de desempate especificados, entretanto não ordenados.'''

    classificacao_completa = Pontos_df.sort_values(by=['Pontos Totais', '10 pontos', '7 pontos', '0 pontos', '5 pontos', '2 pontos'],ascending=[0,0,0,1,0,0])
    '''Métodos da biblioteca pandas para reorganizar a classificação e especificar a ordem de critérios.
    A partir daqui o DataFrame classificacao_completa representa a pontuação atual do bolão com
    seus critérios especificados.'''

    classificacao_completa.index = [i+1 for i in range(0, len(classificacao_completa.values))]
    '''Reorganização do index para que comece a partir de 1 e não de 0, que é o default.'''

    classificacao.update([classificacao_completa.columns.values.tolist()] + classificacao_completa.values.tolist())

    '''classificacao_completa = classificacao_completa.to_html()
    classificacao_completa = classificacao_completa.replace('<table border="1" class="dataframe">', '<table style="text-align: center; width:100%">')
    classificacao_completa = classificacao_completa.replace('<tr style="text-align: right;">', '<tr>')
    classificacao_completa = classificacao_completa.replace('<tbody>', '<tbody  style="text-align: center;">')
    classificacao_completa = classificacao_completa.replace("\n", "")

    return classificacao_completa'''