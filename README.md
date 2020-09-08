# Bolao-Futebol-Clubismo
Django Application com informações a respeito do Bolão Futebol e Clubismo. Torneio entre amigos que classifica a partir de pontos diversos palpites do Campeonato Brasileiro.

No mesmo constam informações com as pontuações dos participantes para a rodada, o mês e o campeonato completo.

A partir deste repositório pode-se atualizar todas as informações para as rodadas do campeonato brasileiro de 2020.

As informações são armazenadas em um banco de dados utilizando-se de google spreadsheets e as bibliotecas gspread e oauth2 são as que extraem os dados pela API do google.

O arquivo json gerado pelo google que integra o código à API foi retirado do repositório por questões de segurança.

O front-end foi extraído a partir de um bootstrap em html e css que passou por sutis modificações, os créditos encontram-se no site.

O back-end é em pandas para a análise dos dados e todos os dataframes são exportados em html para posterior inserção na página.

O site é hospedado a partir do servidor gratuito pythonanywhere e pode ser acessado pelo seguinte link: https://bit.ly/FutebolClubismo
