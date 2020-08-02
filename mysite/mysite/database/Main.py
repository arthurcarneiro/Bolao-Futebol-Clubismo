import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd 
import numpy as np
from collections import OrderedDict
from operator import getitem 
from mysite.database.return_rodada import return_rodada
#from return_rodada import return_rodada
from mysite.database.return_class_cmplt import return_class_cmplt
#from return_class_cmplt import return_class_cmplt
#from return_boletins import return_boletins
#from return_games import return_games

RODADA = "Evento Teste"
MES = "Agosto/2020"

def get_data(chave,requisicao, planilha):
# use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    #creds = ServiceAccountCredentials.from_json_keyfile_name('BolaoFutebolClubismo-d44be1b6b394.json', scope)
    creds = ServiceAccountCredentials.from_json_keyfile_name(chave, scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    #sheet = client.open("Cópia de Bolão(Responses)") #>>>Planilha teste
    nome = "Bolão Brasileirão Futebol e Clubismo - " + planilha
    
    sheet = client.open(nome) #>>>Planilha bundesliga
    
    if(planilha == MES):
        classificacao = sheet.sheet1
        return classificacao
    
    if (requisicao == 'palpites'):
        sheet1 = sheet.sheet1 
        return sheet1
    elif (requisicao == 'gabarito'):
        gabarito = sheet.worksheet("Gabarito")
        return gabarito
    elif (requisicao == 'classificacao'):
        classificacao = sheet.worksheet("Classificação")
        return classificacao
    elif (requisicao == 'palpites_gabarito'):
        gabarito = sheet.worksheet("Gabarito")
        sheet1 = sheet.sheet1
        return sheet1, gabarito
    
    gabarito = sheet.worksheet("Gabarito")
    sheet1 = sheet.sheet1
    classificacao = sheet.worksheet("Classificação")
    
    return sheet1, gabarito, classificacao

#chave = 'BolaoFutebolClubismo-d44be1b6b394.json'
#sheet1, gabarito = get_data(chave)
#print(str(type(sheet1)) + str(type(gabarito)))

#palpites_sheet, gabarito_sheet = get_data('mysite/mysite/database/BolaoFutebolClubismo-d44be1b6b394.json')


#def get_boletins(gabarito,palpites):
def get_boletins(gabarito,palpites,df_format):
    #boletins = {}
    boletins = []
    pontos_totais = []
    nomes = palpites.col_values(3)[1:]
    nomes_dict = {}
    
    if (df_format == True):
        #for i in range(0,len(nomes)-1): #>>>>>Feito no Arquivo de testes<<<<
        for i in range(0,len(nomes)): #Feito na bundesliga evento teste
            #lista, pontos_temp = return_rodada(sheet1.row_values(1)[3:],sheet1.row_values(i+2),gabarito.col_values(2))
            lista, pontos_temp = return_rodada(gabarito.col_values(1),palpites.row_values(i+2),gabarito.col_values(2))
            pontos_totais.append(pontos_temp)


            #boletins[i] = boletins.append(pd.DataFrame(lista, columns = ['Jogo', 'Palpites','Gabarito', 'Pontos'])
            boletins.append(pd.DataFrame(lista, columns = ['Jogo', 'Palpites','Gabarito', 'Pontos']))
            '''boletins[i] = boletins[i].to_html(index =False)
            boletins[i] = boletins[i].replace('<table border="1" class="dataframe">', '<table style="text-align: center; width:100%">')
            boletins[i] = boletins[i].replace('<tr style="text-align: right;">', '<tr>')
            boletins[i] = boletins[i].replace('<tbody>', '<tbody  style="text-align: center;">')
            boletins[i] = boletins[i].replace("\n", "")'''
            nomes_dict.update({nomes[i] : {'Pontos': pontos_totais[i], 'Tabela': boletins[i]}})
    else:
        for i in range(0,len(nomes)): #Feito na bundesliga evento teste
            #lista, pontos_temp = return_rodada(sheet1.row_values(1)[3:],sheet1.row_values(i+2),gabarito.col_values(2))
            lista, pontos_temp = return_rodada(gabarito.col_values(1),palpites.row_values(i+2),gabarito.col_values(2))
            pontos_totais.append(pontos_temp)


            #boletins[i] = boletins.append(pd.DataFrame(lista, columns = ['Jogo', 'Palpites','Gabarito', 'Pontos'])
            boletins.append(pd.DataFrame(lista, columns = ['Jogo', 'Palpites','Gabarito', 'Pontos']))
            boletins[i] = boletins[i].to_html(index =False)
            boletins[i] = boletins[i].replace('<table border="1" class="dataframe">', '<table style="text-align: center; width:100%">')
            boletins[i] = boletins[i].replace('<tr style="text-align: right;">', '<tr>')
            boletins[i] = boletins[i].replace('<tbody>', '<tbody  style="text-align: center;">')
            boletins[i] = boletins[i].replace("\n", "")
            nomes_dict.update({nomes[i] : {'Pontos': pontos_totais[i], 'Tabela': boletins[i]}})

    nomes_dict = OrderedDict(sorted(nomes_dict.items(), key = lambda x: getitem(x[1], 'Pontos'), reverse=True))

    nomes_dict = dict(nomes_dict)

        
    
    #lista_jog_pontos = list(zip(nomes, pontos_totais,boletins.values()))
    #lista_jog_pontos = list(zip(nomes, pontos_totais,boletins))
    
    #lista_jog_pontos = sorted(lista_jog_pontos, key = lambda t: t[1],reverse=True)
    #nomes_dict = {}
    

    
    '''for i in range(0,len(lista_jog_pontos)):
        #boletins[i] = lista_jog_pontos[i][2]
        #nomes[i] = lista_jog_pontos[i][0]'''
        #nomes_dict.update({lista_jog_pontos[i][0] : {0: lista_jog_pontos[i][1], 1:lista_jog_pontos[i][2]}})
    
    
    return nomes_dict
    #return nomes_dict, boletins

#debugging_nomes = get_boletins(gabarito_sheet,palpites_sheet)

'''classificacao = pd.DataFrame(lista_jog_pontos, columns=['Nome', 'Pontos Totais', 'boletins'])
classificacao = classificacao.sort_values(by='Pontos Totais', ascending=False)
classificacao.index = [i+1 for i in range(0,len(classificacao.values))]
'''
#classificacao_detalhada = return_class_cmplt(boletins, classificacao)
#print(classificacao_detalhada)

'''
classificacao = classificacao.sort_values(by='Pontos Totais', ascending=False)
classificacao.index = [i+1 for i in range(0,len(classificacao.values))]'''

'''
pontos_detalhados = []
for key in boletins.keys():
    print("\n" +"="*53)
    print(key+1,end='')
    print(" - " + nomes[key] + " "*(29-len(nomes[key])) + "Total de Pontos: ",end='')
    print(pontos_totais[key])
    print("-"*53)
    print(boletins[key])'''

#return_boletins(boletins,nomes,pontos_totais)
 



