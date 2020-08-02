import pandas as pd
def return_games(jogos, gabarito):

    times_separados = [a for a in [k.split(' x ') for k in jogos]]
    ''' 'resultados_gabarito' recebe valores de gabarito que possui resultados corretos dos jogos em uma lista 
     e o placar é convertido para  inteiros uma lista contendo x placares de cada jogo em listas, com comprimento de x jogos. 
    cada resultado é armazenado em uma lista contendo 2 inteiros, que é a quantidade de gols marcados por cada time.'''
    #resultados_final_shape_list = [[a[0], c, a[1]] for a,c in zip(times_separados,gabarito)]
    resultados_final_shape_list = [['<td style="text-align:right; width:45%">' + a[0], '<td style="text-align:center; width:10%">' + c, '<td style="text-align:left; width:45%">' + a[1]] 
    for a,c in zip(times_separados,gabarito)]
    #results_final_shape = [[  ]]
    resultados_final_shape_df = pd.DataFrame(resultados_final_shape_list)
    resultados_final_shape = resultados_final_shape_df.to_html(index =False, header = False)
    resultados_final_shape = resultados_final_shape.replace("\n", "")
    resultados_final_shape = resultados_final_shape.replace('<td>', '')
    resultados_final_shape = resultados_final_shape.replace('&lt;', '<')
    resultados_final_shape = resultados_final_shape.replace('&gt;', '>')
    resultados_final_shape = resultados_final_shape.replace('<table border="1" class="dataframe">', '<table style= "text-align=center; width:100%">')
    #resultados_final_shape = resultados_final_shape.replace('<table border="1" class="dataframe">', '<table style="width = 100%; margin-center:auto;">')

    return resultados_final_shape
