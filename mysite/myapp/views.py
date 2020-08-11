from django.shortcuts import render
from pandas import DataFrame
from django.template import RequestContext
from mysite.database import Main
from mysite.database.return_games import return_games
from mysite.database.return_class_cmplt import return_class_cmplt

RODADA = "Rodada 2"
MES = "Agosto/2020"

# Create your views here.
def index(request):
    content = {}
    gabarito_sheet = Main.get_data('mysite/database/BolaoFutebolClubismo-d44be1b6b394.json','gabarito', RODADA)
    resultados_html = return_games(gabarito_sheet.col_values(1), gabarito_sheet.col_values(2))
    #gabarito = gabarito_sheet.get_all_values()
    
    content['tabela'] = resultados_html
    content['rodada'] = RODADA
    return render(request, 'index.html',content)

def classificacao_rodada(request):
    content = {}
    content['rodada'] = RODADA
    palpites_sheet, gabarito_sheet = Main.get_data('mysite/database/BolaoFutebolClubismo-d44be1b6b394.json','palpites_gabarito', RODADA)
    #placares = list()
    palpites = palpites_sheet.get_all_values()
    gabarito = gabarito_sheet.get_all_values()
    #nome = [[a for a in x if a == x[2]] for x in palpites[1:]]

    i = 0
    #for a in gabarito_sheet.col_values(2):
    for a in gabarito:
        if (a[1] == "-"):
            i = i+1
            if(i == len(gabarito)):
                content['tables'] = '<p style="text-align:central"> A Rodada ainda não começou. </p>'
            return render(request, 'classificacao_rodada.html',content)
        else:
            break
    
    df_format = False
    #content['tables'] = Main.get_boletins(gabarito_sheet,palpites_sheet)
    #content['tables'] = Main.get_boletins(gabarito_sheet,palpites_sheet, df_format)
    content['tables'] = Main.get_boletins(gabarito,palpites, df_format)
    return render(request, 'classificacao_rodada.html',content)

def classificacao_mes(request):
    content = {}
    palpites_sheet, gabarito_sheet, classificacao_sheet = Main.get_data('mysite/database/BolaoFutebolClubismo-d44be1b6b394.json', '', RODADA)
    df_format = True
    gabarito = gabarito_sheet.get_all_values()
    palpites = palpites_sheet.get_all_values()
    #content['tables'] = Main.get_boletins(gabarito_sheet,palpites_sheet)
    nomes_dict = Main.get_boletins(gabarito,palpites, df_format)
    #nomes_dict = Main.get_boletins(gabarito_sheet,palpites_sheet, df_format)

    #classificacao = return_class_cmplt(nomes_dict,classificacao_sheet)
    return_class_cmplt(nomes_dict,classificacao_sheet)
    
    classificacao_mes_sheet = Main.get_data('mysite/database/BolaoFutebolClubismo-d44be1b6b394.json', '', MES)
    
    valores = classificacao_mes_sheet.get_all_values()
    
    valores = [[x if x == a[0] else int(x) for x  in a] for a in valores[1:]]

    classificacao_mes = DataFrame(valores,columns=['Nome', 'Pontos Totais', '10 pontos', '7 pontos', '5 pontos', '2 pontos', '0 pontos'])
    classificacao_mes = classificacao_mes.sort_values(by=['Pontos Totais', '10 pontos', '7 pontos', '0 pontos', '5 pontos', '2 pontos'],ascending=[0,0,0,1,0,0])
    
    classificacao_mes.index = [i+1 for i in range(0, len(classificacao_mes.values))]
    
    classificacao_mes = classificacao_mes.to_html()
    classificacao_mes = classificacao_mes.replace('<table border="1" class="dataframe">', '<table style="text-align: center; width:100%">')
    classificacao_mes = classificacao_mes.replace('<tr style="text-align: right;">', '<tr>')
    classificacao_mes = classificacao_mes.replace('<tbody>', '<tbody  style="text-align: center;">')
    classificacao_mes = classificacao_mes.replace("\n", "")
    
    #content['classificacao'] = return_class_cmplt(nomes_dict,classificacao_sheet)
    content['classificacao'] = classificacao_mes
    return render(request, 'classificacao_mes.html',content)

def classificacao_geral(request):
    content = {}
    content['rodada'] = "Classificacao Geral"
    return render(request, 'classificacao_geral.html',content)

def prox_rodada(request):
    content = {}
    content['rodada'] = RODADA
    return render(request, 'prox_rodada.html',content)

def rodada_seguinte(request):
    content = {}
    content['rodada'] = RODADA
    return render(request, 'rodada_depois.html',content)

def rodada_depois(request):
    content = {}
    content['rodada'] = RODADA
    return render(request, 'rodada_seguinte.html',content)

def regulamento(request):
    content = {}
    content['rodada'] = "Regulamento"
    return render(request, 'regulamento.html',content)

def galeria_campeoes(request):
    content = {}
    content['rodada'] = "Galeria de Campeões"
    return render(request, 'galeria_campeoes.html',content)     